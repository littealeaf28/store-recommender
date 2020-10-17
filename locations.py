import requests
import os


# def get_address(geo_coord):
#     api_key = os.getenv('API_KEY')
#
#     lat = geo_coord['lat']
#     long = geo_coord['lng']
#     reverse_geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},' \
#                           f'{long}&key={api_key}'
#
#     address_response = requests.get(reverse_geocode_url).json()
#     return address_response['results'][0]['formatted_address']


def get_store_info(store_response):
    return {'name': store_response['name'], 'geo_coord': store_response['geometry']['location']}


def get_locations(user_geo_coord):
    google_api_key = os.getenv('GOOGLE_API_KEY')

    lat, long = user_geo_coord

    max_dist = '20000'
    keyword = 'Walmart'
    search_type = 'department_store'
    stores_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}' \
                 f'&radius={max_dist}&type={search_type}&keyword={keyword}&key={google_api_key}'
    store_responses = requests.get(stores_url).json()['results']

    if len(store_responses) == 0:
        raise Exception('No stores within the designated max radius')

    store_infos = list(map(get_store_info, store_responses))
    return store_infos


def add_address(store_info, address):
    store_info['address'] = address
    return store_info


def add_distance(store_info, distance_response):
    store_info['distance'] = distance_response['distance']['text']
    return store_info


def get_address_and_distances(store_infos, user_geo_coord):
    google_api_key = os.getenv('GOOGLE_API_KEY')

    lat, long = user_geo_coord

    destination_str = ''
    for store_geo_coord in store_infos:
        lat = store_geo_coord['geo_coord']['lat']
        long = store_geo_coord['geo_coord']['lng']
        destination_str = destination_str + f'{lat},{long}|'
    destination_str = destination_str[:-1]

    distance_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?unit=imperial&origins={lat},{long}' \
                   f'&destinations={destination_str}&key={google_api_key}'
    distance_responses = requests.get(distance_url).json()

    store_addresses = distance_responses['destination_addresses']

    store_infos = list(map(add_address, store_infos, store_addresses))
    store_infos = list(map(add_distance, store_infos, distance_responses['rows'][0]['elements']))
    return store_infos

