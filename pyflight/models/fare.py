"""
Defines the Fare class which
represents the fare used to
price one or more segments.
"""


class Fare(object):
    """
    The fare used to price one or more segments.

    This Class supports various *magic methods*:

    ``x == y``
        Compare two :class:`Fare` objects with each other for equality.
        Returns ``True`` when ``x.id == y.id``.

    ``x != y``
        Compare two :class:`Fare` objects with each other for inequality.
        Returns ``True`` when ``x.id != y.id``.

    ``str(x)``
        Returns the ``id`` of this :class:`Fare` object.

    Attributes
    ----------
        id : str
            The unique identifier of the fare.
        carrier_code : str
            The Code for the Carrier whose fare this is.
        origin_city_code : str
            The origin city for this fare.
        destination_city_code : str
            The destination city for this fare.
        basis_code : str
            The Basis Code of this fare.
        private : bool
            Specifies whether this is a private fare
            offered only to select customers or not.
            Defaults to ``None``.
    """

    def __init__(self, fare_data: dict):
        """
        Create a new Fare Object.

        Parameters
        ----------
            fare_data : dict
                A Fare Object returned in from the API in arrays.
        """
        self.id = fare_data['id']  # pylint: disable=invalid-name
        self.carrier_code = fare_data['carrier']
        self.origin_city_code = fare_data['origin']
        self.destination_city_code = fare_data['destination']
        self.basis_code = fare_data['basisCode']
        self.private = fare_data.get('private', None)

    def __eq__(self, other):
        r"""Compare two :class:`Fare`\s for equality.

        Returns
        -------
        bool
            The result of the comparison
        """

        return self.id == other.id

    def __str__(self):
        """Get the ID of this :class:`Fare` object.

        Returns
        -------
        str
            The ``id`` of this :class:`Fare` object.
        """

        return self.id

    def as_dict(self):
        """Get a representation of this :class:`Fare` as a dictionary.

        Returns
        -------
        dict
            A dictionary containing the attributes of
            this :class:`Fare` as key / value pairs.
        """

        return self.__dict__
