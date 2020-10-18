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

    max_dist = '10000'
    keyword = 'Walmart'
    search_type = 'department_store'
    stores_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}' \
                 f'&radius={max_dist}&type={search_type}&keyword={keyword}&key={google_api_key}'
    store_responses = requests.get(stores_url).json()['results']

    store_infos = list(map(get_store_info, store_responses))
    return store_infos


def get_address_and_distances(store_infos, user_geo_coord):
    google_api_key = os.getenv('GOOGLE_API_KEY')

    user_lat, store_long = user_geo_coord

    for store_info in store_infos:
        store_lat = store_info['geo_coord']['lat']
        store_long = store_info['geo_coord']['lng']
        distance_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={user_lat},{store_long}' \
                       f'&destinations={store_lat},{store_long}&key={google_api_key}'
        distance_response = requests.get(distance_url).json()
        store_info['address'] = distance_response['destination_addresses'][0]
        store_info['distance'] = distance_response['rows'][0]['elements'][0]['distance']['value']

    store_infos = list(filter(lambda store_info: not(store_info['address'].startswith('Unnamed Road')), store_infos))

    store_infos = sorted(store_infos, key=lambda store_info: store_info['distance'])

    return store_infos

