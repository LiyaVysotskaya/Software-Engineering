import asyncio
import aiohttp
import math
from PIL import Image, ImageDraw, ImageFont
import io

API_KEY = "9344d2b4-e07b-49fa-91bf-9c37cb3de776"

async def calculate_route_length(points):
    length = 0
    for i in range(len(points) - 1):
        start, end = points[i], points[i + 1]
        length += await calculate_point_distance(start, end)
    return length

async def calculate_point_distance(start, end):
    lat1, lon1 = start
    lat2, lon2 = end
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return 6371 * c

async def plot_route(api_key, points):
    if len(points) < 2:
        raise ValueError("Not enough points to plot the route")

    url = 'https://static-maps.yandex.ru/v1'
    points_str = ",".join([f"{point[1]},{point[0]},pm2blm" for point in points])
    polyline_str = ",".join([f'{point[1]},{point[0]}' for point in points])
    bbox = "37.3194,55.4903~37.9457,55.9492"

    params = {
        "apikey": api_key,
        "l": "map",
        "pt": points_str,
        "pl": polyline_str,
        "size": "650,450",
        "bbox": bbox,
        "lang": "ru_RU"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            image_data = await response.read()

            image = Image.open(io.BytesIO(image_data))
            draw = ImageDraw.Draw(image)

            route_length = await calculate_route_length(points)
            route_length_text = f"Route length: {route_length:.2f} km"
            text_position = (10, image.height - 30)
            font = ImageFont.truetype("Roboto-Regular.ttf", 16)
            draw.text(text_position, route_length_text, fill=(0, 0, 0), font=font)

            image.save("route_map_with_text.png")

async def main():
    points = [(55.715551, 37.554191), (55.818015, 37.440262), (55.791540, 37.559809)]
    await plot_route(API_KEY, points)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.is_running():
        asyncio.ensure_future(main())
    else:
        asyncio.run(main())

