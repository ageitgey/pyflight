"""
Provides an easy-to-use interface to use pyflight with.
"""
from typing import Union
from pyflight.requests import requester
from pyflight.results import Result

api_key = ''


def set_api_key(key: str):
    """Set the API key to use with the API. Note that there is a free quota of 50 calls per day. 
    Args:
        key : str
            The API key to make requests with.

    """
    global api_key
    api_key = key


class Request(object):
    """Class to create, modify, and send requests.
    
    Attributes:
        request_body : dict
            A dictionary containing a request body that can be passed to the
            __init__ function to directly supply request data instead of setting
            it manually after initializing. If this is not supplied, defaults to {}.
            
    Methods:
        send_async : dict or Result
            Asynchronously execute and send a Request.
            By passing a boolean, it is possible to specify whether the containers supplied by the library
            should be used or if the response should be returned as a dictionary.
    """
    def __init__(self, request_body: dict=None, request_api_key: str=''):
        """Create a new Request. If no API Key is passed, then this must be called *after*
        an API key was set using `pyflight.set_api_key()`.
        
        Args:
            request_body : dict
                A request body in the structure that is shown here:
                https://developers.google.com/qpx-express/v1/trips/search
                If this is supplied, it is possible to directly send the request
                without supplying any more information. Additional information about
                the required properties can be found below the page.
            request_api_key : str
                The API key to be used for this request. If this is not given, it uses 
                the API key previously set using `pyflight.set_api_key()`.
                
        """
        global api_key
        if request_body is None:
            request_body = {}
        self.request_body = request_body
        self.url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='
        if request_api_key == '':
            self.url += api_key
        else:
            self.url += request_api_key

    async def send_async(self, use_containers: bool=True) -> Union[dict, Result]:
        """Asynchronously execute and send the Request.
        
        It is also possible to specify whether the results of an API call should be returned as a Result or directly 
        from the API, as a dictionary, without any modifications. By default, pyflight will use the supplied containers.
        Pass False as a second argument to suppress this behaviour.
        
        Args:
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
        if self.request_body != {}:
            response = await requester.post_request(self.url, self.request_body)
        else:
            # TODO: Add non-request-body requests
            return

        if use_containers:
            return Result(response)
        return response
