"""
Provides an easy-to-use interface to use pyflight with.
"""
from pyflight.api import requester, Request
from pyflight.results import Result

from typing import Union

BASE_URL = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='
__api_key = ''


class Request:
    """Represents a Request that can be sent to the API instead of using a dictionary manually.

    Optional attributes default to ``None``.

    Attributes
    ----------
    raw_data : dict
        The raw JSON / dictionary data which will be sent to the API.
    adult_count : int
        The amount of passengers that are adults.
    children_count : int
        The amount of passengers that are children.
    infant_in_lap_count : int
        The amount of passengers that are infants travelling in the lap of an adult.
    infant_in_seat_count : int
        The amount of passengers that are infants assigned a seat.
    senior_count : int
        The amount of passengers that are senior citizens.
    max_price : Optional[str]
         The maximum price below which results should be returned. The currency is specified in ISO-4217, and setting
         this attribute is validated using the regex ``[A-Z]{3}\d+(\.\d+)?``. If it does not match, a
         :class:`ValueError` is raised.
    sale_country : Optional[str]
        The IATA country code representing the point of sale. Determines the currency.
    ticketing_country : Optional[str]
        The IATA country code representing the point of ticketing, for example ``DE``.
    refundable : Optional[bool]
        Whether to return only results with refundable fares or not.
    solution_count : int
        The amount of solutions to return. Defaults to 1, maximum is 500. Raises a :class:`ValueError` when trying to
        assign a value outside 1 to 500.


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
        if not 1 < count < 500:
            raise ValueError('solution_count must be 1-500')
        self.raw_data['request']['solutions'] = count

def set_api_key(key: str):
    """Set the API key to use with the API.  
    
    Parameters
    ----------
        key : str
            The API key to make requests with.

    """
    global __api_key
    __api_key = key


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
        response = await requester.post_request(BASE_URL + __api_key, request_body)
    elif isinstance(request_body, Request):
        response = await requester.post_request(BASE_URL + __api_key, request_body.raw_data)
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
        response = requester.post_request_sync(BASE_URL + __api_key, request_body)
    elif isinstance(request_body, Request):
        response = requester.post_request_sync(BASE_URL + __api_key, request_body.raw_data)
    else:
        raise ValueError('Unsupported Request Type')
    if use_containers:
        return Result(response)
    return response
