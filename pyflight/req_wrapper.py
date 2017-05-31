"""
Provides an easy-to-use interface to use pyflight with.
"""
from pyflight.requests import requester, Request
from pyflight.results import Result

from typing import Union

BASE_URL = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='
api_key = ''


def set_api_key(key: str):
    """Set the API key to use with the API.  
    
    Parameters
    ----------
        key : str
            The API key to make requests with.

    """
    global api_key
    api_key = key


async def send_async(request_body: Union[dict, Request], use_containers: bool=True):
    """Asynchronously execute and send a JSON Request or a :class:`Request`.
     This is a coroutine - calling this function must be awaited.
    
    Parameters
    ----------
    request_body : Union[dict, Request]
        The body of the request to be sent to the API. This must follow the structure described here:
        https://developers.google.com/qpx-express/v1/trips/search
    use_containers : Optional[bool]
        Whether the containers given should be used or not.
        If False is given, any API call will return a dictionary of the "raw" API data without any
        modification. Otherwise, an API call will return a :class:`Result` object or an Error if appropriate.
    
    Raises
    ------
    :class:`APIException`
            If the API call did not return the normal `200` status code and thus, an error occurred.
                    
    Returns
    -------
    :class:`Result`
        If ``use_containers`` is ``True`` and no Error occurred.
    dict
        If ``use_containers`` is ``False``, as a raw dictionary without any adjustments.

    """
    if isinstance(request_body, dict):
        response = await requester.post_request(BASE_URL + api_key, request_body)
    elif isinstance(request_body, Request):
        response = await requester.post_request(BASE_URL + api_key, request_body.raw_data)
    else:
        raise ValueError('Unsupported Request Type')
    if use_containers:
        return Result(response)
    return response


def send_sync(request_body: Union[dict, Request], use_containers: bool=True):
    """Synchronously execute and send a JSON-Request or a :class:`Request. Note that this function is blocking.
    
    Parameters
    ----------
    request_body : Union[dict, Request]
        The body of the request to be sent to the API. This must follow the structure described here:
        https://developers.google.com/qpx-express/v1/trips/search
    use_containers : Optional[bool]
        Whether the containers given should be used or not.
        If False is given, any API call will return a dictionary of the "raw" API data without any
        modification. Otherwise, an API call will return a :class:`Result` object or an Error if appropriate.
    
    Raises
    ------
    :class:`APIException`
            If the API call did not return the normal `200` status code and thus, an error occurred.
                    
    Returns
    -------
    :class:`Result`
        If ``use_containers`` is ``True`` and no Error occurred.
    dict
        If ``use_containers`` is ``False`, as a raw dictionary without any adjustments.

    """
    if isinstance(request_body, dict):
        response = requester.post_request_sync(BASE_URL + api_key, request_body)
    elif isinstance(request_body, Request):
        response = requester.post_request_sync(BASE_URL + api_key, request_body.raw_data)
    else:
        raise ValueError('Unsupported Request Type')
    if use_containers:
        return Result(response)
    return response
