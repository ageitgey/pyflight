"""
Contains the Flight class,
which is used to represent
a flight from takeoff to landing.
"""


class Flight(object):  # pylint: disable=too-many-instance-attributes
    r"""
    The smallest unit of travel, identifies a flight from takeoff to landing.

    In the API Response, this is found as
    ``trips.tripOption[].slice[].segment[].leg[]``

    This class supports various *magic methods*:

    ``x == y``
        Compare two :class:`Flight`\s with each other for equality.

    ``x != y``
        Compare two :class:`Flight`\s with each other for inequality.

    ``str(x)``
        Get the :class:`Flight`'s ``id`` as a String.


    Attributes
    ----------
        id : str
            A unique identifier for this Flight Object
        aircraft : str
            The aircraft travelling between the two points of this Flight
        departure_time : str
            The Time of Departure local to the point of departure,
            with the Time Zone Difference included
        arrival_time : str
            The Time of Arrival local to the point of arrival
            with the Time Zone Difference included
        duration : int
            The scheduled Travelling Time between
            the the two Points, in minutes
        origin : str
            The Origin of this Flight as a City / Airport Code
        destination : str
            The Destination of this Flight as a City / Airport Code
        origin_terminal : str
            The scheduled Terminal from which this Flight should depart on.
            ``''`` (empty string) if not specified.
        destination_terminal : str
            The scheduled Terminal where this Flight should arrive at.
            ``''`` (empty string) if not specified.
        mileage : int
            The number of miles flown in this Flight
        meal : str
            A description of the meal(s) served on the flight
            ``''`` (empty string) if not specified.
        change_plane : bool
            Whether passengers have to change planes following this leg.
            Applies to the next leg, defaults to False.
        performance : int
            Specifies the published on time performance on this leg.
            ``None`` if not specified.
    """

    def __init__(self, leg_data: dict):
        """Create a new Flight Object

        Parameters
        ----------
            leg_data : dict
                The Leg Data given from the API to initialize this Object from
        """
        self.id = leg_data['id']  # pylint: disable=invalid-name
        self.aircraft = leg_data['aircraft']
        self.departure_time = leg_data['departureTime']
        self.arrival_time = leg_data['arrivalTime']
        self.duration = leg_data['duration']
        self.origin = leg_data['origin']
        self.destination = leg_data['destination']
        self.origin_terminal = leg_data.get('originTerminal', '')
        self.destination_terminal = leg_data.get('destinationTerminal', '')
        self.mileage = leg_data['mileage']
        self.meal = leg_data.get('meal', '')
        self.change_plane = leg_data.get('changePlane', '')
        self.performance = leg_data.get('onTimePerformance', None)

    def __eq__(self, other):
        """Compare two :class:`Flight`s with each other for equality.

        Parameters
        ----------
        other : :class:`Flight`
            The other :class:`Flight` to compare to.

        Returns
        -------
        bool
            ``True`` or ``False``, depending on the result of the comparison.
        """

        return self.id == other.id

    def __str__(self):
        """Get a string of the ID of this instance of :class:`Flight`"""

        return self.id

    def as_dict(self):
        """Get this object in the form of a dictionary.

        Returns
        -------
        dict
            A dictionary representing all attributes of this
            :class:`Flight` as Key / Value pairs.
        """

        return self.__dict__
