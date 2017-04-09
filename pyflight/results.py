"""
These provide several Classes that contain the Results of a Request
to simplify accessing them, as well as offering several Methods
to work with the Data from the Result.

Some of the Documentation is extracted from the resource reference from the API itself,
from which a full documentation can be found here:
https://developers.google.com/qpx-express/v1/trips/search
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
        
    ``len(x)``
        Get the length of the Name of this FlightData.
        
        >>> my_data = FlightData('7H6', 'Example Data')
        >>> len(my_data)
        12
        
        
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

    def __len__(self):
        """Get the length of the Name of this FlightData.
        
        Example
        -------
            >>> my_data = FlightData('7H6', 'Example Data')
            >>> len(my_data)
            12
        
        Returns
        -------
        int
            The length of the name of this FlightData
        """
        return len(self.name)

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
    An Aircraft with a Code (unique identifier) and Name. This Class inherits from 
    :class:`FlightData` and thus, supports all operations that FlightData supports. 
    For Examples, view the "Examples" section of :class:`FlightData`.
    """


class Carrier(FlightData):
    """
    This Class inherits from :class:`FlightData` and thus, supports all operations
    that FlightData supports. It represents a Carrier for the returned solution with 
    a code and a name.
    For Examples, view the "Examples" section for :class:`FlightData`.
    """


class City(FlightData):
    """
    This Class inherits from :class:`FlightData` and thus, supports all operations
    that FlightData supports. This represents a City with a code that uniquely identifies
    it as well as a name.
    For Examples, view the "Examples" section for :class:`FlightData`.
    """


class Tax(FlightData):
    """
    This Class inherits from :class:`FlightData` and thus, supports all operations
    that FlightData supports. This represents a Tax with a code (unique identifier) and a Name. 
    This will also be reflected in the Pricing section of a Trip, but with more information 
    such as the charge type, the country, and the price of the Tax.
    For Examples, view the "Examples" section for :class:`FlightData`.
    """


class Airport(object):
    """
    Contains Data of an Airport and its City Code.
    
    This Class supports various *magic methods*: 
    
    ``x == y``
        Compare two Airports with each other for equality by their Airport and City Codes.
        
        >>> my_airport = Airport({'code': 'ABC', 'name': 'ABC International', 'city': 'Example Airport'})
        >>> another_airport = Airport({'code': 'XYZ', 'name': 'XYZ International', 'city': 'Another Airport'})
        >>> my_airport == another_airport
        False
        
    ``x != y``
        Compare two Airports with each other for inequality.
        
        >>> my_airport != another_airport
        True
        
    ``str(x)``
        Get the Airport's Name
        
        >>> str(my_airport)
        'ABC International'
        
    ``len(x)``
        Get the length of the Airport's name
        
        >>> len(my_airport)
        17
    
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
        """Create an Airport Object containing Data about an Airport and its associated City.
        
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

    def __len__(self):
        """Get the length of the Airport Name.
        
        Example
        -------
            >>> airport = {'code': '3E7', 'city': 'XYZ', 'name': 'Example Airport'}
            >>> example_airport = Airport(airport)
            >>> len(example_airport)
            15
        
        Returns
        -------
        int
            The length of the Airport Name 
        """
        return len(self.name)

    def __str__(self):
        """Get this airport's name
        
        Example
        -------
            >>> airport = {'code': '3E7', 'city': 'XYZ', 'name': 'Example Airport'}
            >>> example_airport = Airport(airport)
            >>> str(example_airport)
            Example Airport
        
        Returns
        -------
        str
            A representation of this Airport as a String.
        """
        return self.name

    def as_dict(self):
        """Get a dictionary representation of the Airport.
        
        Example
        -------
            >>> airport = {'code': '3E7', 'city': 'XYZ', 'name': 'Example Airport'}
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


class Flight(object):
    """
    The smallest unit of travel, identifies a flight from takeoff to landing. 
    
    In the API Response, this is found as ``trips.tripOption[].slice[].segment[].leg[]``
    
    This class supports various *magic methods*:
    
    ``x == y``
        Compare two :class:`Flight`\s with each other for equality.
        
    ``x != y``
        Compare two :class:`Flight`\s with each other for inequality.
        
    ``str(x)``
        Get the :class:`Flight`'s ``id`` as a String.

    
    Attributes
    ----------
        id : str
            A unique identifier for this Flight Object
        aircraft : str
            The aircraft travelling between the two points of this Flight
        departure_time : str
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
            The scheduled Terminal from which this Flight should depart on. ``''`` (empty string) if not specified.
        destination_terminal : str
            The scheduled Terminal where this Flight should arrive at. ``''`` (empty string) if not specified.
        mileage : int
            The number of miles flown in this Flight
        meal : str
            A description of the meal(s) served on the flight, ``''`` (empty string) if not specified.
        change_plane : bool
            Whether passengers have to change planes following this leg. Applies to the next leg, defaults to False.
        performance : int
            Specifies the published on time performance on this leg. ``None`` if not specified.
    """
    def __init__(self, leg_data: dict):
        """Create a new Flight Object
        
        Parameters
        ----------
            leg_data : dict
                The Leg Data given from the API to initialize this Object from
        """
        self.id = leg_data['id']
        self.aircraft = leg_data['aircraft']
        self.departure_time = leg_data['departureTime']
        self.arrival_time = leg_data['arrivalTime']
        self.duration = leg_data['duration']
        self.origin = leg_data['origin']
        self.destination = leg_data['destination']
        self.origin_terminal = leg_data.get('originTerminal', '')
        self.destination_terminal = leg_data.get('destinationTerminal', '')
        self.mileage = leg_data['mileage']
        self.meal = leg_data.get('meal', '')
        self.change_plane = leg_data.get('changePlane', '')
        self.performance = leg_data.get('onTimePerformance', None)

    def __eq__(self, other):
        """Compare two :class:`Flight`s with each other for equality.
        
        Parameters
        ----------
        other : :class:`Flight`
            The other :class:`Flight` to compare to.
            
        Returns
        -------
        bool
            ``True`` or ``False``, depending on the result of the comparison.
        """
        return self.id == other.id

    def __str__(self):
        """Get a string representing the ID of this instance of :class:`Flight`"""
        return self.id

    def as_dict(self):
        """Get this object in the form of a dictionary.
        
        Returns
        -------
        dict
            A dictionary representing all attributes of this :class:`Flight` as Key / Value pairs.
        """
        return self.__dict__


class Segment(object):
    """A single Segment consisting of one or more consecutive legs on the same flight.
    
    As an example, a Flight could have a stop between the origin and destination,
    resulting in two Segments instead of one. This contains information about
    one Single Segment's duration - for example, a flight from DFW to HNL, as well
    as other information about the Flight that this Segment describes.
    
    In the Response, this is represented as ``trips.tripOption[].slice[].segment[]``
    
    This class supports various *magic methods*:
    
    ``x == y``
        Compares two :class:`Segment`\s for equality.
        
    ``x != y``
        Compares two :class:`Segment`\s for inequality.
    
    ``str(x)``
        Get the ID of this :class:`Segment` object.
    
    Attributes
    ----------
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
        flights : list of :class:`Flight`
            The flights from takeoff to landing for this Segment.
    """
    def __init__(self, segment: dict):
        """Create a new Segment Object.
        
        Parameters
        ----------
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

    def __eq__(self, other):
        """Compare one :class:`Segment` object to another."""
        return self.id == other.id

    def __str__(self):
        """Get the ID of this :class:`Segment` object."""
        return self.id

    def find_flight(self, condition_function):
        """Find a Flight out of the List of Flights in this :class:`Flight`\s that matches the passed function.
        This will return the first :class:`Flight` for which ``condition_function`` returns ``True``.
        For example, finding the first matching flight by its Carrier: ::
            
            flight = find_flight(lambda f: f.flight_carrier == 'AB')
            
        Parameters
        ---------
        condition_function : function
            A function that returns a ``bool`` as a result of, for example, a comparison.
            
        Returns
        -------
        :class:`Flight`
            If the search was successful and a :class:`Flight` was found
        None
            If no element has been found
        """
        for flight in self.flights:
            if condition_function(flight):
                return flight
        return None

    def find_all_flights(self, condition_function):
        """Similar to :meth:`find_flight`\, except that it returns a list of :class:`Flight`\s matching the condition
        in the passed function instead of a single :class:`Flight` or ``None``. This returns all :class:`Flight`\s for
        which ``condition_function`` returns True.
        
        Parameters
        ---------
        condition_function : function
            A function that returns a ``bool`` as a result of, for example, a comparison.
            
        Returns
        -------
        list of :class:`Flight`\s
            If the search was successful
        empty list
            If nothing was found
        """
        matching_flights = []
        for flight in self.flights:
            if condition_function(flight):
                matching_flights.append(flight)
        return matching_flights

    def as_dict(self):
        """Get a dictionary representing the contents of this :class:`Segment`.
        
        Returns
        -------
        dict
            A dictionary containing the Data of this :class:`Flight` object.
        """
        return {
            'id': self.id,
            'duration': self.duration,
            'cabin': self.cabin,
            'booking_code': self.booking_code,
            'booking_code_count': self.booking_code_count,
            'flight_carrier': self.flight_carrier,
            'flight_number': self.flight_number,
            'married_segment_group': self.married_segment_group,
            'flights': [x.as_dict() for x in self.flights]
        }


class Route(object):
    """Represents the traveller's intent as well as a low-fare search about an itinerary between two points.
    
    In the Response, this is represented as ``trips.tripOption[].slice[]``
    
    This Class supports various *magic methods*:
        
    ``x == y``
        Compares two duration of two :class:`Route`\s with each other for equality.
        Returns ``True`` when ``x.duration == y.duration``.
        
    ``x != y``
        Compares two duration of two :class:`Route`\s with each other for inequality.
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
        segments : list of :class:`Segment`\s
            Segments consisting of one more consecutive legs on the same flight.
    """
    def __init__(self, route_slice: dict):
        """Create a new Route Object.
        
        Parameters
        ----------
            route_slice : dict
                The ``trips.tripsOption[].slice[]`` Object from the Response
        """
        self.duration = route_slice['duration']

        # Save Segments
        self.segments = []
        for segment in route_slice['segment']:
            self.segments.append(Segment(segment))

    def __lt__(self, other):
        """Compare the duration of two :class:`Route`\s.
        
        Returns
        -------
        bool
            The result of the comparison, depending on the ``duration`` of two :class:`Route`\s."""
        return self.duration < other.duration

    def __le__(self, other):
        """Compare the duration of two :class:`Route`\s.
        
        Returns
        -------
        bool
            The result of the comparison, depending on the ``duration`` of two :class:`Route`\s."""
        return self.duration <= other.duration

    def __gt__(self, other):
        """Compare the duration of two :class:`Route`\s
        
        Returns
        -------
        bool
            The result of the comparison, depending on the ``duration`` of two :class:`Route`\s.
        """
        return self.duration > other.duration

    def __ge__(self, other):
        """Compare the duration of two :class:`Route`\s
         
        Returns
        -------
        bool
            The result of the comparison, depending on the ``duration`` of two :class:`Route`\s.
        """
        return self.duration >= other.duration

    def __eq__(self, other):
        """Compare the duration of two :class:`Route`\s with each other.
        
        Returns
        -------
        bool
            The result of the comparison, depending on the ``duration`` of two :class:`Route`s.
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
            'segments': [
                segment.as_dict() for segment in self.segments
            ]
        }


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
            Specifies whether this is a private fare offered only to select customers or not.
            Defaults to ``False``.
    """
    def __init__(self, fare_data: dict):
        """
        Create a new Fare Object.
        
        Parameters
        ----------
            fare_data : dict 
                A Fare Object returned in from the API in arrays.
        """
        self.id = fare_data['id']
        self.carrier_code = fare_data['carrier']
        self.origin_city_code = fare_data['origin']
        self.destination_city_code = fare_data['destination']
        self.basis_code = fare_data['basisCode']
        self.private = fare_data.get('private', False)

    def __eq__(self, other):
        """Compare two :class:`Fare`\s for equality.
        
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
            A dictionary containing the attributes of this :class:`Fare` as key / value pairs.
        """
        return self.__dict__


class BagDescriptor(object):
    """A representation of a type of bag.
    
    This class supports various *magic methods*:
    
    ``x == y``
        Compare two :class:`BagDescriptor`\s for equality.
        Works by comparing their attributes, so it returns ``True`` when ``x.__dict__ == y.__dict__``.
        
    ``x != y``
        Compare two :class:`BagDescriptor`\s for inequality.
        Works by comparing their attributes, so it returns ``True`` when ``x.__dict__ != y.__dict``.
        
    ``str(x)``
        Returns the ``commercial_name`` of a :class:`BagDescriptor`.
    
    Attributes
    ----------
        commercial_name : str
            The commercial name for this :class:`BagDescriptor` for an optional service, can also be an empty string.
        count : int
            How many of this type of bag will be checked on this flight.
        description : list
            A list of strings describing the baggage. Can be an empty list.
        subcode : str
            An IATA subcode used to identify the optional service
        max_kilos : int
            Specifies the maximum number of kilos that all the free baggage together may weigh.
            ``None`` if not specified.
        kilos_per_piece : int
            Specifies the maximum number of kilos that any piece of baggage may weigh.
            ``None`` if not specified.
        pounds : int
            The number of pounds of free baggage allowed. ``None`` if not specified.
        
    Notes
    -----
        A single :class:`FreeBaggageOption` contains multiple BagDescriptors.
    """
    def __init__(self, bag_descriptor_data: dict):
        """Create a new BagDescriptor object.
        
        Parameters
        ----------
            bag_descriptor_data : dict
                The Bag Descriptor data as a dictionary, returned from the API in Arrays.
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
        """Compare two :class:`BagDescriptor` objects with each other for equality by their attributes.
        
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
            A dictionary with key / value pairs containing the attributes of this :class:`BagDescriptor`.
        """
        return self.__dict__


class FreeBaggageOption(object):
    """Contains Information about the free baggage allowance for one Segment.
    
    Attributes
    ----------
        pieces : int
            How many pieces of free baggage are allowed
        bag_descriptors : list
            A list of :class:`BagDescriptor` Objects used to represent different types of bags.
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

        self.bag_descriptors = []
        for bag_descriptor in baggage_data.get('bagDescriptor', []):
            self.bag_descriptors.append(BagDescriptor(bag_descriptor))

    def as_dict(self):
        """Return a dictionary representation of this :class:`FreeBaggageOption`.
        
        Returns
        -------
        dict
            A dictionary with key / value pairs containing the attributes of this :class:`FreeBaggageOption`.
        """
        return {
            'pieces': self.pieces,
            'bag_descriptors': [
                bd.as_dict() for bd in self.bag_descriptors
            ]
        }


class SegmentPricing(object):
    """Price and baggage information for segments.
    
    This class supports various *magic methods*:
    
    ``x == y``
        Compares two :class:`SegmentPricing`\s for equality.
        Returns ``True`` if ``x.segment_id == y.segment_id and x.fare_id == y.fare_id``.
        
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
            The Fare ID for this :class:`SegmentPricing. Used to refer to different parts of the same solution.
        free_baggage : list
            A list of :class:`FreeBaggageOption` objects for the free baggage allowance on this segment. 
    
    """
    def __init__(self, segment_data: dict):
        """Create a new SegmentPricing object.
        
        Arguments:
            segment_data : dict
                The Data for a single SegmentPricing returned in Arrays from the API. 
                
        """
        self.segment_id = segment_data['segmentId']
        self.fare_id = segment_data['fareId']

        self.free_baggage = []
        for free_baggage_option in segment_data['freeBaggageOption']:
            self.free_baggage.append(FreeBaggageOption(free_baggage_option))

    def __eq__(self, other):
        """Compares two :class:`SegmentPricing` objects for equality.
        
        Returns
        -------
        bool
            True or False, depending on the result of the comparison.
        """
        return self.segment_id == other.segment_id and self.fare_id == other.fare_id

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
            A dictionary containing the attributes of this :class:`SegmentPricing` as key / value pairs.
        """
        return {
            'segment_id': self.segment_id,
            'fare_id': self.fare_id,
            'free_baggage': [
                fbo.as_dict() for fbo in self.free_baggage
            ]
        }


class TaxPricing(object):
    """The taxes used to calculate the tax total per ticket.
    
    This extends the information being held in the :class:`Tax` objects.
    
    This class supports various *magic methods*:
    
    ``x == y``
        Check if two :class:`TaxPricing` objects are equal.
        Returns ``True`` if ``x.id == y.id``.
        
    ``x != y``
        Check if two :class:`TaxPricing` objects are equal.
        Returns ``True`` if ``x.id != y.id``.
        
    ``str(x)``
        Returns the ``id`` of this :class:`TaxPricing`
    
    Attributes
    ----------
        id : str
            The unique identifier for this tax in a response, which is not present
            for unnamed carrier surcharges. ``''`` (empty string) if not present.
        charge_type : str
            Specifies the charge type for this :class:`Tax` - whether it is a government charge or a carrier surcharge.
        code : str
            The code to enter in the ticket's tax box.
        country : str
            The country issuing the charge, for government charges only. 
            ``''`` (Empty string) if not a government charge.
        sale_price : str
            The price of the tax in the sales or equivalent currency.
    """
    def __init__(self, pricing_tax_data: dict):
        """Create a new :class:`TaxPricing` object.
        
        Args:
            pricing_tax_data : dict
                The ``pricing[].tax[]` data returned from the API.
        """
        self.id = pricing_tax_data.get('id', '')
        self.charge_type = pricing_tax_data['chargeType']
        self.code = pricing_tax_data['code']
        self.country = pricing_tax_data.get('country', '')
        self.sale_price = pricing_tax_data['salePrice']

    def __eq__(self, other):
        """Compare two :class:`TaxPricing` objects.
        
        Returns
        -------
        bool
            True or False depending on the result of the comparison
        """
        return self.id == other.id

    def __str__(self):
        """Get the ``id`` of this :class:`TaxPricing` object.
        
        Returns
        -------
        str
            The ``id`` of this :class:`TaxPricing`
        """
        return self.id

    def as_dict(self):
        """Get a dictionary representation of this :class:`TaxPricing`
        
        Returns
        -------
        dict
            A dictionary containing the attributes of this :class:`TaxPricing` as key / value pairs.
        """
        return self.__dict__


class Pricing(object):
    """
    Contains Information about the pricing of the given Route, per passenger.
    
    Attributes
    ----------
        fares : list of :class:`Fare`
            A list of :class:`Fare` objects used to price one or more segments.
        segment_pricing : list of :class:`SegmentPricing`
            A list of :class:`SegmentPricing` objects used to price one segment.
        base_fare_total : str
            The total fare in the currency of the country of origin.
            ``None`` when the sales currency and the currency of the country of commencement are not different
        sale_fare_total : str
            The total fare in the sale or equivalent currency.
        sale_fare_total : str
            The total fare in the sale or equivalent currency.
        sale_tax_total : str
            The taxes in the sale or equivalent currency.
        sale_total : str
            The total per-passenger price (fare + tax) in the sale of equivalent currency.
        adults : int
            The amount of passengers that are adults.
        children : int
            The amount of passengers that are children.
        infants_in_lap : int
            The amount of passengers that are infants travelling in the lap of an adult.
        infants_in_seat : int
            The amount of passengers that are infants assigned to a seat.
        seniors : int
            The amount of passengers that are senior citizens.
        fare_calculation : str
            The horizontal fare calculation. On a ticket, this is a field that displays
            all of the relevant items that go into the calculation of the fare.
        latest_ticketing_time : str
            The latest ticketing time for this pricing assuming there is no change in fares / rules 
            and the reservation occurs at ticketing time.
        for_passenger_type : str
            Specifies the passenger type code for this pricing, used by a carrier to restrict
            fares to certain categories of passengers (for example, a fare might be valid only
            for senior citizens).
        refundable : bool
            Specifies whether the fares on this pricing are refundable. 
            If the API does not specify this explicitly in the response, it defaults to ``False``.

    """
    def __init__(self, pricing_data: dict):
        """
        Create a new Pricing object from fare data.
        
        Parameters
        ----------
            pricing_data : dict
                The Pricing Data Object as returned from the API in an Array
        """
        self.fares = []
        for fare in pricing_data['fare']:
            self.fares.append(Fare(fare))

        self.segment_pricing = []
        for segment_pricing in pricing_data['segmentPricing']:
            self.segment_pricing.append(SegmentPricing(segment_pricing))

        self.base_fare_total = pricing_data.get('baseFareTotal')
        self.sale_fare_total = pricing_data['saleFareTotal']
        self.sale_tax_total = pricing_data['saleTaxTotal']
        self.sale_total = pricing_data['saleTotal']
        self.adults = pricing_data['passengers'].get('adultCount', 0)
        self.children = pricing_data['passengers'].get('childCount', 0)
        self.infants_in_lap = pricing_data['passengers'].get('infantInLapCount', 0)
        self.infants_in_seat = pricing_data['passengers'].get('infantInSeatCount', 0)
        self.seniors = pricing_data['passengers'].get('seniorCount', 0)
        self.fare_calculation = pricing_data['fareCalculation']
        self.latest_ticketing_time = pricing_data['latestTicketingTime']
        self.for_passenger_type = pricing_data['ptc']
        self.refundable = pricing_data.get('refundable', False)

    def as_dict(self):
        """Get a dictionary representing this :class:`Pricing`.
        
        Returns
        -------
        dict
            A dictionary containing the attributes of this :class:`Pricing` as key / value pairs.
        """
        return {
            'fares': [
                f.as_dict() for f in self.fares
            ],
            'segment_pricing': [
                sp.as_dict() for sp in self.segment_pricing
            ],
            'base_fare_total': self.base_fare_total,
            'sale_fare_total': self.sale_fare_total,
            'sale_tax_total': self.sale_tax_total,
            'sale_total': self.sale_total,
            'adults': self.adults,
            'children': self.children,
            'infants_in_lap': self.infants_in_lap,
            'infants_in_seat': self.infants_in_seat,
            'seniors': self.seniors,
            'fare_calculation': self.fare_calculation,
            'latest_ticketing_time': self.latest_ticketing_time,
            'for_passenger_type': self.for_passenger_type,
            'refundable': self.refundable
        }


class Trip(object):
    """Contains Information about one Trip - an itinerary solution - returned by the API.
      `
    This class supports various *magic methods*:
    
    ``x == y``
        Compares two :class:`Trip`\s with each other for equality.
        Returns ``True`` when ``x.id == y.id``.
        
    ``x != y``
        Compares two :class:`Trip`\s with each other for inequality.
        Returns ``True`` when ``x.id != y.id``.
        
    ``str(x)``
        Returns the ``id`` of the :class:`Trip` this is invoked on.
    
    Attributes
    ----------
        total_price : str
            The total price as Currency followed by the Amount for all Passengers on the Trip, e.g. ``'USD59.00'``
        id : str
            The unique ID given to each Trip
        routes : list of :class:`Route`
            A list of Routes from this Trip
        pricing : list of :class:`Pricing`
            A list of pricing data from this Trip
    """
    def __init__(self, trip_data: dict):
        """Create a new Trip object.
        
        Parameters
        ----------
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

    def __eq__(self, other):
        """Compare two :class:`Trip` objects with each other for equality
        
        Returns
        -------
        bool
            True or False depending on the result of the comparison
        """
        return self.id == other.id

    def __str__(self):
        """Returns the ``id`` of this :class:`Trip`.
        
        Returns
        -------
        str
            The ``id`` of this :class:`Trip`
        """
        return self.id


class Result(object):
    """Contains Results of an API Call.
    
    This Class supports various *magic methods*:
    
    ``x == y``
        Checks if two :class:`Result`\s are identical.
        This is equivalent to ``x.request_id == y.request_id``.
        
    ``x != y``
        Checks if two :class:`Result`\s are not identical to each other.
        This is equivalent to ``x.request_id != y.request_id``.
        
    ``str(x)``
        Returns the ``request_id`` for the :class:`Result` this is invoked on.
    
    Attributes
    ----------
        request_id : str
            Specifies the Request ID, unique for each Request.
            
        airports : list of :class:`Airport`
            Contains Data for the Flights found in the Response.
            
        carriers : list of :class:`Carrier`
            Contains the Code and the Name of the Carriers found in the Response
            
        taxes : list of :class:`Tax`
            Contains the Code and the Name of Taxes found in the Response
            
        trips : list of :class:`Trip`
            Contains information about trips (itinerary solutions) returned by the API.
            The Amount of Trips is determined by the amount of Solutions set in the Request.
    """

    def __init__(self, data: dict):
        """Create the Result Object from the Response of the API.
        
        Parameters
        ----------
            data: dict
                The Response of the API, as a dictionary
        """
        self.request_id = data['trips']['requestId']

        # Save Airports
        self.airports = []
        airports = data['trips']['data']['airport']
        for airport in airports:
            self.airports.append(Airport(airport))

        # Save Aircraft
        self.aircraft = []
        for single_aircraft in data['trips']['data']['aircraft']:
            self.aircraft.append(Aircraft(single_aircraft['code'], single_aircraft['name']))

        # Save Carriers
        self.carriers = []
        carriers = data['trips']['data']['carrier']
        for carrier in carriers:
            self.carriers.append(Carrier(carrier['code'], carrier['name']))

        # Save Cities
        self.cities = []
        for city in data['trips']['data']['city']:
            self.cities.append(City(city['code'], city['name']))

        # Save Taxes
        self.taxes = []
        taxes = data['trips']['data']['tax']
        for tax in taxes:
            self.taxes.append(Tax(tax['id'], tax['name']))

        # Save Trips
        self.trips = []
        trips = data['trips']['tripOption']
        for trip in trips:
            self.trips.append(Trip(trip))

    def __eq__(self, other):
        """Compare two :class:`Result` objects for equality.
        
        Returns
        -------
        bool
            True or False depending on the result of the comparison
        """
        return self.request_id == other.request_id

    def __str__(self):
        """Get the ID of this :class:`Request`.
        
        Returns
        -------
        str
            The ``request_id`` of the :class:`Request` this is invoked on.
        """
        return self.request_id
