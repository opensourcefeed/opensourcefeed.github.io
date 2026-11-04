"""Build _data/rank.yaml from Google Analytics 4 page views.

For every period (last 30 days, last 3 months) two reports are fetched:
the current window and the window immediately before it. The "previous"
rank of an entry is its rank in that preceding window, so rank changes
reflect real period-over-period trends rather than the last script run.

Only URLs that belong to an existing distribution/desktop page are ranked.
Hits on redirect aliases (``redirect_from``) are merged into the canonical
page, and everything else (games, UUID paths, typos, ...) is dropped.

History: every run also makes sure a frozen snapshot exists for each of the
last MONTHS_BACK complete calendar months and for each complete year since
FIRST_YEAR (``_data/rank_history/<key>.yaml``), plus an archive page stub for
each one (``rank-archive/<key>.md``). Existing snapshots and stubs are never
overwritten unless ``--rebuild-history`` is passed. Top entries in the live
30-day ranking get a ``trend`` (monthly ranks, oldest first, then the
current rank) used for sparklines.

Usage:  python3 fetch4.py [--rebuild-history]
"""

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
import argparse
import datetime
import glob
import os
import re
import yaml

PROPERTY_ID = "319747791"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, "..", ".."))
RANK_FILE = os.path.join(SITE_ROOT, "_data", "rank.yaml")
HISTORY_DIR = os.path.join(SITE_ROOT, "_data", "rank_history")
ARCHIVE_DIR = os.path.join(SITE_ROOT, "rank-archive")
# Live ranking pages whose <title> carries the current month, e.g. "(November 2026)".
DATED_TITLE_PAGES = [
    os.path.join(SITE_ROOT, "page-hit-rank.md"),
    os.path.join(SITE_ROOT, "page-hit-rank-desktops.md"),
]

MONTHS_BACK = 12      # monthly snapshots kept up to date / used for trends
FIRST_YEAR = 2023     # first year-in-review page (GA4 data starts mid-2022)

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
# History: monthly / yearly snapshots and archive pages
# ---------------------------------------------------------------------------

def month_bounds(year, month):
    start = datetime.date(year, month, 1)
    end = (start + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)
    return start, end


def shift_month(year, month, delta):
    index = year * 12 + (month - 1) + delta
    return index // 12, index % 12 + 1


def complete_months(today, count):
    """The last `count` complete calendar months, oldest first."""
    year, month = shift_month(today.year, today.month, -count)
    return [shift_month(year, month, i) for i in range(count)]


def month_label(year, month):
    return datetime.date(year, month, 1).strftime("%B %Y")


def snapshot_path(key):
    return os.path.join(HISTORY_DIR, f"{key}.yaml")


def load_snapshot(key):
    path = snapshot_path(key)
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return yaml.safe_load(f)


def write_archive_stub(snapshot, rebuild):
    key = snapshot["key"]
    path = os.path.join(ARCHIVE_DIR, f"{key}.md")
    if os.path.exists(path) and not rebuild:
        return

    if snapshot["kind"] == "year":
        title = f"Most Popular Linux Distros of {snapshot['label']}"
        description = (f"The most-viewed Linux distributions, BSDs and desktop environments on "
                       f"OpenSourceFeed in {snapshot['label']}, with rank changes from {snapshot['compare_label']}.")
        permalink = f"/page-hit-rank/{key}/"
    else:
        title = f"Most Popular Linux Distributions – {snapshot['label']}"
        description = (f"Top Linux distributions, BSDs and desktop environments by OpenSourceFeed page views "
                       f"in {snapshot['label']}, with rank changes from {snapshot['compare_label']}.")
        permalink = "/page-hit-rank/" + key.replace("-", "/") + "/"

    front = {
        "layout": "rank-archive",
        "archive_key": key,
        "archive_kind": snapshot["kind"],
        "title": title,
        "description": description,
        "permalink": permalink,
        "image": "/assets/images/meta/logo-collage.png",
    }
    if snapshot["kind"] == "month":
        # Monthly pages are templated and overlap the live ranking: keep them for
        # readers but out of search results. Year-in-review pages stay indexable.
        front["robots"] = "noindex, follow"
        front["sitemap"] = False
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    with open(path, "w") as f:
        f.write("---\n")
        yaml.safe_dump(front, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        f.write("---\n")
    print(f"Wrote archive page {path}")


def make_snapshot(client, property_id, canonical, aliases, key, kind, label,
                  cur, prev, compare_label, rebuild):
    current_counts = run_report(client, property_id, cur[0], cur[1], canonical, aliases)
    previous_counts = run_report(client, property_id, prev[0], prev[1], canonical, aliases)

    snapshot = {
        "key": key,
        "kind": kind,
        "label": label,
        "compare_label": compare_label,
        "period": {"start": cur[0].isoformat(), "end": cur[1].isoformat()},
        "previous_period": {"start": prev[0].isoformat(), "end": prev[1].isoformat()},
        "generated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    for category, list_key in CATEGORIES.items():
        snapshot[list_key] = build_ranking(current_counts, previous_counts, category, canonical)

    os.makedirs(HISTORY_DIR, exist_ok=True)
    with open(snapshot_path(key), "w") as f:
        yaml.safe_dump(snapshot, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    print(f"Saved snapshot {key}")
    write_archive_stub(snapshot, rebuild)


def ensure_history(client, property_id, canonical, aliases, today, rebuild=False):
    for year, month in complete_months(today, MONTHS_BACK):
        key = f"{year}-{month:02d}"
        if os.path.exists(snapshot_path(key)) and not rebuild:
            continue
        py, pm = shift_month(year, month, -1)
        make_snapshot(client, property_id, canonical, aliases, key, "month",
                      month_label(year, month), month_bounds(year, month),
                      month_bounds(py, pm), month_label(py, pm), rebuild)

    for year in range(FIRST_YEAR, today.year):
        key = str(year)
        if os.path.exists(snapshot_path(key)) and not rebuild:
            continue
        make_snapshot(client, property_id, canonical, aliases, key, "year", str(year),
                      (datetime.date(year, 1, 1), datetime.date(year, 12, 31)),
                      (datetime.date(year - 1, 1, 1), datetime.date(year - 1, 12, 31)),
                      str(year - 1), rebuild)

    # Recreate any missing archive page for snapshots that already exist.
    for path in sorted(glob.glob(os.path.join(HISTORY_DIR, "*.yaml"))):
        snapshot = load_snapshot(os.path.splitext(os.path.basename(path))[0])
        if snapshot:
            write_archive_stub(snapshot, False)


def attach_trends(data, today):
    """Add monthly rank trends (last MONTHS_BACK months + current) to d30 entries."""
    months = complete_months(today, MONTHS_BACK)
    snapshots = [load_snapshot(f"{y}-{m:02d}") or {} for y, m in months]
    data["meta"]["trend_months"] = [datetime.date(y, m, 1).strftime("%b %Y") for y, m in months] + ["Now"]

    for list_key in CATEGORIES.values():
        ranks_by_month = [
            {e["url"]: e["current"]["rank"] for e in snap.get(list_key, [])}
            for snap in snapshots
        ]
        for entry in data["rankings"]["d30"][list_key]:
            entry["trend"] = [ranks.get(entry["url"]) for ranks in ranks_by_month] + [entry["current"]["rank"]]


def update_dated_titles(today):
    """Replace the "(Month YYYY)" part of the live pages' front-matter title."""
    month = today.strftime("%B %Y")
    pattern = re.compile(r"^(title:.*\()[A-Z][a-z]+ \d{4}(\).*)$", re.M)
    for path in DATED_TITLE_PAGES:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        updated = pattern.sub(lambda m: m.group(1) + month + m.group(2), text, count=1)
        if updated != text:
            with open(path, "w", encoding="utf-8") as f:
                f.write(updated)
            print(f"Updated title month in {os.path.basename(path)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_reports(property_id, rebuild_history=False):
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

    ensure_history(client, property_id, canonical, aliases, today, rebuild_history)
    attach_trends(data, today)
    update_dated_titles(today)

    save_rank_file(data)


def save_rank_file(data):
    with open(RANK_FILE, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--rebuild-history", action="store_true",
                        help="regenerate all monthly/yearly snapshots and archive page stubs")
    args = parser.parse_args()
    run_reports(PROPERTY_ID, rebuild_history=args.rebuild_history)
