from flask import Flask, request
from cost import get_cost
from locations import get_locations, get_address_and_distances
from dotenv import load_dotenv
from busyness import get_busyness

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    load_dotenv()

    req_data = request.get_json()
    items = req_data['groceries']
    user_geo_coord = list(req_data['location'].values())

    store_infos = get_locations(user_geo_coord)
    if len(store_infos) == 0:
        return {'err': 'No stores within max distance'}

    store_infos = get_address_and_distances(store_infos, user_geo_coord)
    if len(store_infos) == 0:
        return {'err': 'No stores within max distance'}  # Removes stores at unnamed addresses
    store_infos = store_infos[:6]  # places cap on number of stores to find busyness of (API costs money)

    store_infos = get_busyness(store_infos)
    if len(store_infos) == 0:
        return {'err': 'Stores in the area have all closed down'}
    store_infos = store_infos[:4]   # places cap on number of stores to execute item_find functionality on

    # execute item_finder functionality

    cost_sorted_stores = get_cost(store_infos)
    return {'cost_sorted_stores': cost_sorted_stores}


if __name__ == '__main__':
    app.run()
