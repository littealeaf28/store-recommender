from flask import Flask
from distance import get_store_locations, get_address_and_distances
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/')
def main():
    load_dotenv()

    user_geo_coord = ['30.386163', '-82.288778']    # lat, long
    try:
        # store_geo_coords, store_addresses = get_store_locations(user_geo_coord)
        store_geo_coords = get_store_locations(user_geo_coord)
    except Exception as ex:
        return str(ex)

    store_addresses, store_distances = get_address_and_distances(user_geo_coord, store_geo_coords)

    return 'Hello'


if __name__ == '__main__':
    app.run()

