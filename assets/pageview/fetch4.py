from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
import re
import yaml
import datetime
import os

PROPERTY_ID = "319747791"
RANK_FILE = "../../_data/rank.yaml"


def run_sample():
    run_report(PROPERTY_ID)


def run_report(property_id):
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pagePath")],
        metrics=[Metric(name="screenPageViews")],  # safer for web-only sites
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    )

    response = client.run_report(request)
    print_run_report_response(response)


def load_rank_file():
    if not os.path.exists(RANK_FILE):
        return {
            "meta": {
                "previous_date": None,
                "current_date": datetime.date.today().isoformat(),
            },
            "distributions": [],
            "desktops": [],
        }

    with open(RANK_FILE, "r") as f:
        data = yaml.safe_load(f) or {}

    data.setdefault("meta", {})
    data.setdefault("distributions", [])
    data.setdefault("desktops", [])

    data["meta"]["previous_date"] = data["meta"].get("current_date")
    data["meta"]["current_date"] = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )

    return data


def save_rank_file(data):
    with open(RANK_FILE, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False)


def save_results(result_map, category):
    if not result_map:
        print("No results found for", category)
        return

    final_result = load_rank_file()
    target_key = "distributions" if category == "distribution" else "desktops"
    target_list = final_result[target_key]

    # sort by views DESC (critical fix)
    sorted_items = sorted(
        result_map.items(), key=lambda x: x[1], reverse=True
    )

    processed = set()
    rank = 1

    for url, count in sorted_items:
        if not re.match(rf"\/{category}\/", url):
            continue

        entry = next((d for d in target_list if d["url"] == url), None)

        if not entry:
            entry = {"url": url, "previous": None, "current": None}
            target_list.append(entry)

        entry["previous"] = entry["current"]
        entry["current"] = {"rank": rank, "count": count}

        processed.add(url)
        rank += 1

    # pages that disappeared this run
    for entry in target_list:
        if entry["url"] not in processed:
            entry["previous"] = entry["current"]
            entry["current"] = {"rank": rank, "count": 0}
            rank += 1

    target_list.sort(key=lambda x: x["current"]["rank"])
    save_rank_file(final_result)

    print(f"Saved {category} rankings")


def print_run_report_response(response):
    print(f"{response.row_count} rows received")

    result_map = {}

    for row in response.rows:
        url = row.dimension_values[0].value

        if re.match(r"\/(desktop|distribution)\/.+", url):
            value = int(row.metric_values[0].value)
            result_map[url] = value

    save_results(result_map, "desktop")
    save_results(result_map, "distribution")


run_sample()
