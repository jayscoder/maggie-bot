import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def download_urls(url):
    for i in range(3):
        content = await fetch(url)
        url = yield content

async def main():
    urls = [
        'https://www.example.com',
        'https://www.baidu.com',
        'https://www.yahoo.com'
    ]
    a = download_urls(urls[0])
    print(a.asend(urls[1]))
    print(a.asend(urls[2]))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
