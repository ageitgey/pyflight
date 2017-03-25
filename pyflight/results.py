"""
Provides several Classes that contain the Results of a Request
to simplify accessing them.
"""


class FlightData:
    """Base Class for simple Flight Data with a Code / ID and name. 
    
    Attributes:
        code : str
            A Code given to the FlightData Object as given from the API.
        name : str
            A name specifying the Name associated with the Code
    
    Methods:
        __init__(code: str, name: str)
            Create a new FlightData Object with the given parameters. Used by calling
        __eq__ -> bool
            Compare two Flight Data Objects for Equality
        len(some_flight_data) -> int
            Get the length of the Name of this FlightData
        as_dict() -> dict
            Get a dictionary representing the contents of this Object
    """

    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    def __eq__(self, other) -> bool:
        """Compare two FlightData Objects with each other for equality or inequality.

        Arguments:
            other : FlightData
                The Object to compare this one with
                
        Example:
            >>> first_data = FlightData('9B1', 'Some Data')
            >>> second_data = FlightData('7B3', 'More Data')
            >>> first_data == second_data
            False
        
        Returns:
            bool: True or False, depending on the Result of the Comparison
        """
        return self.code == other.code and self.name == other.name

    def __len__(self) -> int:
        """Get the length of the Name of this FlightData.
        
        Example:
            >>> my_data = Tax('7H6', 'Example Data')
            >>> len(my_data)
            11
        
        Returns:
            int: The length of the name of this FlightData
        """
        return len(self.name)

    def __str__(self) -> str:
        """Get the Name of this FlightData Object.
        
        Example:
            >>> my_data = FlightData('3E7', 'Example Data')
            >>> str(my_data)
            'Example Data'
        
        Returns:
            str: the Name of the FlightData Object
        """
        return f'{self.name}'

    def as_dict(self) -> dict:
        """Get this FlightData Object as a Dictionary.

        Example:
            >>> my_data = Tax('B31', 'Example FlightData')
            >>> my_data.as_dict()
            {'id': 'B31', 'name': 'Example FlightData')
    
        Returns:
            dict: Contains the Attributes of this Object 
        """
        return {'id': self.code, 'name': self.name}


class Aircraft(FlightData):
    pass


class Tax(FlightData):
    pass


class Carrier(FlightData):
    pass


class Airport:
    """
    Contains Data of an Airport and its City
    
    Attributes:
        airport_code : str
            The Code of this Airport
            
        airport_name : str
            The Name of this Airport
        
        city_code : str
            The Code of the City associated with the Airport
            
        city_name : str
            The Name of the City associated with the Airport
        
    Methods:
        __init__(airport: dict, city: dict)
            Create a new Airport Object containing Data about an Airport and its associated City
        __eq__ -> bool
            Compare two Airports with each other by their Airport and City Codes
        __len__ -> int
            Get the length of the Airport Name
        __str__ -> str
            Get a string representing the Airport and City Name, e.g. "Example Airport in Example City"
        as_dict() -> dict
            Get a representation of this Airport as a Dictionary.
    """

    def __init__(self, airport: dict, city: dict):
        """Create an Airport Object containing Data about an Airport and its associated City.
        
        An Airport Object which contains Data about 
        each Flight returned from the API. It will match
        the Data for a structured Overview of each Flight.
        
        Arguments:
            airport : dict
                A single Airport returned by the API
            city : dict
                A single City returned by the API
        """
        self.airport_code = airport['code']
        self.airport_name = airport['name']
        self.city_code = city['code']
        self.city_name = city['name']

    def __eq__(self, other):
        """Compare two Airports with each other by their Airport and City Codes.
        
        Arguments
            other : Airport
                The other Airport to compare this one to
        
        Returns
            bool: True or False depending on the Result of the Comparison
        """
        return self.airport_code == other.airport_code and self.city_code == other.city_code

    def __len__(self) -> int:
        """Get the length of the Airport Name.
        
        Example
            >>> airport = {'code': '3E7', 'name': 'Example Airport'}
            >>> city = {'code': 'XYZ', 'name': 'Example City'}
            >>> example_airport = Airport(airport, city)
            >>> len(example_airport)
            15
        
        Returns
            int: The length of the Airport Name 
        """
        return len(self.airport_name)

    def __str__(self) -> str:
        """Get a representation of this Airport as a String.
        
        Example
            >>> airport = {'code': '3E7', 'name': 'Example Airport'}
            >>> city = {'code': 'XYZ', 'name': 'Example City'}
            >>> example_airport = Airport(airport, city)
            >>> str(example_airport)
            Example Airport in Example City
        
        Returns
            str: A representation of this Airport as a String.
        """
        return f'{self.airport_name} in {self.city_name}'

    def as_dict(self) -> dict:
        """Get a dictionary representation of the Airport.
        
        Example
            >>> airport = {'code': '3E7', 'name': 'Example Airport'}
            >>> city = {'code': 'XYZ', 'name': 'Example City'}
            >>> example_airport = Airport(airport, city)
            >>> example_airport.as_dict()
            {
                'airport_code': '3E7',
                'airport_name': 'Example Airport',
                'city_code': 'XYZ',
                'city_name': 'Example City'<
            }
        
        Returns
            dict: A dictionary representing this Airport. 
        """
        return {
            'airport_code': self.airport_code,
            'airport_name': self.airport_name,
            'city_code': self.city_code,
            'city_name': self.city_name
                }


class Trip:
    """Contains Information about one Trip returned by the API.
    
    The Amount of Trips is determined by the amount of Solutions set in the Request.
      
    Attributes
        
    """
    def __init__(self, trip_data: dict):
        """Create a new Trip object.
        
        Arguments:
            trip_data : dict
                The tripOption dictionary returned by the API to create the Trip Object from
        """
        self.total_price = trip_data['saleTotal']
        self.id


class Result:
    """Contains Results of an API Call.
    
    Attributes
        request_id : str
            Specifies the Request ID, unique for each Request.
            
        airports : list of Airports
            Contains Data for the Flights found in the Response.
            
        taxes : list of Taxes
            Contains the Code and the Name of Taxes found in the Response
            
        carriers : list of Carriers
            Contains the Code and the Name of the Carriers found in the Response
    """

    def __init__(self, data: dict):
        """Create the Result Object from the Response of the API.
        
        Arguments:
            data: dict
                The Response of the API, as a dictionary
        """
        self.request_id = data['trips']['requestId']

        # Save Flight Data
        self.airports = []

        airports = data['trips']['data']['airport']
        cities = data['trips']['data']['city']

        # Match Airport and City together
        for airport_data, city_data in zip(airports, cities):
            # Airport Code and City Code Match - append an Airport Object
            if airport_data['city'] == city_data['code']:
                self.airports.append(Airport(airport_data, city_data))
            else:
                # Search for the Airport matching the City Code
                for city in cities:
                    if city['code'] == airport_data['city']:
                        self.airports.append(Airport(airport_data, city))
                        break
                else:
                    raise ValueError(f'Failed to find matching City for Airport: {airport_data}')

        # Save Taxes
        self.taxes = []

        taxes = data['trips']['data']['tax']
        for tax in taxes:
            self.taxes.append(Tax(tax['id'], tax['name']))

        # Save Carriers
        self.carriers = []
        carriers = data['trips']['data']['carrier']
        for carrier in carriers:
            self.carriers.append(Carrier(carrier['code'], carrier['name']))