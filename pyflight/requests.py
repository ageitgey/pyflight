"""
Handles all Requests that are sent to the API.
"""
import asyncio

import aiohttp
import re
import requests
from typing import Optional

import pyflight.rate_limiter


MAX_PRICE_REGEX = re.compile('[A-Z]{3}\d+(\.\d+)?')


class APIException(Exception):
    """
    Custom Exception that is raised from the Requests when an API call goes wrong, meaning the API did not  
    return a status code of 200. 

    Examples
    --------
        
    .. code-block:: python
    
        try:
            flight_info = send_sync(my_request_body, use_containers=False)
        except pyflight.APIException as err:
            print('Error trying to execute a request:') 
            print(err)
        else:
            ...
            
    The Exception will be formatted as: `'<status-code>: <error-message> (reason)'`, for example
    `400: Bad Request (keyInvalid)`
    """


class Request:
    """Represents a Request that can be sent to the API instead of using a dictionary manually.
    
    Attributes
    ----------
    raw_data : dict
        The raw JSON / dictionary data which will be sent to the API.
        
    """
    def __init__(self):
        """Create a new Request."""
        self.raw_data = {
            'request': {
                'passengers': {},
                'slice': [],
                'solutions': 1
            }
        }

    @property
    def adult_count(self) -> int:
        return self.raw_data['request']['passengers'].get('adultCount', 0)

    @adult_count.setter
    def adult_count(self, count: int):
        self.raw_data['request']['passengers']['adultCount'] = count

    @property
    def children_count(self) -> int:
        return self.raw_data['request']['passengers'].get('childrenCount', 0)

    @children_count.setter
    def children_count(self, count: int):
        self.raw_data['request']['passengers']['childrenCount'] = count

    @property
    def infant_in_lap_count(self) -> int:
        return self.raw_data['request']['passengers'].get('infantInLapCount', 0)

    @infant_in_lap_count.setter
    def infant_in_lap_count(self, count: int):
        self.raw_data['request']['passengers']['infantInLapCount'] = count

    @property
    def infant_in_seat_count(self) -> int:
        return self.raw_data['request']['passengers'].get('infantInSeatCount', 0)

    @infant_in_seat_count.setter
    def infant_in_seat_count(self, count: int):
        self.raw_data['request']['passengers']['infantInSeatCount'] = count

    @property
    def senior_count(self) -> int:
        return self.raw_data['request']['passengers'].get('seniorCount', 0)

    @senior_count.setter
    def senior_count(self, count: int):
        self.raw_data['request']['passengers']['seniorCount'] = count

    @property
    def max_price(self) -> Optional[str]:
        return self.raw_data['request'].get('maxPrice', None)

    @max_price.setter
    def max_price(self, max_price: str):
        if not re.match(MAX_PRICE_REGEX, max_price):
            raise ValueError('max_price given (\'{}\') does not match ISO-4217 format'.format(max_price))
        self.raw_data['request']['maxPrice'] = max_price

    @property
    def sale_country(self) -> Optional[str]:
        return self.raw_data['request'].get('saleCountry', None)

    @sale_country.setter
    def sale_country(self, sale_country: str):
        self.raw_data['request']['saleCountry'] = sale_country

    @property
    def ticketing_country(self) -> Optional[str]:
        return self.raw_data['request'].get('ticketingCountry', None)

    @ticketing_country.setter
    def ticketing_country(self, country: str):
        self.raw_data['request']['ticketingCountry'] = country

    @property
    def refundable(self) -> Optional[bool]:
        return self.raw_data['request'].get('refundable', None)

    @refundable.setter
    def refundable(self, refundable: bool):
        self.raw_data['request']['refundable'] = refundable

    @property
    def solution_count(self):
        return self.raw_data['request']['solutions']

    @solution_count.setter
    def solution_count(self, count: int):
        self.raw_data['request']['solutions'] = count


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
                    reason = resp['error']['errors'][0]['reason']
                    raise APIException('{0["error"]["code"]}: {0["error"]["message"]} ({1})'.format(resp, reason))
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
            reason = resp['error']['errors'][0]['reason']
            raise APIException('{0["error"]["code"]}: {0["error"]["message"]} ({1})'.format(resp, reason))
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
