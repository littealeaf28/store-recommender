import requests


def get_busyness(store_info):
    url = 'https://besttime.app/api/v1/forecasts'

    # live forecast
    params = {
        'api_key_private': 'private-key',
        'venue_name': 'name',
        'venue_address': 'address'
    }