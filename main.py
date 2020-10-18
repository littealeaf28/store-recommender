from flask import Flask, request
from cost import get_cost
from locations import get_locations, get_address_and_distances
from dotenv import load_dotenv
from busyness import get_busyness
from prices import get_availabilities_and_prices

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    load_dotenv()

    req_data = request.get_json()
    items = req_data['groceries']
    user_geo_coord = req_data['location']

    store_infos = get_locations(user_geo_coord)
    if len(store_infos) == 0:
        return {}

    store_infos = get_address_and_distances(store_infos, user_geo_coord)
    store_infos = store_infos[:6]
    if len(store_infos) == 0:
        return {}

    store_infos = get_busyness(store_infos)
    store_infos = store_infos[:4]
    if len(store_infos) == 0:
        return {}

    store_infos = get_availabilities_and_prices(store_infos, items)

    # execute cost function
    optimal_store = get_cost(store_infos)
    # print(optimal_store)
    return optimal_store


if __name__ == '__main__':
    app.run()

