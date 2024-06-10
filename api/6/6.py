import requests
import random
from PIL import Image
from io import BytesIO

STATIC_MAP_API_KEY = "9344d2b4-e07b-49fa-91bf-9c37cb3de776"
GEOCODER_API_KEY = "bd00890e-c1a8-44c4-84e7-23a7fa1ec216"

def get_city_image(static_map_api_key, geocoder_api_key, city, zoom=12):
    base_url = 'https://static-maps.yandex.ru/1.x/'
    l = random.choice(['map', 'sat'])

    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "geocode": city,
        "format": "json",
        "apikey": geocoder_api_key
    }
    response = requests.get(geocode_url, params=geocode_params)
    if response.status_code == 200:
        location = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        lon, lat = location.split()
        
        params = {
            "key": static_map_api_key,
            "ll": f"{lon},{lat}",
            "z": zoom,
            "l": l,
            "size": "600,400",
            "lang": "ru_RU"
        }

        map_response = requests.get(base_url, params=params)
        if map_response.status_code == 200:
            return Image.open(BytesIO(map_response.content))
        else:
            print(f"Ошибка получения карты города {city}: {map_response.status_code}")
            return None
    else:
        print(f"Ошибка геокодирования города {city}: {response.status_code}")
        return None

def guess_the_city(static_map_api_key, geocoder_api_key):
    cities = ["Нью-Йорк", "Лондон", "Париж", "Токио", "Сидней",
    "Берлин", "Дубай", "Рим", "Мумбаи", "Пекин",
    "Бангкок", "Стамбул", "Москва", "Мехико", "Сеул",
    "Лос-Анджелес", "Буэнос-Айрес", "Каир", "Торонто", "Лагос"]
    random.shuffle(cities)
    
    for city in cities:
        img = get_city_image(static_map_api_key, geocoder_api_key, city)
        if img:
            img.show()
            guess = input(f"Угадайте город: ")
            if guess.lower() == city.lower():
                print("Верно!")
            else:
                print(f"Неправильно, это был город {city}")

guess_the_city(STATIC_MAP_API_KEY, GEOCODER_API_KEY)
