"""
Contains a FreeBaggageOption class
which is used to represent information
about the free baggage allowance for
one Segment.
"""

from .bag_descriptor import BagDescriptor


class FreeBaggageOption(object):
    """Contains Information about the free baggage allowance for one Segment.

    Attributes
    ----------
        pieces : int
            How many pieces of free baggage are allowed
        bag_descriptors : List[:class:`BagDescriptor`]
            A list of :class:`BagDescriptor` Objects used
            to represent different types of bags.
            Can be an empty list.

    Notes
    -----
        Information about this is saved in a :class:`SegmentPricing` class.
    """

    def __init__(self, baggage_data: dict):
        """Create a new FreeBaggageOption object.

        Parameters
        ----------
            baggage_data : dict
                The Baggage Data as returned from the API in an Array.

        """
        self.pieces = baggage_data['pieces']
        self.bag_descriptors = [
            BagDescriptor(bd) for bd in baggage_data.get('bagDescriptor', [])
        ]

    def as_dict(self):
        """Return a dictionary representation of this :class:`FreeBaggageOption`.

        Returns
        -------
        dict
            A dictionary with key / value pairs containing
            the attributes of this :class:`FreeBaggageOption`.
        """

        return {
            'pieces': self.pieces,
            'bag_descriptors': [bd.as_dict() for bd in self.bag_descriptors]
        }
