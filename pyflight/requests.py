import aiohttp
import asyncio
import json

print(aiohttp.__version__)

base_url = 'https://www.googleapis.com/qpxExpress/v1/trips/search'


class Requester:
    """
    Class to make requests that keeps a aiohttp.ClientSession alive for faster requests.
    """

    def __init__(self):
        """
        Initialization of the Requester. 
        Gets a dedicated Event Loop from asyncio to be used for making Requests along with a Client Session.
        None is assigned to Client Session here because it should be set within a coroutine.
        """
        self.loop = asyncio.get_event_loop()
        self.client_session = None

    async def set_client_session(self):
        """
        Set the Client Session of self which is used for making requests.
        """
        self.client_session = aiohttp.ClientSession()

    async def post_request(self, url: str, payload: dict={}):
        """
        Send a POST request to the specified URL with the given payload.
        
        :param url: The URL to which the POST Request should be sent
        :param payload: The Payload to be sent along with the POST request
        :return: The Response of the Website
        """
        if self.client_session is None:
            await self.set_client_session()
        async with self.client_session.post(url, payload) as r:
            return await r.json()

    async def get_request(self, url: str):
        """
        Send a GET request to the specified URL with the given payload.

        :param url: The URL to which the GET Request should be sent
        :return: The Response of the Website
        """
        if self.client_session is None:
            await self.set_client_session()
        async with self.client_session.get(url) as r:
            return await r.json()

_requester = Requester()


def make_request(url):
    """
    Sends out a request
    :param url: 
    :return: 
    """
    return _requester.loop.run_until_complete(_requester.post_request(url))

print(make_request('http://random.cat/meow'))

# _requester.client_session.close() !!!!!!!!
