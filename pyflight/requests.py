"""
Handles all Requests that are sent to the API.
"""
import asyncio

import aiohttp
import requests

import pyflight.rate_limiter


class APIException(Exception):
    """
    Custom Exception that is raised from the Requests when an API call goes wrong, meaning the API did not 
    return a status code of 200. 
    
    Examples:
        try:
            flight_info = send_sync(my_request_body, use_containers=False)
        except pyflight.APIException as err:
            print('Error trying to execute a request:') 
            print(err)
        else:
            ...
    """


class Requester(object):
    """
    Class to execute requests with.
    """

    def __init__(self):
        """Initialization of the Requester. 
        Gets a dedicated Event Loop from asyncio to be used for making Requests.
        """
        self.loop = asyncio.get_event_loop()

    async def post_request(self, url: str, payload: dict) -> dict:
        """Send a POST request to the specified URL with the given payload.
        
        Arguments
            url : str
                The URL to which the POST Request should be sent
            payload: dict
                The Payload to be sent along with the POST request
                
        Returns
            dict: The Response of the Website
        """
        await pyflight.rate_limiter.delay_async(self.loop)
        async with aiohttp.ClientSession(loop=self.loop) as cs:
            async with cs.post(url, data=payload) as r:
                if r.status != 200:
                    resp = r.json()
                    reason = resp["error"][0]["reason"]
                    raise APIException(f'{resp["error"]["code"]}: {resp["error"]["message"]} ({reason})')
                return await r.json()

    async def get_request(self, url: str) -> dict:
        """Send a GET request to the specified URL with the given payload.
        Arguments
            url : str
                The URL to which the GET Request should be sent
                
        Returns
            dict: The Response of the Website
        """
        await pyflight.rate_limiter.delay_async(self.loop)
        async with aiohttp.ClientSession(loop=self.loop) as cs:
            async with cs.get(url) as r:
                return await r.json()

    @staticmethod
    def post_request_sync(url: str, payload: dict) -> dict:
        """Send a synchronous POST request to the specified URL with the given payload.
        
        Arguments
            url : str
                The URL to which the POST Request should be sent
            payload: dict
                The Payload to be sent along with the POST request
                
        Returns
            dict: The Response of the Website
        """
        pyflight.rate_limiter.delay_sync()
        r = requests.post(url, json=payload)
        if r.status_code != 200:
            resp = r.json()
            reason = resp["error"][0]["reason"]
            raise APIException(f'{resp["error"]["code"]}: {resp["error"]["message"]} ({reason})')
        return r.json()

requester = Requester()


def get_request(url: str) -> dict:
    """Sends out a GET request in Background
    
    Arguments:
        url : str
            The URL to which the Request should be sent
            
    Returns:
        dict: The Response, as a dictionary
    """
    return requester.loop.run_until_complete(requester.get_request(url))


def post_request(url: str, payload=None) -> dict:
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
    return requester.loop.run_until_complete(requester.post_request(url, payload))
