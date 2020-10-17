from flask import Flask
from locations import get_locations, get_address_and_distances
from dotenv import load_dotenv
from traffic import get_busyness

app = Flask(__name__)


@app.route('/')
def main():
    load_dotenv()

    user_geo_coord = ['30.386163', '-82.288778']    # lat, long
    try:
        store_infos = get_locations(user_geo_coord)
    except Exception as ex:
        return str(ex)

    store_infos = get_address_and_distances(store_infos, user_geo_coord)

    store_infos = get_busyness(store_infos)

    # execute cost function

    return 'Hello'


if __name__ == '__main__':
    app.run()

