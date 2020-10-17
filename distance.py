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


def get_store_locations(user_geo_coord):
    api_key = os.getenv('API_KEY')

    lat, long = user_geo_coord

    max_dist = '20000'
    keyword = 'Walmart'
    search_type = 'department_store'
    stores_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}' \
                 f'&radius={max_dist}&type={search_type}&keyword={keyword}&key={api_key}'
    store_responses = requests.get(stores_url).json()['results']

    if len(store_responses) == 0:
        raise Exception('No stores within the designated max radius')

    store_geo_coords = map(lambda store_response: store_response['geometry']['location'], store_responses)
    # store_addresses = map(get_address, store_geo_coords)

    # return [store_geo_coords, store_addresses]
    return store_geo_coords


def get_address_and_distances(user_geo_coord, store_geo_coords):
    api_key = os.getenv('API_KEY')

    lat, long = user_geo_coord

    destination_str = ''
    for store_geo_coord in store_geo_coords:
        lat = store_geo_coord['lat']
        long = store_geo_coord['lng']
        destination_str = destination_str + f'{lat},{long}|'
    destination_str = destination_str[:-1]

    distance_url = f'https://maps.googleapis.com/maps/api/distancematrix/json?unit=imperial&origins={lat},{long}' \
                   f'&destinations={destination_str}&key={api_key}'
    distance_responses = requests.get(distance_url).json()
    store_addresses = distance_responses['destination_addresses']
    store_distances = list(map(lambda distance_response: distance_response['distance']['text'],
                               distance_responses['rows'][0]['elements']))

    return [store_addresses, store_distances]
