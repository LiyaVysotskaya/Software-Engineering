import asyncio
import aiohttp

API_KEY = "9344d2b4-e07b-49fa-91bf-9c37cb3de776"
async def fetch_map(stadiums):
    points = "~".join([f"{coord},pm2rdl{index+1}" for index, (name, coord) in enumerate(stadiums.items())])
    center = "37.622504,55.753215"

    async with aiohttp.ClientSession() as session:
        async with session.get('https://static-maps.yandex.ru/v1', params={
            "apikey": API_KEY,
            "ll": center,
            "z": "11",
            "size": "650,450",
            "lang": "ru_RU",
            "pt": points
        }) as response:
            if response.status == 200:
                filename = "stadiums_map.png"
                with open(filename, 'wb') as file:
                    file.write(await response.read())
            else:
                raise Exception(f"Failed to fetch map: {response.status}")

async def main():
    stadiums_location = {
        "Лужники": "37.554191,55.715551",
        "Спартак": "37.440262,55.818015",
        "Динамо": "37.559809,55.791540"
    }
    await fetch_map(stadiums_location)

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = None

if loop and loop.is_running():
    loop.create_task(main())
else:
    asyncio.run(main())

