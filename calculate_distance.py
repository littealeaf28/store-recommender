import requests

def get_store_locations(longitude,latitude):
    API_KEY='AIzaSyBLS5HmpphdMz7sK7i8FDil-o64M-bn6es'
    radiusDist='20000'
    keyword='Walmart'
    searchType='department_store'
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={longitude},{latitude}&radius={radiusDist}&type={searchType}&keyword={keyword}&key={API_KEY}'
    stores = requests.get(url)
    return stores.json()