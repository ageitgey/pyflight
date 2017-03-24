"""
Provides several Classes that contain the Results of a Request
to simplify accessing them.
"""


class Tax:
    """
    Contains Data about a Tax as given for different Flights.
    
    Attributes
    ----------
    id : str
        The ID of the Tax given by the API. Used for Comparisons.
    
    name : str
        The Name of the Tax.
        
    Methods
    -------
    as_dict()
        Get this Object as a Dictionary.
    """

    def __init__(self, tax_id: str, name: str):
        self.id = tax_id
        self.name = name

    def __eq__(self, other):
        """
        Compare two Taxes with each other for equality.
        
        >>> first_tax = Tax('9B1', 'Example Tax')
        >>> second_tax = Tax('7B3', 'Another Example Tax')
        >>> first_tax == second_tax
        False
        
        :param other: A Tax Object to compare
        :return: The Result of the comparison
        """
        return self.id == other.id

    def __len__(self):
        """
        Get the length of the Name of this Tax.
        
        >>> my_tax = Tax('7H6', 'Example Tax')
        >>> len(my_tax)
        11
        
        :return: The length of the name of this Tax 
        """
        return len(self.name)

    def __str__(self):
        """
        Get a String representation of the Tax this Object holds.
        
        >>> my_tax = Tax('3E7', 'Example Tax')
        >>> str(my_tax)
        '3E7: Example Tax'
        
        :return: A String containing the ID and the Name of the Tax.
        """
        return f'{self.id}: {self.name}'

    def as_dict(self):
        """
        Get this Tax as a Dictionary.
        
        >>> my_tax = Tax('B31', 'Example Tax')
        >>> my_tax.as_dict()
        {'id': 'B31', 'name': 'Example Tax')
        
        :return: A Dictionary containing the Attributes of this Object 
        """
        return {'id': self.id, 'name': self.name}


class Airport:
    """
    Contains Data of an Airport and its City
    
    Attributes
    ----------
    airport_code : str
    """

    def __init__(self, airport: dict, city: dict):
        """
        Create a Airport Object which contains Data about 
        each Flight returned from the API. It will match
        the Data for a structured Overview of each Flight.
        
        :param airport: A single Airports returned by the API
        :param city: A single Cities returned by the API
        """
        self.airport_code = airport['code']
        self.airport_name = airport['name']
        self.city_code = city['code']
        self.city_name = city['name']

    def __str__(self):
        """
        Get a representation of this Airport as a String.
        :return: 
        """


class Result:
    """
    Contains Results of an API Call.
    
    Attributes
    ----------
    request_id : int
        Specifies the Request ID, unique for each Request.
        
    airports : list of Airports
        Contains Data for the Flights found in the Response.
    """

    def __init__(self, data: dict):
        """
        Create the Result Object from the Response of the API.
        
        :param data: The Response of the API, as a dictionary 
        """
        self.request_id = data['trips']['requestId']

        # Save Flight Data
        self.airports = []

        airports = data['trips']['data']['airport']
        cities = data['trips']['data']['city']

        # Match Airport and City together
        for airport_data, city_data in zip(airports, cities):
            # Airport Code and City Code Match - create an Airport Object
            if airport_data['city'] == city_data['code']:
                self.airports.append(Airport(airport_data, city_data))
            else:
                # Search for the Airport matching the City Code
                for city in cities:
                    if city['code'] == airport_data['city']:
                        self.airports.append(Airport(airport_data, city))
                        break
                else:
                    print(f'Failed to find matching City for Airport: {airport_data}, Airport Data will be unmatched.')
                    self.airports.append(Airport(airport_data, city_data))

        # Save Taxes

