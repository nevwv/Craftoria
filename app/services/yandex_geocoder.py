import requests

def validate_location(address, api_key):
    try:
        url = f"https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&format=json&geocode={address}"
        response = requests.get(url)
        data = response.json()
        return data['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'] > 0
    except Exception:
        return False