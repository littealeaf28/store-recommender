import requests
import os
import json
from datetime import datetime


def add_busyness(store_info):
    best_time_url = 'https://besttime.app/api/v1/forecasts'
    best_time_api_key = os.getenv('BEST_TIME_API_KEY')

    params = {
        'api_key_private': best_time_api_key,
        'venue_name': store_info['name'],
        'venue_address': store_info['address']
    }
    forecast_response = requests.post(best_time_url, params=params).json()

    if forecast_response['status'] == 'error':
        return None

    # with open('busyness.json', 'a') as busyness_file:
    #     json.dump(forecast_response, busyness_file, indent=4, sort_keys=True)

    # now_weekday = datetime.today().weekday()
    # now_hour = datetime.now().hour
    #
    # print(forecast_response[forecast_response][now_weekday])

    return store_info


def get_prev_busyness(store_infos):
    with open('busyness.json', 'r') as busyness_file:
        forecast_response = json.load(busyness_file)

    now_weekday = datetime.today().weekday()
    now_hour = datetime.now().hour

    print(forecast_response['analysis'][now_weekday])


def get_busyness(store_infos):
    # store_infos = list(map(add_busyness, store_infos))

    # for store_info in store_infos:
    get_prev_busyness()

    for store_info in store_infos:
        print(store_info)

    return store_infos
