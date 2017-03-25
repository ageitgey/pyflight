"""
Handles all Requests that are sent to the API.
"""
import aiohttp
import asyncio

import pyflight.rate_limiter


class Requester:
    """
    Class to make requests that keeps a aiohttp.ClientSession alive for faster requests.
    """

    def __init__(self):
        """Initialization of the Requester. 
        Gets a dedicated Event Loop from asyncio to be used for making Requests along with a Client Session.
        None is assigned to Client Session here because it should be set within a coroutine.
        """
        self.loop = asyncio.get_event_loop()
        self.client_session = None
        self._request_url = 'https://www.googleapis.com/qpxExpress/v1/trips/search'

    def set_api_key(self, key: str):
        """Set an API Key to be used for making Calls to the API.
        
        Note that there is a free quota of 50 Calls per API Key.
        
        Arguments: 
            key : str
                The API Key you wish to use for making Calls to the API.
        """
        self._request_url += '?key=' + key

    async def set_client_session(self):
        """
        Set the Client Session of self which is used for making requests.
        """
        self.client_session = aiohttp.ClientSession()

    async def post_request(self, url: str, payload: dict):
        """Send a POST request to the specified URL with the given payload.
        
        Arguments
            url : str
                The URL to which the POST Request should be sent
            payload: dict
                The Payload to be sent along with the POST request
                
        Returns
            dict: The Response of the Website
        """
        await pyflight.rate_limiter.delay_request(self.loop)
        if self.client_session is None:
            await self.set_client_session()
        async with self.client_session.post(url, payload) as r:
            return await r.json()

    async def get_request(self, url: str):
        """Send a GET request to the specified URL with the given payload.

        Arguments
            url : str
                The URL to which the GET Request should be sent
                
        Returns
            dict: The Response of the Website
        """
        await pyflight.rate_limiter.delay_request(self.loop)
        if self.client_session is None:
            await self.set_client_session()
        async with self.client_session.get(url) as r:
            return await r.json()

    def close(self):
        """
        Closes the Client Session of this Object.
        """
        self.client_session.close()

_requester = Requester()


def get_request(url: str) -> dict:
    """Sends out a GET request in Background
    
    Arguments:
        url : str
            The URL to which the Request should be sent
            
    Returns:
        dict: The Response, as a dictionary
    """
    return _requester.loop.run_until_complete(_requester.get_request(url))


def post_request(url: str, payload=None):
    """Sends out a POST Request to the specified URL
    
    Arguments
        url : str
            The URL to which the Request should be sent
        payload : dict
            The Payload to be sent to the URL
            
    Returns:
        dict: The Response, as dictionary
    """
    if payload is None:
        payload = {}
    return _requester.loop.run_until_complete(_requester.post_request(url, payload))


pyflight.rate_limiter.set_queries_per_day(24 * 60)
while True:
    print(get_request('http://random.cat/meow'))

# _requester.close() !!!!!!!!
