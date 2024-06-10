import aiohttp
import asyncio

API_KEY = "bd00890e-c1a8-44c4-84e7-23a7fa1ec216"
async def get_city_coordinates(city, api_key):
    async with aiohttp.ClientSession() as session:
        url = "https://geocode-maps.yandex.ru/1.x/"
        params = {
            "geocode": city,
            "format": "json",
            "apikey": api_key
        }
        async with session.get(url, params=params) as response:
            data = await response.json()
            if response.status == 200:
                geo_object = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
                coordinates = geo_object['Point']['pos']
                longitude, latitude = map(float, coordinates.split())
                return latitude
            else:
                raise Exception(f"Geocoding error: {response.status}")

async def find_southernmost_city(api_key, cities):
    tasks = [get_city_coordinates(city.strip(), api_key) for city in cities]
    latitudes = await asyncio.gather(*tasks)

    southernmost_city = None
    min_latitude = float('inf')

    for city, latitude in zip(cities, latitudes):
        if latitude is not None and latitude < min_latitude:
            southernmost_city = city
            min_latitude = latitude

    if southernmost_city:
        print(f"Southernmost city: {southernmost_city}")
    else:
        print("Failed to determine the coordinates of cities.")

cities = input("Enter the list of cities separated by commas: ").split(',')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.is_running():
        asyncio.ensure_future(find_southernmost_city(API_KEY, cities))
    else:
        asyncio.run(find_southernmost_city(API_KEY, cities))

