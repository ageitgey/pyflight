"""
Handles all Requests that are sent to the API.
"""
import asyncio

import aiohttp
import requests


class APIException(Exception):
    """
    Custom Exception that is raised from the Requests when an
    API call goes wrong, meaning the API did not

    return a status code of 200.

    Attributes
    ----------
    code : int
        The code of the Error that was returned
    message : str
        The error message as returned by the API
    reason : str
        The reason as specified by the API

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

    The Exception will be formatted as:
    `'<status-code>: <error-message> (reason)'`, for example
    ``400: Bad Request (keyInvalid)``
    """

    def __init__(self, code: int, message: str, reason: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = code
        self.message = message
        self.reason = reason

    def __str__(self):
        return '{}: {} ({})'.format(self.code, self.message, self.reason)


class Requester(object):
    """
    Class to execute requests with.
    """

    def __init__(self):
        """Initialization of the Requester.
        Gets a dedicated Event Loop from asyncio
        to be used for making Requests.
        """

        self.loop = asyncio.get_event_loop()
        self.api_key = None

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
        # pylint: disable=invalid-name

        async with aiohttp.ClientSession(loop=self.loop) as cs:
            async with cs.post(url + self.api_key, data=payload) as r:
                if r.status != 200:
                    resp = await r.json()
                    raise APIException(
                        code=r.status,
                        message=resp['error']['message'],
                        reason=resp['error']['errors'][0]['reason']
                    )

                return await r.json()

    def post_request_sync(self, url: str, payload: dict) -> dict:
        """Send a synchronous POST request to the specified URL with the given payload.

        Arguments
            url : str
                The URL to which the POST Request should be sent
            payload: dict
                The Payload to be sent along with the POST request

        Returns
            dict: The Response of the Website
        """
        # pylint: disable=invalid-name

        r = requests.post(url + self.api_key, json=payload)

        if r.status_code != 200:
            resp = r.json()
            raise APIException(
                code=r.status_code,
                message=resp['error']['message'],
                reason=resp['error']['errors'][0]['reason']
            )

        return r.json()


requester = Requester()  # pylint: disable=invalid-name
