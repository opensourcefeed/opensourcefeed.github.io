"""A simple example of how to access the Google Analytics API."""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import re
from collections import OrderedDict
from operator import itemgetter

import yaml
import datetime

def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service


def get_first_profile_id(service):
    # Use the Analytics service object to get the first profile id.

    # Get a list of all Google Analytics accounts for this user
    accounts = service.management().accounts().list().execute()

    if accounts.get('items'):
        # Get the first Google Analytics account.
        account = accounts.get('items')[0].get('id')

        # Get a list of all the properties for the first account.
        properties = service.management().webproperties().list(
                accountId=account).execute()

        if properties.get('items'):
            # Get the first property id.
            property = properties.get('items')[0].get('id')

            # Get a list of all views (profiles) for the first property.
            profiles = service.management().profiles().list(
                    accountId=account,
                    webPropertyId=property).execute()

            if profiles.get('items'):
                # return the first view (profile) id.
                return profiles.get('items')[0].get('id')

    return None


def get_results(service, profile_id, type):
    # Use the Analytics Service Object to query the Core Reporting API
    # for the number of sessions within the past seven days.
    return service.data().ga().get(
            ids='ga:' + profile_id,
            start_date='30daysAgo',
            end_date='today',
            metrics='ga:uniquePageviews',
            dimensions='ga:pagePath',
            sort='-ga:uniquePageviews',
            filters='ga:pagePath=~/' + type + '/.+').execute()


def save_results(service, profile_id, type):

    results = get_results(service, profile_id, type)
    # Print data nicely for the user.
    if results:
        rows = results.get('rows')
        rank = 1
        prog = re.compile(r'\/'+type+'\/[a-z0-9]+')
        map = {}
        for row in rows:
            if not prog.search(row[0]): continue

            url = re.sub(r'.*(/'+type+'/[a-z0-9]+).*', r"\1", row[0])
            if url in map:
                map[url] = map[url] + int(row[1])
            else:
                map[url] = int(row[1])

        map = OrderedDict(sorted(map.items(), key=itemgetter(0)))
        map = OrderedDict(sorted(map.items(), key=itemgetter(1), reverse=True))
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

        for url in map:
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
                'count': map[url]
            }
            processed.append(url);
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


def main():
    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'
    key_file_location = '../../../secret.json'

    # Authenticate and construct service.
    service = get_service(
            api_name='analytics',
            api_version='v3',
            scopes=[scope],
            key_file_location=key_file_location)

    profile_id = get_first_profile_id(service)
    save_results(service, profile_id, 'distribution')
    save_results(service, profile_id, 'desktop')


if __name__ == '__main__':
    main()