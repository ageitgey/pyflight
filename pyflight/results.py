"""
These provide several Classes that contain the Results of a Request
to simplify accessing them, as well as offering several Methods
to work with the Data from the Result.

Some of the Documentation is extracted from the resource reference
from the API itself, for which a full documentation can be found here:
https://developers.google.com/qpx-express/v1/trips/search
"""

from .models.airport import Airport
from .models.flight_data import Aircraft, Carrier, City, Tax
from .models.trip import Trip


class Result(object):
    r"""Contains Results of an API Call.

    This Class supports various *magic methods*:

    ``x == y``
        Checks if two :class:`Result`\s are identical.
        This is equivalent to ``x.request_id == y.request_id``.

    ``x != y``
        Checks if two :class:`Result`\s are not identical to each other.
        This is equivalent to ``x.request_id != y.request_id``.

    ``str(x)``
        Returns the ``request_id`` for the :class:`Result` this is invoked on.

    ``for trip in x``
        This will call ``__iter__`` of :class:`Result` and return an iterator
        over the :class:`Trip`\s saved in this :class:`Result`.

    Attributes
    ----------
        request_id : str
            Specifies the Request ID, unique for each Request.

        airports : List[:class:`Airport`]
            Contains Data for the Flights found in the Response.

        aircraft : List[:class:`Aircraft`]
            Contains the Code and the Name of the
            Aircraft found in the Response.

        carriers : List[:class:`Carrier`]
            Contains the Code and the Name of the
            Carriers found in the Response.

        cities : List[:class:`City`]
            Contains the Code and the Name of the
            Cities found in the Response.

        taxes : List[:class:`Tax`]
            Contains the Code and the Name of the
            Taxes found in the Response.

        trips : List[:class:`Trip`]
            Contains information about trips (itinerary solutions)
            returned by the API. The Amount of Trips is determined
            by the amount of Solutions set in the Request.
    """

    def __init__(self, data: dict):
        """Create the Result Object from the Response of the API.

        Parameters
        ----------
            data: dict
                The Response of the API, as a dictionary
        """
        self.request_id = data['trips']['requestId']

        self.airports = [Airport(a) for a in data['trips']['data']['airport']]
        self.aircraft = [
            Aircraft(a['code'], a['name'])
            for a in data['trips']['data']['aircraft']
        ]
        self.carriers = [
            Carrier(c['code'], c['name'])
            for c in data['trips']['data']['carrier']
        ]
        self.cities = [
            City(c['code'], c['name']) for c in data['trips']['data']['city']
        ]
        self.taxes = [
            Tax(t['id'], t['name']) for t in data['trips']['data']['tax']
        ]
        self.trips = [Trip(t) for t in data['trips']['tripOption']]

    def __eq__(self, other):
        """Compare two :class:`Result` objects for equality.

        Returns
        -------
        bool
            True or False depending on the result of the comparison
        """

        return self.request_id == other.request_id

    def __str__(self):
        """Get the ID of this :class:`Request`.

        Returns
        -------
        str
            The ``request_id`` of the :class:`Request` this is invoked on.
        """

        return self.request_id

    def __iter__(self):
        """
        Returns a generator for the :class:`Trip`s
        saved in this :class:`Result`.
        """

        for trip in self.trips:
            yield trip

    def as_dict(self) -> dict:
        """Returns a dictionary representation of this :class:`Result`.

        Useful for serializing data to JSON.
        Internally, this calls ``as_dict()`` on all of its members.

        Returns
        -------
        dict
            The data stored in this :class:`Result` as key / value pairs.
        """

        return {
            'request_id': self.request_id,
            'airports': [a.as_dict() for a in self.airports],
            'aircraft': [a.as_dict() for a in self.aircraft],
            'carriers': [c.as_dict() for c in self.carriers],
            'cities': [c.as_dict() for c in self.cities],
            'taxes': [t.as_dict() for t in self.taxes],
            'trips': [t.as_dict() for t in self.trips]
        }
