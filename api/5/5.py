import aiohttp
import asyncio

GEOCODER_API_KEY = "bd00890e-c1a8-44c4-84e7-23a7fa1ec216"
SEARCHER_API_KEY = "4e32e608-2fea-4dc0-b4cc-e732a5f618dd"

async def find_nearest_pharmacy(api_key_geocode, api_key_search, address):
    async with aiohttp.ClientSession() as session:
        geocode_url = f"https://geocode-maps.yandex.ru/1.x/?geocode={address}&format=json&apikey={api_key_geocode}"
        search_url = f"https://search-maps.yandex.ru/v1/?apikey={api_key_search}&text=аптека&type=biz&lang=ru_RU&results=1"
        
        async with session.get(geocode_url) as geocode_response:
            geocode_data = await geocode_response.json()
            
            if geocode_response.status == 200:
                location = geocode_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                lon, lat = location.split()
                
                search_params = {
                    "ll": f"{lon},{lat}",
                }
                async with session.get(search_url, params=search_params) as search_response:
                    search_data = await search_response.json()
                    
                    if search_response.status == 200:
                        pharmacy = search_data['features'][0]
                        pharmacy_name = pharmacy['properties']['CompanyMetaData']['name']
                        pharmacy_address = pharmacy['properties']['CompanyMetaData']['address']
                        print(f"Ближайшая аптека: {pharmacy_name}, адрес: {pharmacy_address}")
                    else:
                        print(f"Ошибка поиска аптеки: {search_response.status}")
                        print(search_data)
            else:
                print(f"Ошибка геокодирования: {geocode_response.status}")
                print(geocode_data)

address = input("Введите адрес: ")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.is_running():
        asyncio.ensure_future(find_nearest_pharmacy(GEOCODER_API_KEY, SEARCHER_API_KEY, address))
    else:
        asyncio.run(find_nearest_pharmacy(GEOCODER_API_KEY, SEARCHER_API_KEY, address))

