"""
Provides an easy-to-use interface to use pyflight with.
"""
import re
from typing import List, Optional, Union

from .api import requester
from .result import Result

BASE_URL = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key='
__API_KEY = ''
MAX_PRICE_REGEX = re.compile(r'[A-Z]{3}\d+(\.\d+)?')
ALLOWED_PREFERRED_CABINS = 'COACH', 'PREMIUM_COACH', 'BUSINESS', 'FIRST'


class Slice:
    """Represents a slice that makes up a single itinerary of this trip.

    For example, for one-way trips, usually one slice is used.
    A round trip would use two slices. (e.g. SFO - FRA - SFO)

    Optional attributes default to ``None`` or an empty list if applicable,
    but can be set if wanted.

    Attributes
    ----------
    raw_data : dict
        The raw JSON / dictionary data which will be sent to the API.
    origin : str
        The airport or city IATA designator of the origin.
    destination : str
        The airport or city IATA designator of the destination.
    date : str
        The date on which this flight should take place,
        in the format YYYY-MM-DD.
    max_stops : Optional[int]
        The maximum amount of stops that the passenger(s)
        are willing to accept on this slice.
    max_connection_duration : Optional[int]
        The longest duration (in minutes) between two legs
        that passengers are willing to accept
    preferred_cabin : Optional[str]
        The preferred cabin for this slice.
        Allowed values are COACH, PREMIUM_COACH, BUSINESS, and FIRST.
        A :class:`ValueError` is raised if a value is assigned that is
        not listed above.
    earliest_departure_time : Optional[str]
        The earliest time for departure, local to the point of departure.
        Formatted as HH:MM.
    latest_departure_time : Optional[str]
        The latest time for departure, local to the point of departure.
        Formatted as HH:MM.
    permitted_carriers : List[str]
        A list of 2-letter IATA airline designators for
        which results should be returned.
    prohibited_carriers : List[str]
        A list of 2-letter IATA airline designators,
        for which no results will be returned.
    """

    def __init__(self, origin: str, destination: str, date: str):
        """Create a new slice.

        Parameters
        ----------
        origin : str
            The airport or city IATA designator of the origin.
        destination : str
            The airport or city IATA designator of the destination.
        date : str
            The date on which this flight should take place,
            in the format YYYY-MM-DD.
        """

        self.raw_data = {
            'kind': 'qpxexpress#sliceInput',
            'origin': origin,
            'destination': destination,
            'date': date
        }

    @property
    def origin(self) -> str:
        """The airport or city IATA designator of the origin."""

        return self.raw_data['origin']

    @origin.setter
    def origin(self, new_origin: str):
        self.raw_data['origin'] = new_origin

    @property
    def destination(self) -> str:
        """The airport or city IATA designator of the destination."""

        return self.raw_data['destination']

    @destination.setter
    def destination(self, new_destination: str):
        self.raw_data['destination'] = new_destination

    @property
    def date(self) -> str:
        """
        The date on which this flight should take place,
        in the format YYYY-MM-DD.
        """

        return self.raw_data['date']

    @date.setter
    def date(self, new_date: str):
        self.raw_data['date'] = new_date

    @property
    def max_stops(self) -> Optional[int]:
        """
        The maximum amount of stops that the passenger(s)
        are willing to accept on this slice.
        """

        return self.raw_data.get('maxStops', None)

    @max_stops.setter
    def max_stops(self, max_stops: int):
        self.raw_data['max_stops'] = max_stops

    @property
    def max_connection_duration(self) -> Optional[int]:
        """
        The longest duration (in minutes) between two legs
        that passengers are willing to accept
        """

        return self.raw_data.get('maxConnectionDuration', None)

    @max_connection_duration.setter
    def max_connection_duration(self, new_max_duration: int):
        self.raw_data['maxConnectionDuration'] = new_max_duration

    @property
    def preferred_cabin(self) -> Optional[str]:
        """
        The preferred cabin for this slice.
        Allowed values are COACH, PREMIUM_COACH, BUSINESS, and FIRST.
        A :class:`ValueError` is raised if a value is assigned that is
        not listed above.
        """

        return self.raw_data.get('preferredCabin', None)

    @preferred_cabin.setter
    def preferred_cabin(self, new_preferred_cabin: str):
        if new_preferred_cabin not in ALLOWED_PREFERRED_CABINS:
            raise ValueError('Invalid value for preferred_cabin')
        self.raw_data['preferredCabin'] = new_preferred_cabin

    @property
    def _permitted_departure_time(self) -> dict:
        if 'permittedDepartureTime' not in self.raw_data:
            self.raw_data['permittedDepartureTime'] = {
                'kind': 'qpxexpress#timeOfDayRange'
            }

        return self.raw_data['permittedDepartureTime']

    @property
    def earliest_departure_time(self) -> Optional[str]:
        """
        The earliest time for departure, local to the point of departure.
        Formatted as HH:MM.
        """

        return self._permitted_departure_time.get('earliestTime', None)

    @earliest_departure_time.setter
    def earliest_departure_time(self, new_edt: str):
        self._permitted_departure_time['earliestTime'] = new_edt

    @property
    def latest_departure_time(self) -> Optional[str]:
        """
        The latest time for departure, local to the point of departure.
        Formatted as HH:MM.
        """

        return self._permitted_departure_time.get('latestTime', None)

    @latest_departure_time.setter
    def latest_departure_time(self, new_ldt: str):
        self._permitted_departure_time['latestTime'] = new_ldt

    @property
    def permitted_carriers(self) -> List[str]:
        """
        A list of 2-letter IATA airline designators for
        which results should be returned.
        """

        return self.raw_data.get('permittedCarrier', [])

    @permitted_carriers.setter
    def permitted_carriers(self, new_permitted_carriers: list):
        self.raw_data['permittedCarrier'] = new_permitted_carriers

    @property
    def prohibited_carriers(self) -> List[str]:
        """
        A list of 2-letter IATA airline designators,

        for which no results will be returned.
        """

        return self.raw_data.get('prohibitedCarrier', [])

    @prohibited_carriers.setter
    def prohibited_carriers(self, new_prohibited_carriers: list):
        self.raw_data['prohibitedCarrier'] = new_prohibited_carriers


class Request:
    r"""Represents a Request that can be sent to the API instead
    of using a dictionary manually.

    Please note that each Request requires at least
    1 adult or senior passenger.
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
        The amount of passengers that are infants
        travelling in the lap of an adult.
    infant_in_seat_count : int
        The amount of passengers that are infants assigned a seat.
    senior_count : int
        The amount of passengers that are senior citizens.
    max_price : Optional[str]
         The maximum price below which results should be returned.
         The currency is specified in ISO-4217, and setting
         this attribute is validated using the regex ``[A-Z]{3}\d+(\.\d+)?``.
         If it does not match, a :class:`ValueError` is raised.
    sale_country : Optional[str]
        The IATA country code representing the point of sale.
        Determines the currency.
    ticketing_country : Optional[str]
        The IATA country code representing the point of ticketing,
        for example ``DE``.
    refundable : Optional[bool]
        Whether to return only results with refundable fares or not.
    solution_count : int
        The amount of solutions to return. Defaults to 1, maximum is 500.
        Raises a :class:`ValueError` when trying to
        assign a value outside of 1 to 500.
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

    def add_slice(self, slice_: Slice):
        """Adds a slice to this Request.

        Parameters
        ----------
        slice_ : :class:`Slice`
            The Slice to be added to the request.

        Returns
        -------
        self
            To ease chaining of this function, ``self`` is returned.
        """

        self.raw_data['request']['slice'].append(slice_.raw_data)

        return self

    def as_dict(self) -> dict:
        """
        Returns the raw data associated with this request,
        which is sent to the API when calling send_sync or send_async.
        """

        return self.raw_data

    def send_sync(self, use_containers: bool = True) -> Union[Result, dict]:
        """Synchronously execute a request.

        Internally, this calls :meth:`pyflight.send_sync()`.
        You can also call the function directly.
        For further information, please view
        documentation for :meth:`pyflight.send_sync()`.
        """

        return send_sync(self, use_containers=use_containers)

    async def send_async(self, use_containers: bool = True) -> Union[Result, dict]:
        """Asynchronously execute a request.

        Internally, this calls :meth:`pyflight.send_async()`.
        You can also call the function directly. For further information,
        please view documentation for :meth:`pyflight.send_async()`.
        """

        return send_async(self, use_containers=use_containers)

    @property
    def adult_count(self) -> int:
        """The amount of passengers that are adults."""

        return self.raw_data['request']['passengers'].get('adultCount', 0)

    @adult_count.setter
    def adult_count(self, count: int):
        self.raw_data['request']['passengers']['adultCount'] = count

    @property
    def children_count(self) -> int:
        """The amount of passengers that are children."""

        return self.raw_data['request']['passengers'].get('childrenCount', 0)

    @children_count.setter
    def children_count(self, count: int):
        self.raw_data['request']['passengers']['childrenCount'] = count

    @property
    def infant_in_lap_count(self) -> int:
        """
        The amount of passengers that are infants
        travelling in the lap of an adult.
        """

        return self.raw_data['request']['passengers'].get('infantInLapCount', 0)

    @infant_in_lap_count.setter
    def infant_in_lap_count(self, count: int):
        self.raw_data['request']['passengers']['infantInLapCount'] = count

    @property
    def infant_in_seat_count(self) -> int:
        """The amount of passengers that are infants assigned a seat."""

        return self.raw_data['request']['passengers'].get(
            'infantInSeatCount', 0
        )

    @infant_in_seat_count.setter
    def infant_in_seat_count(self, count: int):
        self.raw_data['request']['passengers']['infantInSeatCount'] = count

    @property
    def senior_count(self) -> int:
        """The amount of passengers that are senior citizens."""

        return self.raw_data['request']['passengers'].get('seniorCount', 0)

    @senior_count.setter
    def senior_count(self, count: int):
        self.raw_data['request']['passengers']['seniorCount'] = count

    @property
    def max_price(self) -> Optional[str]:
        """
        The maximum price below which results should be returned,
        specified in ISO-421 format.
        """

        return self.raw_data['request'].get('maxPrice', None)

    @max_price.setter
    def max_price(self, max_price: str):
        if not re.match(MAX_PRICE_REGEX, max_price):
            err_msg = 'max_price given (\'{}\') does not match ISO-4217 format'
            raise ValueError(err_msg.format(max_price))
        self.raw_data['request']['maxPrice'] = max_price

    @property
    def sale_country(self) -> Optional[str]:
        """
        The IATA country code representing the point of sale.
        Determines the currency.
        """

        return self.raw_data['request'].get('saleCountry', None)

    @sale_country.setter
    def sale_country(self, sale_country: str):
        self.raw_data['request']['saleCountry'] = sale_country

    @property
    def ticketing_country(self) -> Optional[str]:
        """
        The IATA country code representing the point of ticketing,
        for example ``DE``.
        """

        return self.raw_data['request'].get('ticketingCountry', None)

    @ticketing_country.setter
    def ticketing_country(self, country: str):
        self.raw_data['request']['ticketingCountry'] = country

    @property
    def refundable(self) -> Optional[bool]:
        """Whether to return only results with refundable fares or not."""

        return self.raw_data['request'].get('refundable', None)

    @refundable.setter
    def refundable(self, refundable: bool):
        self.raw_data['request']['refundable'] = refundable

    @property
    def solution_count(self):
        """The amount of solutions to return. Defaults to 1."""

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
            The API key to execute requests with.
    """

    requester.api_key = key


async def send_async(request_body: Union[dict, Request], use_containers: bool = True):
    """Asynchronously execute and send a JSON Request or a :class:`Request`.
     This is a coroutine - calling this function must be awaited.

    Parameters
    ----------
    request_body : Union[dict, Request]
        The body of the request to be sent to the API.
        This must follow the structure described here:
        https://developers.google.com/qpx-express/v1/trips/search
        It is heavily recommended to use :class:`Request` instead
        of constructing request bodies manually.
    use_containers : Optional[bool]
        Whether the containers given should be used or not.
        If False is given, any API call will return a dictionary
        of the "raw" API data without any modification. Otherwise, an
        API call will return a :class:`Result` object.

    Raises
    ------
    :class:`APIException`
            If the API call did not return the normal `200`
            status code and thus, an error occurred.

    Returns
    -------
    :class:`Result`
        If ``use_containers`` is ``True`` and no Error occurred.
    dict
        If ``use_containers`` is ``False``,
        as a raw dictionary without any adjustments.

    """

    if isinstance(request_body, dict):
        response = await requester.post_request(BASE_URL, request_body)
    elif isinstance(request_body, Request):
        response = await requester.post_request(
            BASE_URL, request_body.raw_data
        )
    else:
        raise ValueError('Unsupported Request Type')

    if use_containers:
        return Result(response)

    return response


def send_sync(request_body: Union[dict, Request], use_containers: bool = True):
    """Synchronously execute and send a JSON-Request or a :class:`Request.
    Note that this function is blocking.

    Parameters
    ----------
    request_body : Union[dict, Request]
        The body of the request to be sent to the API.
        This must follow the structure described here:
        https://developers.google.com/qpx-express/v1/trips/search
        It is heavily recommended to use :class:`Request` instead
        of constructing request bodies manually.
    use_containers : Optional[bool]
        Whether the containers given should be used or not.
        If False is given, any API call will return a dictionary
        of the "raw" API data without any modification. Otherwise,
        the API call will return a :class:`Result` object.

    Raises
    ------
    :class:`APIException`
            If the API call did not return the normal `200`
            status code and thus, an error occurred.

    Returns
    -------
    :class:`Result`
        If ``use_containers`` is ``True`` and no Error occurred.
    dict
        If ``use_containers`` is ``False`, as a
        raw dictionary without any adjustments.

    """

    if isinstance(request_body, dict):
        response = requester.post_request_sync(BASE_URL, request_body)
    elif isinstance(request_body, Request):
        response = requester.post_request_sync(BASE_URL, request_body.raw_data)
    else:
        raise ValueError('Unsupported Request Type')

    if use_containers:
        return Result(response)

    return response
