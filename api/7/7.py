import asyncio
import aiohttp

GEOCODER_API_KEY = "bd00890e-c1a8-44c4-84e7-23a7fa1ec216"

async def get_district(api_key, address):
    async with aiohttp.ClientSession() as session:
        geocode_url = f"https://geocode-maps.yandex.ru/1.x/?geocode={address}&format=json&apikey={api_key}&kind=district"
        async with session.get(geocode_url) as response:
            data = await response.json()
            
            if response.status == 200:
                try:
                    district = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AdministrativeArea']['SubAdministrativeArea']['SubAdministrativeAreaName']
                    print(f"Район: {district}")
                except KeyError:
                    print("Не удалось определить район для указанного адреса.")
            else:
                print(f"Ошибка геокодирования: {response.status}")
                print(data)

address = input("Введите адрес: ")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.is_running():
        asyncio.ensure_future(get_district(GEOCODER_API_KEY, address))
    else:
        asyncio.run(get_district(GEOCODER_API_KEY, address))
