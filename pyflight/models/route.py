"""
Contains the Route class which
represents a traveller's intent
as well as a low-fare search
about an itinerary between two points.
"""

from .segment import Segment


class Route(object):
    r"""Represents the traveller's intent as well as a low-fare
    search about an itinerary between two points.

    In the Response, this is represented as ``trips.tripOption[].slice[]``

    This Class supports various *magic methods*:

    ``x == y``
        Compares two duration of two :class:`Route`\s
        with each other for equality.
        Returns ``True`` when ``x.duration == y.duration``.

    ``x != y``
        Compares two duration of two :class:`Route`\s
        with each other for inequality.
        Returns ``True`` when ``x.duration != y.duration``.

    ``x < y``
        Compare the ``duration`` of two :class:`Route`\s with each other.
        Returns ``True`` when ``x.duration < y.duration``.

    ``x <= y``
        Compare the ``duration`` of two :class:`Route`\s with each other.
        Returns ``True`` when ``x.duration <= y.duration``.

    ``x > y``
        Compare the ``duration`` of two :class:`Route`\s with each other.
        Returns ``True`` when ``x.duration > y.duration``.

    ``x >= y``
        Compare the ``duration`` of two :class:`Route`\s with each other.
        Returns ``True`` when ``x.duration >= y.duration``.

    Attributes
    ----------
        duration : int
            The duation of the :class:`Route`, in Minutes
        segments : List[:class:`Segment`]
            Segments consisting of one more consecutive
            legs on the same flight.
    """

    def __init__(self, route_slice: dict):
        """Create a new Route Object.

        Parameters
        ----------
            route_slice : dict
                The ``trips.tripsOption[].slice[]`` Object from the Response
        """
        self.duration = route_slice['duration']
        self.segments = [Segment(s) for s in route_slice['segment']]

    def __lt__(self, other):
        r"""Compare the duration of two :class:`Route`\s.

        Returns
        -------
        bool
            The result of the comparison, depending on the
            ``duration`` of two :class:`Route`\s."""

        return self.duration < other.duration

    def __le__(self, other):
        r"""Compare the duration of two :class:`Route`\s.

        Returns
        -------
        bool
            The result of the comparison, depending on the
            ``duration`` of two :class:`Route`\s."""

        return self.duration <= other.duration

    def __gt__(self, other):
        r"""Compare the duration of two :class:`Route`\s

        Returns
        -------
        bool
            The result of the comparison, depending on the
            ``duration`` of two :class:`Route`\s.
        """

        return self.duration > other.duration

    def __ge__(self, other):
        r"""Compare the duration of two :class:`Route`\s

        Returns
        -------
        bool
            The result of the comparison, depending on
            the ``duration`` of two :class:`Route`\s.
        """

        return self.duration >= other.duration

    def __eq__(self, other):
        r"""Compare the duration of two :class:`Route`\s with each other.

        Returns
        -------
        bool
            The result of the comparison, depending on the
            ``duration`` of two :class:`Route`s.
        """

        return self.duration == other.duration

    def as_dict(self):
        """Returns this :class:`Route` as a dictionary.

        Returns
        -------
        dict
            This :class:`Route` as a dictionary."""

        return {
            'duration': self.duration,
            'segments': [segment.as_dict() for segment in self.segments]
        }
