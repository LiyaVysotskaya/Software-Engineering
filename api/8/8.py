import math
import requests

GEOCODER_API_KEY = "bd00890e-c1a8-44c4-84e7-23a7fa1ec216"

def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b

    radians_latitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_latitude)

    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    distance = math.sqrt(dx * dx + dy * dy)

    return distance

def get_coordinates(api_key, address):
    base_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": address,
        "format": "json",
        "apikey": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        geo_object = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        coords = geo_object['Point']['pos']
        lon, lat = map(float, coords.split())
        return lon, lat
    else:
        print(f"Ошибка геокодирования: {response.status_code}")
        return None

home_address = input("Введите адрес вашего дома: ")
university_address = input("Введите адрес УУНиТ: ")

home_coords = get_coordinates(GEOCODER_API_KEY, home_address)
university_coords = get_coordinates(GEOCODER_API_KEY, university_address)

if home_coords and university_coords:
    distance = lonlat_distance(home_coords, university_coords)
    print(f"Расстояние от дома до университета: {distance} метров")
