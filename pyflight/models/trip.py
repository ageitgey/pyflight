"""
Contains the Trip class,
which contains information
about a single trip - which
is an itinerary solution -
as returned by the API.
"""

from .route import Route
from .pricing import Pricing


class Trip(object):
    r"""Contains Information about one Trip - an itinerary solution - from the API.

    This class supports various *magic methods*:

    ``x == y``
        Compares two :class:`Trip`\s with each other for equality.
        Returns ``True`` when ``x.id == y.id``.

    ``x != y``
        Compares two :class:`Trip`\s with each other for inequality.
        Returns ``True`` when ``x.id != y.id``.

    ``str(x)``
        Returns the ``id`` of the :class:`Trip` this is invoked on.

    Attributes
    ----------
        total_price : str
            The total price as Currency followed by the
            Amount for all Passengers on the Trip, e.g. ``'USD59.00'``
        id : str
            The unique ID given to each Trip
        routes : List[:class:`Route`]
            A list of Routes from this Trip
        pricing : List[:class:`Pricing`]
            A list of pricing data from this Trip
    """

    def __init__(self, trip_data: dict):
        """Create a new Trip object.

        Parameters
        ----------
            trip_data : dict The tripOption dictionary returned by
                the API to create the Trip Object from.
        """
        self.total_price = trip_data['saleTotal']
        self.id = trip_data['id']  # pylint: disable=invalid-name

        self.routes = [Route(r) for r in trip_data['slice']]
        self.pricing = [Pricing(pd) for pd in trip_data['pricing']]

    def __eq__(self, other):
        """Compare two :class:`Trip` objects with each other for equality

        Returns
        -------
        bool
            True or False depending on the result of the comparison
        """

        return self.id == other.id

    def __str__(self):
        """Returns the ``id`` of this :class:`Trip`.

        Returns
        -------
        str
            The ``id`` of this :class:`Trip`
        """

        return self.id

    def as_dict(self) -> dict:
        """Get a dictionary representation of this :class:`Trip`.

        Returns
        -------
        dict
            A dictionary containing the attributes
            of this :class:`Trip` as key / value pairs.
        """

        return {
            'total_price': self.total_price,
            'id': self.id,
            'routes': [r.as_dict() for r in self.routes],
            'pricing': [p.as_dict() for p in self.pricing]
        }
