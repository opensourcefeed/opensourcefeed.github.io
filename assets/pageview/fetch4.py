"""Build _data/rank.yaml from Google Analytics 4 page views.

For every period (last 30 days, last 3 months) two reports are fetched:
the current window and the window immediately before it. The "previous"
rank of an entry is its rank in that preceding window, so rank changes
reflect real period-over-period trends rather than the last script run.

Only URLs that belong to an existing distribution/desktop page are ranked.
Hits on redirect aliases (``redirect_from``) are merged into the canonical
page, and everything else (games, UUID paths, typos, ...) is dropped.
"""

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
import datetime
import glob
import os
import re
import yaml

PROPERTY_ID = "319747791"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, "..", ".."))
RANK_FILE = os.path.join(SITE_ROOT, "_data", "rank.yaml")

PERIODS = [
    {"key": "d30", "label": "Last 30 days", "days": 30, "legacy": True},
    {"key": "m3", "label": "Last 3 months", "days": 90, "legacy": False},
]

CATEGORIES = {
    "distribution": "distributions",
    "desktop": "desktops",
}

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)


# ---------------------------------------------------------------------------
# Page registry (valid URLs + aliases) built from the site's front matter
# ---------------------------------------------------------------------------

def clean_path(url):
    """Strip query/fragment, trailing slash and case so paths compare equal."""
    if not url:
        return None
    clean = str(url).split("?", 1)[0].split("#", 1)[0].strip().lower()
    if not clean.startswith("/"):
        clean = "/" + clean
    if clean != "/":
        clean = clean.rstrip("/")
    return clean


def category_of(path):
    match = re.match(r"^/(distribution|desktop)/[^/]+$", path or "")
    return match.group(1) if match else None


def read_front_matter(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read(20000)
    except OSError:
        return None
    match = FRONT_MATTER.match(text)
    if not match:
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def build_page_registry():
    """Return (canonical_pages, aliases).

    canonical_pages: {path: category}
    aliases: {alias_path: canonical_path}
    """
    canonical = {}
    aliases = {}

    files = glob.glob(os.path.join(SITE_ROOT, "distribution-*.md"))
    files += glob.glob(os.path.join(SITE_ROOT, "desktop-*.md"))

    for file_path in sorted(files):
        fm = read_front_matter(file_path)
        if not fm or fm.get("redirect_to"):
            continue

        permalink = clean_path(fm.get("permalink"))
        category = category_of(permalink)
        if not category:
            continue

        canonical[permalink] = category

        redirects = fm.get("redirect_from") or []
        if isinstance(redirects, str):
            redirects = [redirects]
        for alias in redirects:
            alias_path = clean_path(alias)
            if alias_path and alias_path != permalink:
                aliases[alias_path] = permalink

    return canonical, aliases


def resolve_url(raw_url, canonical, aliases):
    path = clean_path(raw_url)
    if not path:
        return None
    path = aliases.get(path, path)
    return path if path in canonical else None


# ---------------------------------------------------------------------------
# Google Analytics
# ---------------------------------------------------------------------------

def window_dates(days, offset_days=0, today=None):
    """Inclusive date window of `days` days ending `offset_days` before today."""
    today = today or datetime.date.today()
    end = today - datetime.timedelta(days=offset_days)
    start = end - datetime.timedelta(days=days - 1)
    return start, end


def run_report(client, property_id, start, end, canonical, aliases):
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pagePath")],
        metrics=[Metric(name="screenPageViews")],
        date_ranges=[DateRange(start_date=start.isoformat(), end_date=end.isoformat())],
        limit=100000,
    )

    response = client.run_report(request)
    print(f"{response.row_count} rows received for {start} .. {end}")

    counts = {}
    for row in response.rows:
        url = resolve_url(row.dimension_values[0].value, canonical, aliases)
        if not url:
            continue
        counts[url] = counts.get(url, 0) + int(row.metric_values[0].value)

    return counts


# ---------------------------------------------------------------------------
# Ranking
# ---------------------------------------------------------------------------

def rank_counts(counts):
    """Ordinal ranks by count desc (ties broken by URL); zero counts dropped."""
    items = sorted(
        ((url, count) for url, count in counts.items() if count > 0),
        key=lambda x: (-x[1], x[0]),
    )
    return {url: {"rank": i, "count": count} for i, (url, count) in enumerate(items, start=1)}


def build_ranking(current_counts, previous_counts, category, canonical):
    def only(counts):
        return {u: c for u, c in counts.items() if canonical.get(u) == category}

    current = rank_counts(only(current_counts))
    previous = rank_counts(only(previous_counts))

    leader = max((v["count"] for v in current.values()), default=0)

    entries = []
    for url, cur in sorted(current.items(), key=lambda x: x[1]["rank"]):
        score = max(1, round(cur["count"] * 100 / leader)) if leader else 0
        prev = previous.get(url)
        entries.append({
            "url": url,
            "current": {"rank": cur["rank"], "count": cur["count"], "score": score},
            "previous": prev,
            "change": (prev["rank"] - cur["rank"]) if prev else None,
        })
    return entries


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_reports(property_id):
    canonical, aliases = build_page_registry()
    print(f"{len(canonical)} ranked pages, {len(aliases)} aliases")

    client = BetaAnalyticsDataClient()
    today = datetime.date.today()

    data = {
        "meta": {
            "current_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "periods": {},
        },
        "rankings": {},
    }

    for period in PERIODS:
        cur_start, cur_end = window_dates(period["days"], 0, today)
        prev_start, prev_end = window_dates(period["days"], period["days"], today)

        current_counts = run_report(client, property_id, cur_start, cur_end, canonical, aliases)
        previous_counts = run_report(client, property_id, prev_start, prev_end, canonical, aliases)

        data["meta"]["periods"][period["key"]] = {
            "label": period["label"],
            "current": {"start": cur_start.isoformat(), "end": cur_end.isoformat()},
            "previous": {"start": prev_start.isoformat(), "end": prev_end.isoformat()},
        }

        bucket = data["rankings"].setdefault(period["key"], {})
        for category, key in CATEGORIES.items():
            bucket[key] = build_ranking(current_counts, previous_counts, category, canonical)
            print(f"Saved {len(bucket[key])} {key} for {period['label']}")

            # Legacy root keys (read by distribution/desktop layouts) mirror d30.
            if period["legacy"]:
                data[key] = bucket[key]

    save_rank_file(data)


def save_rank_file(data):
    with open(RANK_FILE, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    run_reports(PROPERTY_ID)
