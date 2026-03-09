from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
import datetime
import os
import re
import yaml

PROPERTY_ID = "319747791"
RANK_FILE = "../../_data/rank.yaml"

PERIODS = [
    {
        "key": "d30",
        "label": "Last 30 days",
        "start_date": "30daysAgo",
        "legacy": True,
    },
    {
        "key": "m3",
        "label": "Last 3 months",
        "start_date": "90daysAgo",
        "legacy": False,
    },
]

URL_PATTERN = re.compile(r"^/(desktop|distribution)/[a-z0-9][a-z0-9\-]*(?:/[a-z0-9][a-z0-9\-]*)*$")


def run_sample():
    run_reports(PROPERTY_ID)


def run_reports(property_id):
    client = BetaAnalyticsDataClient()
    data = load_rank_file()

    for period in PERIODS:
        result_map = run_report(client, property_id, period["start_date"])
        save_results(result_map, "desktop", period, data)
        save_results(result_map, "distribution", period, data)

    save_rank_file(data)


def run_report(client, property_id, start_date):
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pagePath")],
        metrics=[Metric(name="screenPageViews")],
        date_ranges=[DateRange(start_date=start_date, end_date="today")],
    )

    response = client.run_report(request)
    print(f"{response.row_count} rows received for start date {start_date}")

    result_map = {}
    for row in response.rows:
        raw_url = row.dimension_values[0].value
        url = normalize_url(raw_url)
        if not url:
            continue

        value = int(row.metric_values[0].value)
        result_map[url] = value

    return result_map


def normalize_url(url):
    if not url:
        return None

    clean = url.split("?", 1)[0].split("#", 1)[0].strip()

    if clean != "/" and clean.endswith("/"):
        clean = clean.rstrip("/")

    if "//" in clean:
        return None

    if not URL_PATTERN.match(clean):
        return None

    return clean


def load_rank_file():
    if not os.path.exists(RANK_FILE):
        return new_rank_file()

    with open(RANK_FILE, "r") as f:
        data = yaml.safe_load(f) or {}

    data.setdefault("meta", {})
    data["meta"]["previous_date"] = data["meta"].get("current_date")
    data["meta"]["current_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    rankings = data.setdefault("rankings", {})

    # Backward compatibility: migrate legacy root lists into d30 bucket if missing.
    d30_bucket = rankings.setdefault("d30", {})
    d30_bucket.setdefault("distributions", data.get("distributions", []))
    d30_bucket.setdefault("desktops", data.get("desktops", []))

    m3_bucket = rankings.setdefault("m3", {})
    m3_bucket.setdefault("distributions", [])
    m3_bucket.setdefault("desktops", [])

    # Keep legacy keys available for templates/scripts that still read them.
    data.setdefault("distributions", d30_bucket["distributions"])
    data.setdefault("desktops", d30_bucket["desktops"])

    return data


def new_rank_file():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return {
        "meta": {
            "previous_date": None,
            "current_date": now,
        },
        "rankings": {
            "d30": {"distributions": [], "desktops": []},
            "m3": {"distributions": [], "desktops": []},
        },
        "distributions": [],
        "desktops": [],
    }


def save_rank_file(data):
    with open(RANK_FILE, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)


def save_results(result_map, category, period, data):
    if not result_map:
        print(f"No results found for {category} ({period['key']})")
        return

    bucket = data["rankings"][period["key"]]
    target_key = "distributions" if category == "distribution" else "desktops"
    target_list = bucket[target_key]

    sorted_items = sorted(result_map.items(), key=lambda x: x[1], reverse=True)

    processed = set()
    rank = 1

    for url, count in sorted_items:
        if not re.match(rf"^/{category}/", url):
            continue

        entry = next((d for d in target_list if d.get("url") == url), None)
        if not entry:
            entry = {"url": url, "previous": None, "current": None}
            target_list.append(entry)

        entry["previous"] = entry.get("current")
        entry["current"] = {"rank": rank, "count": count}

        processed.add(url)
        rank += 1

    for entry in target_list:
        if entry.get("url") not in processed:
            entry["previous"] = entry.get("current")
            entry["current"] = {"rank": rank, "count": 0}
            rank += 1

    target_list.sort(key=lambda x: x.get("current", {}).get("rank", 10**9))

    # Keep legacy root arrays synced to last 30 days data.
    if period["legacy"]:
        data[target_key] = target_list

    print(f"Saved {category} rankings for {period['label']}")


if __name__ == "__main__":
    run_sample()
