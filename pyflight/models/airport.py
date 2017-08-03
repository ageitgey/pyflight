"""
Defines the Airport class
which is used to represent
an Airport with its code,
city code, and name.
"""


class Airport(object):
    """
    Contains Data of an Airport and its City Code.

    This Class supports various *magic methods*:

    ``x == y``
        Compare two Airports with each other
        for equality by their Airport and City Codes.

    ``x != y``
        Compare two Airports with each other for inequality.

    ``str(x)``
        Get the Airport's Name

        >>> str(my_airport)
        'ABC International'


    Attributes
    ----------
        code : str
            The Code of this Airport

        name : str
            The Name of this Airport

        city : str
            The Code of the City associated with the Airport
    """

    def __init__(self, airport: dict):
        """Create an Airport Object containing Data
        about an Airport and its associated City.

        An Airport Object which contains Data about
        each Flight returned from the API.

        Arguments
        ---------
            airport : dict
                A single Airport returned by the API
        """
        self.code = airport['code']
        self.name = airport['name']
        self.city = airport['city']

    def __eq__(self, other):
        """Compare two Airports with each other by their Airport and City Codes.

        Arguments
        ---------
            other : Airport
                The other Airport to compare this one to

        Returns
        -------
        bool
            ``True`` or ``False` depending on the Result of the Comparison
        """

        return self.__dict__ == other.__dict__

    def __str__(self):
        """Get this airport's name

        Returns
        -------
        str
            The name of this :class:`Airport`.
        """

        return self.name

    def as_dict(self):
        """Get a dictionary representation of the Airport.

        Example
        -------
            >>> airport = {
                'code': '3E7', 'city': 'XYZ', 'name': 'Example Airport'
            }
            >>> example_airport = Airport(airport)
            >>> example_airport.as_dict()
            {
                'code': '3E7',
                'city': 'XYZ',
                'name': 'Example Airport',
            }

        Returns
        -------
        dict
            A dictionary representing this Airport.
        """

        return self.__dict__
