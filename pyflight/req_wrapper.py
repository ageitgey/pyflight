"""
Wraps Requests in an easy-to-use Module.
"""
from pyflight.requests import Requester

# Whether the Results should be put into the provided Containers. Defaults to True
use_containers = True


def set_use_containers(use: bool):
    """Specify whether the API Response should be put into a Container.
    
    By default, pyflight will automatically put an API Response into the provided Containers for easy interaction.
    If you wish to suppress this behaviour, set use to False. 
    
    Args:
        use : bool
            Set it to False to directly return API Responses as JSON instead of
            packing them into the provided Containers.
    """
    global use_containers
    use_containers = use

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

async def get_req():
    return await _requester.post_request('http://random.cat/meow')

print(get_request('http://random.cat/meow'))