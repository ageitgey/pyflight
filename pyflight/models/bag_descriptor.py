"""
Contains the BagDescriptor
class which is used to re-
present a type of bag.
"""


class BagDescriptor(object):
    r"""A representation of a type of bag.

    This class supports various *magic methods*:

    ``x == y``
        Compare two :class:`BagDescriptor`\s for equality.
        Works by comparing their attributes, so it returns ``True``
        when ``x.__dict__ == y.__dict__``.

    ``x != y``
        Compare two :class:`BagDescriptor`\s for inequality.
        Works by comparing their attributes, so it returns
        ``True`` when ``x.__dict__ != y.__dict``.

    ``str(x)``
        Returns the ``commercial_name`` of a :class:`BagDescriptor`.

    Attributes
    ----------
        commercial_name : str
            The commercial name for this :class:`BagDescriptor`
            for an optional service, can also be an empty string.
        count : int
            How many of this type of bag will be checked on this flight.
        description : List[str]
            A list of strings describing the baggage. Can be an empty list.
        subcode : str
            An IATA subcode used to identify the optional service
        max_kilos : int
            Specifies the maximum number of kilos that all
            the free baggage together may weigh.
            ``None`` if not specified.
        kilos_per_piece : int
            Specifies the maximum number of kilos that
            any piece of baggage may weigh.
            ``None`` if not specified.
        pounds : int
            The number of pounds of free baggage allowed.
            ``None`` if not specified.

    Notes
    -----
        A single :class:`FreeBaggageOption` contains multiple BagDescriptors.
    """

    def __init__(self, bag_descriptor_data: dict):
        """Create a new BagDescriptor object.

        Parameters
        ----------
            bag_descriptor_data : dict
                The Bag Descriptor data as a dictionary,
                returned from the API in Arrays.
        """
        self.commercial_name = bag_descriptor_data.get('commercialName', '')
        self.count = bag_descriptor_data['count']
        self.description = bag_descriptor_data.get('description', [])
        self.subcode = bag_descriptor_data['subcode']
        self.max_kilos = bag_descriptor_data.get('kilos')
        self.kilos_per_piece = bag_descriptor_data.get('kilosPerPiece')
        self.pounds = bag_descriptor_data.get('pounds')

    def __str__(self):
        """Get the ``commercial_name`` of this :class:`BagDescriptor`.

        Returns
        -------
        str
            The ``commercial_name`` of this :class:`BagDescriptor`.
        """

        return self.commercial_name

    def __eq__(self, other):
        """Compare two :class:`BagDescriptor` objects
        with each other for equality by their attributes.

        Returns
        -------
        bool
            True or False, depending on the result of the comparison.
        """

        return self.__dict__ == other.__dict__

    def as_dict(self):
        """Get a dictionary representing the attributes of this :class:`BagDescriptor`

        Returns
        -------
        dict
            A dictionary with key / value pairs containing
            the attributes of this :class:`BagDescriptor`.
        """

        return self.__dict__
