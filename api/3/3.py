import asyncio
import aiohttp
import io
from PIL import Image

async def download_satellite_image(latitude, longitude):
    instance_id = '54d9abec-8400-4559-955a-ce245d0ef562'
    url = f'https://services.sentinel-hub.com/ogc/wms/{instance_id}'
    bbox = f'{latitude-0.01},{longitude-0.01},{latitude+0.01},{longitude+0.01}'
    params = {
        'service': 'WMS',
        'request': 'GetMap',
        'layers': 'TRUE-COLOR-S2L2A',
        'width': '650',
        'height': '650',
        'format': 'image/png',
        'bbox': bbox,
        'time': '2021-09-28/2021-10-04',
        'transparent': 'true',
        'SHOWLOGO': 'false',
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            image_data = await response.read()
            image = Image.open(io.BytesIO(image_data))
            image.save('satellite_image.png')

latitude = 55.7522
longitude = 37.6156

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.is_running():
        asyncio.ensure_future(download_satellite_image(latitude, longitude))
    else:
        asyncio.run(download_satellite_image(latitude, longitude))

