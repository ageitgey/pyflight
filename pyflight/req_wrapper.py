"""
Provides an easy-to-use interface to use pyflight with.
"""
from typing import Union
from pyflight.requests import requester
from pyflight.results import Result

BASE_URL = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='
api_key = ''


def set_api_key(key: str):
    """Set the API key to use with the API. Note that there is a free quota of 50 calls per day. 
    Args:
        key : str
            The API key to make requests with.

    """
    global api_key
    api_key = key


async def send_async(request_body: dict, use_containers: bool=True) -> Union[dict, Result]:
    """Asynchronously execute and send the Request. This is a coroutine - calling this function must be awaited.
    
    It is also possible to specify whether the results of an API call should be returned as a Result or directly 
    from the API, as a dictionary, without any modifications. By default, pyflight will use the supplied containers.
    Pass False as a second argument to suppress this behaviour.
    
    Args:
        request_body : dict
            The body of the request to be sent to the API. This must follow the structure described here:
            https://developers.google.com/qpx-express/v1/trips/search
        use_containers : bool
            Whether the containers given should be used or not.
            If False is given, any API call will return a dictionary of the "raw" API data without any
            modification. Otherwise, an API call will return a pyflight.Result object or an Error if appropriate.
            
    References:
        https://developers.google.com/qpx-express/v1/trips/search
        
    Returns:
        If use_containers is True, a pyflight.Result object.
        Otherwise, the response as a dictionary.

    """
    response = await requester.post_request(BASE_URL + api_key, request_body)
    if use_containers:
        return Result(response)
    return response


def send_sync(request_body: dict, use_containers: bool=True) -> Union[dict, Result]:
    """Synchronously execute and send the Request. Note that this function is blocking.
    
    It is possible to specify whether the results of an API call should be returned as a Result or directly 
    from the API, as a dictionary, without any modifications. By default, pyflight will use the supplied containers.
    Pass False as a second argument to suppress this behaviour.
    
    Args:
        request_body : dict
            The body of the request to be sent to the API. This must follow the structure described here:
            https://developers.google.com/qpx-express/v1/trips/search
        use_containers : bool
            Whether the containers given should be used or not.
            If False is given, any API call will return a dictionary of the "raw" API data without any
            modification. Otherwise, an API call will return a pyflight.Result object or an Error if appropriate.
            
    References:
        https://developers.google.com/qpx-express/v1/trips/search
        
    Returns:
        If use_containers is True, a pyflight.Result object.
        Otherwise, the response as a dictionary.

    """
    response = requester.post_request_sync(BASE_URL + api_key, request_body)
    if use_containers:
        return Result(response)
    return response
