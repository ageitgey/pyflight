"""
Contains the base class FlightData
and its subclasses Aircraft, City,
Carrier, and Tax, used to represent
simple information about the given
type as returned from the API.
"""


class FlightData(object):
    """Base Class for simple Flight Data with a Code / ID and name.

    This Class supports various *magic methods*:

    ``x == y``
        Compare two FlightData objects with each other for equality.

        >>> first_data = FlightData('9B1', 'Some Data')
        >>> second_data = FlightData('7B3', 'More Data')
        >>> first_data == second_data
        False

    ``x != y``
        Compare two FlightData objects with each other for inequality.

        >>> first_data != second_data
        True

    ``str(x)``
        Get the Name of this FlightData.

        >>> my_data = FlightData('3E7', 'Example Data')
        >>> str(my_data)
        'Example Data'


    Attributes
    ----------
        code : str
            A Code given to the FlightData Object as given from the API.
        name : str
            A name specifying the Name associated with the Code

    """

    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    def __eq__(self, other):
        """Compare two FlightData Objects with each other for equality or inequality.

        Arguments
        ---------
            other : FlightData
                The Object to compare this one with

        Example
        -------
            >>> first_data = FlightData('9B1', 'Some Data')
            >>> second_data = FlightData('7B3', 'More Data')
            >>> first_data == second_data
            False

        Returns
        -------
        bool
            ``True`` or ``False``, depending on the Result of the Comparison
        """

        return self.code == other.code and self.name == other.name

    def __str__(self):
        """Get the Name of this FlightData Object.

        Example
        -------
            >>> my_data = FlightData('3E7', 'Example Data')
            >>> str(my_data)
            'Example Data'

        Returns
        -------
        str
            the Name of the FlightData Object
        """

        return self.name

    def as_dict(self):
        """Get this FlightData Object as a Dictionary.

        Example
        -------
            >>> my_data = Tax('B31', 'Example FlightData')
            >>> my_data.as_dict()
            {'code': 'B31', 'name': 'Example FlightData')

        Returns
        -------
        dict
            Contains the Attributes of this Object
        """

        return self.__dict__


class Aircraft(FlightData):
    """
    This Class inherits from :class:`FlightData` and thus,
    supports all operations that FlightData supports.
    This represents a Tax with a code (unique identifier) and a Name.
    This will also be reflected in the Pricing section of a Trip,
    but with more information such as the charge type, the country,
    and the price of the Tax. For Examples, view the "Examples" section
    for :class:`FlightData`.
    """


class Carrier(FlightData):
    """
    This Class inherits from :class:`FlightData` and thus,
    supports all operations that FlightData supports.
    This represents a Tax with a code (unique identifier) and a Name.
    This will also be reflected in the Pricing section of a Trip,
    but with more information such as the charge type, the country,
    and the price of the Tax. For Examples, view the "Examples" section
    for :class:`FlightData`.
    """


class City(FlightData):
    """
    This Class inherits from :class:`FlightData` and thus,
    supports all operations that FlightData supports.
    This represents a Tax with a code (unique identifier) and a Name.
    This will also be reflected in the Pricing section of a Trip,
    but with more information such as the charge type, the country,
    and the price of the Tax. For Examples, view the "Examples" section
    for :class:`FlightData`.
    """


class Tax(FlightData):
    """
    This Class inherits from :class:`FlightData` and thus,
    supports all operations that FlightData supports.
    This represents a Tax with a code (unique identifier) and a Name.
    This will also be reflected in the Pricing section of a Trip,
    but with more information such as the charge type, the country,
    and the price of the Tax. For Examples, view the "Examples" section
    for :class:`FlightData`.
    """
