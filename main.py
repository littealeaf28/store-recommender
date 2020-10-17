from flask import Flask
from calculate_distance import get_store_locations

app = Flask(__name__)


@app.route('/')
def main():
    longit='30.386163'
    lat='-82.288778'
    return get_store_locations(longit,lat)


if __name__ == '__main__':
    app.run()