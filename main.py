from flask import Flask
from locations import get_locations, get_address_and_distances
from dotenv import load_dotenv
from busyness import get_busyness
from cost import get_cost
from prices import get_availabilities_and_prices

app = Flask(__name__)


@app.route('/')
def main():
    load_dotenv()

    # item_str = 'milk,bread,detergent'
    # items = split(item_str, ', ')
    items = ['milk', 'bread', 'detergent']
    user_geo_coord = ['30.386163', '-82.288778']    # lat, long
    try:
        store_infos = get_locations(user_geo_coord)
    except Exception as ex:
        return str(ex)

    store_infos = get_address_and_distances(store_infos, user_geo_coord)

    store_infos = get_busyness(store_infos)

    # store_infos = get_availabilities_and_prices(store_infos, items)

    # print(store_infos)

    # execute cost function
    # optimal_store = get_cost(store_infos)
    return store_infos[0]


if __name__ == '__main__':
    app.run()

