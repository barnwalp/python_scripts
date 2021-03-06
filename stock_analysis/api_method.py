import requests
import json
from datetime import date


def get_stock_data(ticker, endpoint, report_type):
    today = date.today().strftime('%Y-%m-%d')
    # ticker = 'IOC'
    # report_type = 'income-statement'
    url = f'https://morningstar1.p.rapidapi.com/{endpoint}/{report_type}'

    querystring = {"Ticker": ticker,"Mic":"XNSE"}

    headers = {
        'accept': "string",
        'x-rapidapi-key': "5015d61e13mshcbb3771deca7b37p19c7c8jsnc900286d0d7b",
        'x-rapidapi-host': "morningstar1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        # get the response data in readable format
        json_object = json.dumps(response.json(), sort_keys=True, indent=4)
    else:
        print(response.status_code)

    path = "C:\\Users\\panka\\github_repo\\share"
    report_name = report_type.split('/')[0]
    path_to_file = f'{path}\\{ticker}_{report_name}_{today}.json'
    with open(path_to_file, 'w') as f:
        f.write(json_object)

def get_general_data(endpoint, report_type):
    today = date.today().strftime('%Y-%m-%d')
    url = f'https://morningstar1.p.rapidapi.com/{endpoint}/{report_type}'

    querystring = {"Mic":"XNSE"}

    headers = {
        'accept': "string",
        'x-rapidapi-key': "5015d61e13mshcbb3771deca7b37p19c7c8jsnc900286d0d7b",
        'x-rapidapi-host': "morningstar1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        # get the response data in readable format
        json_object = json.dumps(response.json(), sort_keys=True, indent=4)
    else:
        print(response.status_code)

    path = "C:\\Users\\panka\\github_repo\\share"
    report_name = report_type.split('/')[0]
    path_to_file = f'{path}\\{report_name}_{today}.json'
    with open(path_to_file, 'w') as f:
        f.write(json_object)

