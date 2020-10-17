from flask import Flask
from distance import get_store_locations
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/')
def main():
    load_dotenv()

    lat = '30.386163'
    long = '-82.288778'
    return get_store_locations(lat, long)


if __name__ == '__main__':
    app.run()

