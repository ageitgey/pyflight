"""
Provides several Classes that contain the Results of a Request
to simplify accessing them, as well as offering several Methods
to work with the Data from the Result.
"""


class FlightData(object):
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
    """
    An Aircraft with an ID and Name.
    """
    pass


class Tax(FlightData):
    """
    A Tax with an ID and a Name. This will also be reflected 
    in the Pricing section of a Trip, but with more information such as
    the charge type, the country, and the price of the Tax.
    """
    pass


class Carrier(FlightData):
    pass


class Airport(object):
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


class Flight(object):
    """
    The smallest unit of travel, identifies a flight from takeoff to landing. 
    
    In the API Response, this is found as 'trips.tripOption[].slice[].segment[].leg[]'
    
    Attributes
        id : str
            A unique identifier for this Flight Object
        aircraft : str
            The aircraft travelling between the two points of this Flight
        destination_time : str
            The Time of Departure local to the point of departure, with the Time Zone Difference included
        arrival_time : str
            The Time of Arrival local to the point of arrival, with the Time Zone Difference included
        duration : int
            The scheduled Travelling Time between the the two Points, in minutes
        origin : str
            The Origin of this Flight as a City / Airport Code
        destination : str
            The Destination of this Flight as a City / Airport Code
        origin_terminal : str
            The scheduled Terminal from which this Flight should depart on. '' if not specified.
        destination_terminal : str
            The scheduled Terminal where this Flight should arrive at. '' if not specified.
        mileage : int
            The number of miles flown in this Flight
        meal : str
            A description of the meal(s) served on the flight, '' if not specified.
        change_plane : bool
            Whether passengers have to change planes following this leg. Applies to the next leg, defaults to False.
        performance : int
            Specifies the published on time performance on this leg. 0 if not specified.
    """
    def __init__(self, leg_data: dict):
        """Create a new Flight Object
        
        Args:
            leg_data : dict
                The Leg Data given from the API to initialize this Object from
        """
        print(leg_data)
        self.id = leg_data['id']
        self.aircraft = leg_data['aircraft']
        self.departure_time = leg_data['departureTime']
        self.arrival_time = leg_data['arrivalTime']
        self.duration = leg_data['duration']
        self.origin = leg_data['origin']
        self.destination = leg_data['destination']
        self.origin_terminal = leg_data.get('originTerminal', '')
        self.destination_terminal = leg_data.get('detinationTerminal', '')
        self.mileage = leg_data['mileage']
        self.meal = leg_data.get('meal', '')
        self.change_plane = leg_data.get('changePlane', '')
        self.performance = leg_data.get('onTimePerformance', 0)


class Segment(object):
    """A single Segment consisting of one or more consecutive legs on the same flight.
    
    As an example, a Flight could have a stop between the origin and destination,
    resulting in two Segments instead of one. This contains information about
    one Single Segment's duration - for example, a flight from DFW to HNL, as well
    as other information about the Flight that this Segment describes.
    
    In the Response, this is represented as 'trips.tripOption[].slice[].segment[]'
    
    Attributes:
        id : str
            The unique ID identifying this Segment.
        duration : int
            The duration of this Flight Segment, in Minutes
        cabin : str
            The cabin booked for this segment
        booking_code : str
            The booking code or booking class for this Segment
        booking_code_count : int
            The Number of seats available in this Segment with this Booking Code
        flight_carrier : str
            A two-letter IATA airline designator for this Segment
        flight_number : str
            The flight number of this Segment
        married_segment_group : str
            The Index of a Segment in a married Segment Group
    """
    def __init__(self, segment: dict):
        """Create a new Segment Object.
        
        Args:
            segment : dict
                The dictionary to construct this Segment from.
        """
        self.id = segment['id']
        self.duration = segment['duration']

        self.cabin = segment['cabin']
        self.booking_code = segment['bookingCode']
        self.booking_code_count = segment['bookingCodeCount']
        self.flight_carrier = segment['flight']['carrier']
        self.flight_number = segment['flight']['number']
        self.married_segment_group = segment['marriedSegmentGroup']

        # Save Flights
        self.flights = []
        for flight in segment['leg']:
            self.flights.append(Flight(flight))


class Route(object):
    """Represents the traveller's intent as well as a low-fare search about an itinerary between two points.
    
    In the Response, this is represented as 'trips.tripOption[].slice[]'
    
    Attributes:
        duration : int
            The duration of the Route, in Minutes
    """
    def __init__(self, route_slice: dict):
        """Create a new Route Object.
        
        Args:
            route_slice : dict
                The 'trips.tripsOption[].slice[]' Object from the Response
        """
        self.duration = route_slice['duration']

        # Save Segments
        self.segments = []
        for segment in route_slice['segment']:
            self.segments.append(Segment(segment))


class Fare(object):
    """
    The fare used to price one or more segments.
    
    Attributes:
        id : str
            The unique identifier of the fare.
        carrier_code : str
            The Code for the Carrier whose fare this is.
        origin_city_code : str
            The origin city for this fare
        destination_city_code : str
            The destination city for this fare
        basis_code : str
            The Basis Code of this fare.
        private : bool
            Specifies whether this is a private fare offered only to select customers or not.
    """
    def __init__(self, fare_data: dict):
        """
        Create a new Fare Object.
        
        Args:
            fare_data : dict 
                A Fare Object returned in from the API in arrays.
        """
        self.id = fare_data['id']
        self.carrier_code = fare_data['carrier']
        self.origin_city_code = fare_data['origin']
        self.destination_city_code = fare_data['destination']
        self.basis_code = fare_data['basisCode']
        self.private = fare_data.get('private', False)


class FreeBaggageOption(object):
    """Contains Information about the free baggage allowance for one Segment.
    
    Attributes:
        pieces : int
            How many pieces of free baggage are allowed
    
    Notes:
        Information about this is saved in a SegmentPricing class.
    
    """
    def __init__(self, baggage_data: dict):
        """Create a new FreeBaggageOption object. 
        
        Args:
            baggage_data : dict
                The Baggage Data as returned from the API in an Array.
                
        """
        self.pieces = baggage_data['pieces']


class SegmentPricing(object):
    """Price and baggage information for segments.
    
    Attributes:
        fare_id : str
            The Fare ID for this Segment Pricing. Used to refer to different parts of the same solution.
        segment_id : str
            A unique identifier for this SegmentPricing object.
        free_baggage : list
            A list of FreeBaggageOption objects for the free baggage allowance on this segment. 
    
    """
    def __init__(self, segment_data: dict):
        """Create a new SegmentPricing object.
        
        Arguments:
            segment_data : dict
                The Data for a single SegmentPricing returned in Arrays from the API. 
                
        """
        self.fare_id = segment_data['fareId']
        self.segment_id = segment_data['segmentId']

        self.free_baggage = []
        for free_baggage_option in segment_data['freeBaggageOption']:
            self.free_baggage.append(FreeBaggageOption(free_baggage_option))


class Pricing(object):
    """
    Contains Information about the pricing of the given Route, per passenger.
    
    Attributes
        fares : list
            A list of fare objects used to price one or more segments.
        segment_pricing : list
            A list of SegmentPricing objects used to price one segment.
            
    """
    def __init__(self, pricing_data: dict):
        """
        Create a new Pricing object from fare data.
        Args:
            pricing_data : dict
                The Pricing Data Object as returned from the API in an Array
        """
        self.fares = []
        for fare in pricing_data['fare']:
            self.fares.append(Fare(fare))

        self.segment_pricing = []
        for segment_pricing in pricing_data['segmentPricing']:
            self.segment_pricing.append(SegmentPricing(segment_pricing))


class Trip(object):
    """Contains Information about one Trip - an itinerary solution -  returned by the API.
    
    The Amount of Trips is determined by the amount of Solutions set in the Request.
      
    Attributes
        total_price : str
            The total price as Currency followed by the Amount for all Passengers on the Trip, e.g. 'USD59.00'
        id : str
            The unique ID given to each Trip
        routes : list
            A list of Routes from this Trip
        
    """
    def __init__(self, trip_data: dict):
        """Create a new Trip object.
        
        Arguments:
            trip_data : dict
                The tripOption dictionary returned by the API to create the Trip Object from
        """
        self.total_price = trip_data['saleTotal']
        self.id = trip_data['id']

        # Get Routes / Slices
        self.routes = []

        for route in trip_data['slice']:
            self.routes.append(Route(route))

        # Get Pricing Data
        self.pricing = []

        for pricing_data in trip_data['pricing']:
            self.pricing.append(Pricing(pricing_data))


class Result(object):
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

        # Save Aircraft
        self.aircraft = []

        for single_aircraft in data['trips']['data']['aircraft']:
            self.aircraft.append(Aircraft(single_aircraft['code'], single_aircraft['name']))

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

        # Save Trips
        self.trips = []
        trips = data['trips']['tripOption']
        for trip in trips:
            self.trips.append(Trip(trip))
