"""
Contains the SegmentPricing class
which contains information about
price and baggage for segments.
"""

from .free_baggage_option import FreeBaggageOption


class SegmentPricing(object):
    r"""Price and baggage information for segments.

    This class supports various *magic methods*:

    ``x == y``
        Compares two :class:`SegmentPricing`\s for equality.
        Returns ``True`` if
        ``x.segment_id == y.segment_id and x.fare_id == y.fare_id``.

    ``x != y``
        Compares two :class:`SegmentPricing`\s for inequality.
        Returns ``True`` if ``not x == y``

    ``str(x)``
        Returns the ``segment_id`` of this :class:`SegmentPricing`.

    Attributes
    -----------
        segment_id : str
            A unique identifier for this :class:`SegmentPricing` object.
        fare_id : str
            The Fare ID for this :class:`SegmentPricing`.
            Used to refer to different parts of the same solution.
        free_baggage : List[:class:`FreeBaggageOption`]
            A list of :class:`FreeBaggageOption` objects
            for the free baggage allowance on this segment.

    """

    def __init__(self, segment_data: dict):
        """Create a new SegmentPricing object.

        Arguments:
            segment_data : dict
                The Data for a single SegmentPricing
                returned in Arrays from the API.

        """
        self.segment_id = segment_data['segmentId']
        self.fare_id = segment_data['fareId']
        self.free_baggage = [
            FreeBaggageOption(fbo)
            for fbo in segment_data.get('freeBaggageOption', [])
        ]

    def __eq__(self, other):
        """Compares two :class:`SegmentPricing` objects for equality.

        Returns
        -------
        bool
            True or False, depending on the result of the comparison.
        """

        return self.segment_id == other.segment_id \
            and self.fare_id == other.fare_id

    def __str__(self):
        """Returns the ``segment_id`` of this :class:`SegmentPricing`.

        Returns
        -------
        str
            The ``segment_id`` of this :class:`SegmentPricing`.
        """

        return self.segment_id

    def as_dict(self):
        """Return a dictionary representing this :class:`SegmentPricing`.

        Returns
        -------
        dict
            A dictionary containing the attributes of this
            :class:`SegmentPricing` as key / value pairs.
        """

        return {
            'segment_id': self.segment_id,
            'fare_id': self.fare_id,
            'free_baggage': [fbo.as_dict() for fbo in self.free_baggage]
        }
