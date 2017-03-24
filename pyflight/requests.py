import aiohttp
import asyncio
import async_timeout

print(aiohttp.__version__)

base_url = 'https://www.googleapis.com/qpxExpress/v1/trips/search'


class Requester:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.client_session = None

    async def set_client_session(self):
        self.client_session = aiohttp.ClientSession()

    async def send_request(self, url: str):
        if self.client_session is None:
            await self.set_client_session()
        async with self.client_session.get(url) as r:
            res = await r.json()
            print(res)

requester = Requester()


def make_request(url):
    requester.loop.run_until_complete(requester.send_request(url))

make_request('http://random.cat/meow')

# requester.client_session.close() !!!!!!!!
