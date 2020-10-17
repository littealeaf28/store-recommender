import requests
import os


def get_address(geo_coord):
    api_key = os.getenv('API_KEY')

    lat = geo_coord['lat']
    long = geo_coord['lng']
    reverse_geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},' \
                          f'{long}&key={api_key}'

    address_response = requests.get(reverse_geocode_url).json()
    return address_response['results'][0]['formatted_address']


def get_store_locations(lat, long):
    api_key = os.getenv('API_KEY')

    max_dist = '20000'
    keyword = 'Walmart'
    search_type = 'department_store'
    stores_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}' \
                 f'&radius={max_dist}&type={search_type}&keyword={keyword}&key={api_key} '
    store_responses = requests.get(stores_url).json()['results']

    if len(store_responses) == 0:
        return 'None'

    store_geo_coords = map(lambda store_response: store_response['geometry']['location'], store_responses)

    store_addresses = map(get_address, store_geo_coords)

    for result in store_addresses:
        print(result)

    return 'Hello'

# def
