import requests
import os
# import json
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

    now_weekday = datetime.today().weekday()
    # now_hour = datetime.now().hour
    now_hour = 12

    forecast_day = forecast_response['analysis'][now_weekday]
    for forecast_hour in forecast_day['hour_analysis']:
        if forecast_hour['hour'] == now_hour:
            store_info['hour_intensity'] = forecast_hour['intensity_nr']
            break

    if store_info['hour_intensity'] == '999':
        return None

    store_info['surge_hours'] = forecast_day['surge_hours']
    store_info['quiet_hours'] = forecast_day['quiet_hours']
    store_info['busy_hours'] = forecast_day['busy_hours']
    return store_info


# def get_prev_busyness(store_info):
#     with open('busyness.json', 'r') as busyness_file:
#         forecast_response = json.load(busyness_file)
#
#     now_weekday = datetime.today().weekday()
#     now_hour = datetime.now().hour
#
#     forecast_day = forecast_response['analysis'][now_weekday]
#     for forecast_hour in forecast_day['hour_analysis']:
#         if forecast_hour['hour'] == now_hour:
#             store_info['hour_intensity'] = forecast_hour['intensity_nr']
#             break
#
#     if store_info['hour_intensity'] == '999':
#         return None
#
#     store_info['surge_hours'] = forecast_day['surge_hours']
#     store_info['quiet_hours'] = forecast_day['quiet_hours']
#     store_info['busy_hours'] = forecast_day['busy_hours']
#     return store_info


def get_busyness(store_infos):
    store_infos = list(map(add_busyness, store_infos))
    # store_infos[0] = get_prev_busyness(store_infos[0])

    store_infos = list(filter(lambda store_info: store_info is not None, store_infos))

    return store_infos
