"""
Contains the Segment class
which is used to represent
one or more consecutive legs
on the same flight.
"""

from .flight import Flight


class Segment(object):  # pylint: disable=too-many-instance-attributes
    r"""A single Segment consisting of one or
    more consecutive legs on the same flight.

    As an example, a Flight could have a stop between the
    origin and destination, resulting in two Segments
    instead of one. This contains information about
    one Single Segment's duration - for example, a flight
    from DFW to HNL, as well as other information about
    the Flight that this Segment describes.

    In the Response, this is represented as
    ``trips.tripOption[].slice[].segment[]``

    This class supports various *magic methods*:

    ``x == y``
        Compares two :class:`Segment`\s for equality.

    ``x != y``
        Compares two :class:`Segment`\s for inequality.

    ``str(x)``
        Get the ID of this :class:`Segment` object.

    Attributes
    ----------
        id : str
            The unique ID identifying this Segment.
        duration : int
            The duration of this Flight Segment, in Minutes
        cabin : str
            The cabin booked for this segment
        booking_code : str
            The booking code or booking class for this Segment
        booking_code_count : int
            The Number of seats available in
            this Segment with this Booking Code
        flight_carrier : str
            A two-letter IATA airline designator for this Segment
        flight_number : str
            The flight number of this Segment
        married_segment_group : str
            The Index of a Segment in a married Segment Group
        flights : List[:class:`Flight`]
            The flights from takeoff to landing for this Segment.
    """

    def __init__(self, segment: dict):
        """Create a new Segment Object.

        Parameters
        ----------
            segment : dict
                The dictionary to construct this Segment from.
        """
        self.id = segment['id']  # pylint: disable=invalid-name
        self.duration = segment['duration']
        self.cabin = segment['cabin']
        self.booking_code = segment['bookingCode']
        self.booking_code_count = segment['bookingCodeCount']
        self.flight_carrier = segment['flight']['carrier']
        self.flight_number = segment['flight']['number']
        self.married_segment_group = segment['marriedSegmentGroup']

        self.flights = [Flight(f) for f in segment['leg']]

    def __eq__(self, other):
        """Compare one :class:`Segment` object to another."""

        return self.id == other.id

    def __str__(self):
        """Get the ID of this :class:`Segment` object."""

        return self.id

    def find_one(self, condition_function):
        r"""Find a Flight out of the List of Flights in this
        :class:`Flight`\s that matches the passed function.
        This will return the first :class:`Flight` for which
        ``condition_function`` returns ``True``.
        For example, finding the first matching flight by its Carrier: ::

            flight = some_flight.find_one(lambda f: f.flight_carrier == 'AB')

        Parameters
        ---------
        condition_function : function
            A function that returns a ``bool`` as a result of,
            for example, a comparison.

        Returns
        -------
        :class:`Flight`
            If the search was successful and a :class:`Flight` was found
        None
            If no element has been found
        """

        for flight in self.flights:
            if condition_function(flight):
                return flight

        return None

    def find(self, condition_function: callable):
        r"""Similar to :meth:`find_one`\, except that it returns
        a generator of :class:`Flight`\s matching the condition
        in the passed function instead of a single :class:`Flight`
        or ``None``. This returns all :class:`Flight`\s for
        which ``condition_function`` returns True.

        For example, finding all flights with a duration above 60 minutes:

            flights = some_flight.find(lambda f: f.duration > 60)


        Examples
        --------
        Using the Generator to iterate over the results:

        .. code-block:: python

           for flight in some_flight.find(lambda f: f.duration > 60):
               print(flight.id)

        Saving the results to a list:

        .. code-block:: python

           found_flights = [
               f for f in some_flight.find(lambda f: f.duration > 60)
           ]


        Parameters
        ---------
        condition_function : function
            A function that returns a ``bool`` as a result of,
            for example, a comparison.

        Returns
        -------
        Generator[:class:`Flight`]
            A generator over which you can iterate easily, or
            construct a list from it. See examples.
        """

        return (f for f in self.flights if condition_function(f))

    def as_dict(self):
        """Get a dictionary representing the contents of this :class:`Segment`.

        Returns
        -------
        dict
            A dictionary containing the Data of this :class:`Flight` object.
        """

        return {
            'id': self.id,
            'duration': self.duration,
            'cabin': self.cabin,
            'booking_code': self.booking_code,
            'booking_code_count': self.booking_code_count,
            'flight_carrier': self.flight_carrier,
            'flight_number': self.flight_number,
            'married_segment_group': self.married_segment_group,
            'flights': [x.as_dict() for x in self.flights]
        }
