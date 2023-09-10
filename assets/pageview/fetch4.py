from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    MetricType,
    RunReportRequest,
)
import re;
import yaml
import datetime

PROPERTY_ID = '319747791'

def run_sample():
    """Runs the sample."""
    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID before running the sample.
    property_id = PROPERTY_ID
    run_report(property_id)


def run_report(property_id=PROPERTY_ID):
    """Runs a report of active users grouped by country."""
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pagePath")],
        metrics=[Metric(name="screenPageViews")],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    )
    response = client.run_report(request)
    print_run_report_response(response)

def save_results(resultMap, type):
    # Print data nicely for the user.
    if len(resultMap):

        with open("../../_data/rank.yaml", "r") as file:
            final_result = yaml.load(file.read())

        if not final_result:
            print ("No previous record found")
            final_result = {
                'meta': {
                    'previous_date': None,
                    'current_date': datetime.date.today().isoformat()
                },
                'distributions' : [],
                'desktops': []
            }
        elif not 'desktops' in final_result:
            final_result['desktops'] = []
        else:
            final_result['meta']['previous_date'] = final_result['meta']['current_date']
            final_result['meta']['current_date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        processed = []

        rank = 1

        for url in resultMap:

            if not re.match(r"\/" + type + "\/", url): continue

            distribution = None
            for d in final_result['distributions' if type == 'distribution' else 'desktops']:
                if d['url'] == url:
                    distribution = d
                    break

            if not distribution:
                distribution = {
                    'url': url,
                    'previous': None,
                    'current': None
                }
                final_result['distributions' if type == 'distribution' else 'desktops'].append(distribution)

            distribution['previous'] = distribution['current']
            distribution['current'] = {
                'rank': rank,
                'count': int(resultMap[url])
            }
            processed.append(url)
            rank += 1

        for d in final_result['distributions' if type == 'distribution' else 'desktops']:
            if d['url'] not in processed:
                d['previous'] = d['current']
                d['current'] = {
                    'rank': rank,
                    'count': 0
                }
                rank += 1

        # ut.sort(key=lambda x: x.count, reverse=True)
        final_result['distributions' if type == 'distribution' else 'desktops'].sort(key = lambda x: x['current']['rank'])

        with open("../../_data/rank.yaml", "w") as file:
            file.write(yaml.safe_dump(final_result, default_flow_style=False))


        print ('Done')

    else:
        print ('No results found')

def print_run_report_response(response):
    """Prints results of a runReport call."""
    print(f"{response.row_count} rows received")

    resultMap = {}

    for rowIdx, row in enumerate(response.rows):
        
        url = row.dimension_values[0].value
        
        if re.match(r"\/desktop\/.+|\/distribution\/.+", url):
            resultMap[url] = 0

            for i, metric_value in enumerate(row.metric_values):
                metric_name = response.metric_headers[i].name
                resultMap[url] = metric_value.value

    print(resultMap)

    save_results(resultMap, 'desktop')
    save_results(resultMap, 'distribution')

run_sample()

