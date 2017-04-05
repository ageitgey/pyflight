# Tests the various Containers / Classes found in results.py

import json
import os
import sys

# Change Directory to Parent Directory
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path + '/../')

import pyflight
from pyflight.results import *


# Test the FlightData Container
def test_flight_data():
    first_data = FlightData('9B1', 'Example Data')
    second_data = FlightData('7B3', 'Another Example Data')
    third_data = FlightData('9B1', 'Example Data')

    # Test the __eq__ overload
    assert first_data != second_data
    assert first_data == third_data
    assert third_data == first_data

    # Test the __len__ overload
    assert len(first_data) == 12
    assert len(second_data) == 20
    assert len(third_data) == 12

    # Test the __str__ overload
    assert str(first_data) == 'Example Data'
    assert str(second_data) == 'Another Example Data'
    assert str(third_data) == 'Example Data'

    # Test the as_dict method
    assert first_data.as_dict() == {
        'id': '9B1',
        'name': 'Example Data'
    }
    assert second_data.as_dict() == {
        'id': '7B3',
        'name': 'Another Example Data'
    }
    assert third_data.as_dict() == {
        'id': '9B1',
        'name': 'Example Data'
    }


# Test the Airport Container
def test_airport():
    first_airport = Airport({'code': '13', 'name': 'Some Airport'}, {'code': 'C83', 'name': 'Some City'})
    second_airport = Airport({'code': '58', 'name': 'Another Airport'}, {'code': '337', 'name': 'Another City'})
    third_airport = Airport({'code': '31', 'name': 'Airport Airport'}, {'code': '958', 'name': 'City City'})

    # Test the __len__ overload
    assert len(first_airport) == 12
    assert len(second_airport) == 15
    assert len(third_airport) == 15

    # Test the __eq__ overload
    assert first_airport == first_airport
    assert first_airport != second_airport
    assert first_airport != third_airport
    assert second_airport == second_airport
    assert second_airport != third_airport
    assert third_airport == third_airport

    # Test the __str__ overload
    assert str(first_airport) == 'Some Airport in Some City'
    assert str(second_airport) == 'Another Airport in Another City'
    assert str(third_airport) == 'Airport Airport in City City'

    # Test the as_dict method
    assert first_airport.as_dict() == {
        'airport_code': '13',
        'airport_name': 'Some Airport',
        'city_code': 'C83',
        'city_name': 'Some City'
    }
    assert second_airport.as_dict() == {
        'airport_code': '58',
        'airport_name': 'Another Airport',
        'city_code': '337',
        'city_name': 'Another City'
    }
    assert third_airport.as_dict() == {
        'airport_code': '31',
        'airport_name': 'Airport Airport',
        'city_code': '958',
        'city_name': 'City City'
    }

# Get sample Data from JSON
with open('tests/response_1.json') as f:
    first_result = json.load(f)
with open('tests/response_2.json') as f:
    second_result = json.load(f)

first_result = Result(first_result)
second_result = Result(second_result)


# Test the Entry grabbing from the Result Container
def test_result_grab_all_entries():
    assert first_result.request_id == 'eBJXPDdjvK4zDogeE0JJp3'
    assert second_result.request_id == 'hRI7zJ7vwhikqNiwU0JKDA'

    assert len(first_result.aircraft) == 1
    assert len(second_result.aircraft) == 13

    assert len(first_result.airports) == 2
    assert len(second_result.airports) == 9

    assert len(first_result.carriers) == 1
    assert len(second_result.carriers) == 5

    assert len(first_result.taxes) == 4
    assert len(second_result.taxes) == 14

    assert len(first_result.trips) == 1
    assert len(second_result.trips) == 8


# Test correct Grabbing of Aircraft
def test_result_aircraft():
    assert first_result.aircraft[0].code == '320'
    assert first_result.aircraft[0].name == 'Airbus A320'

    assert second_result.aircraft[0].code == '319'
    assert second_result.aircraft[0].name == 'Airbus A319'

    assert second_result.aircraft[1].code == '320'
    assert second_result.aircraft[1].name == 'Airbus A320'

    assert second_result.aircraft[2].code == '321'
    assert second_result.aircraft[2].name == 'Airbus A321'

    assert second_result.aircraft[12].code == '76W'
    assert second_result.aircraft[12].name == 'Boeing 767'


# Test correct Grabbing of Airports
def test_result_airport():
    assert first_result.airports[0].airport_code == 'LAX'
    assert first_result.airports[0].airport_name == 'Los Angeles International'
    assert first_result.airports[0].city_code == 'LAX'
    assert first_result.airports[0].city_name == 'Los Angeles'

    assert first_result.airports[1].airport_code == 'SFO'
    assert first_result.airports[1].airport_name == 'San Francisco International'
    assert first_result.airports[1].city_code == 'SFO'
    assert first_result.airports[1].city_name == 'San Francisco'

    assert second_result.airports[0].airport_code == 'CDG'
    assert second_result.airports[0].airport_name == 'Paris Charles de Gaulle'
    assert second_result.airports[0].city_code == 'PAR'
    assert second_result.airports[0].city_name == 'Paris'

    assert second_result.airports[1].airport_code == 'FRA'
    assert second_result.airports[1].airport_name == 'Frankfurt International'
    assert second_result.airports[1].city_code == 'FRA'
    assert second_result.airports[1].city_name == 'Frankfurt'


# Test correct Grabbing of Carriers
def test_result_carrier():
    assert first_result.carriers[0].code == 'VX'
    assert first_result.carriers[0].name == 'Virgin America Inc.'

    assert second_result.carriers[0].code == 'AF'
    assert second_result.carriers[0].name == 'Air France'

    assert second_result.carriers[1].code == 'DL'
    assert second_result.carriers[1].name == 'Delta Air Lines Inc.'


# Test correct Grabbing of Taxes
def test_result_taxes():
    assert first_result.taxes[0].code == 'ZP'
    assert first_result.taxes[0].name == 'US Flight Segment Tax'

    assert first_result.taxes[1].code == 'XF'
    assert first_result.taxes[1].name == 'US Passenger Facility Charge'

    assert second_result.taxes[0].code == 'DE_1'
    assert second_result.taxes[0].name == 'German Airport Security Tax'

    assert second_result.taxes[1].code == 'XY'
    assert second_result.taxes[1].name == 'US Immigration Fee'


# Test correct Grabbing of Trips
def test_result_trips():
    assert first_result.trips[0].id == 'faqkIcj6Te2V3Sll2SskwJ001'
    assert first_result.trips[0].total_price == 'USD69.00'

    assert second_result.trips[0].id == '43z22eKyiiCSeB8K7CaOB8001'
    assert second_result.trips[0].total_price == 'USD3275.60'

    assert second_result.trips[1].id == '43z22eKyiiCSeB8K7CaOB8002'
    assert second_result.trips[1].total_price == 'USD3345.60'


# Test correct Grabbing of Routes
def test_result_routes():
    assert len(first_result.trips[0].routes) == 1

    assert len(second_result.trips[0].routes) == 2
    assert len(second_result.trips[1].routes) == 2
    assert len(second_result.trips[2].routes) == 2

    assert first_result.trips[0].routes[0].duration == 75
    assert second_result.trips[0].routes[0].duration == 1670
    assert second_result.trips[0].routes[1].duration == 1352


# Test correct Grabbing of Route Segments
def test_result_segments():
    assert len(first_result.trips[0].routes[0].segments) == 1
    assert len(second_result.trips[0].routes[0].segments) == 3
    assert len(second_result.trips[0].routes[1].segments) == 3

    assert first_result.trips[0].routes[0].segments[0].id == 'G4Yqn7Md2QltVrzT'
    assert first_result.trips[0].routes[0].segments[0].flight_carrier == 'VX'
    assert first_result.trips[0].routes[0].segments[0].cabin == 'COACH'
    assert first_result.trips[0].routes[0].segments[0].booking_code_count == 7


# Test correct Grabbing of Route Segment Flights
def test_result_segment_flights():
    assert len(first_result.trips[0].routes[0].segments[0].flights) == 1
    assert len(second_result.trips[0].routes[0].segments[0].flights) == 1

    assert first_result.trips[0].routes[0].segments[0].flights[0].id == 'LFaJowO2NvJzM2Vd'
    assert first_result.trips[0].routes[0].segments[0].flights[0].aircraft == '320'
    assert second_result.trips[0].routes[0].segments[0].flights[0].id == 'LACncSVM+gmtx9mJ'
    assert second_result.trips[0].routes[0].segments[0].flights[0].aircraft == '738'
    assert second_result.trips[0].routes[0].segments[0].flights[0].meal == 'Food and Beverages for Purchase'


# Test correct Grabbing of Pricing Data
def test_result_pricing():
    assert len(first_result.trips[0].pricing) == 1
    assert len(second_result.trips[0].pricing) == 2
    assert len(second_result.trips[2].pricing) == 2
    assert len(first_result.trips[0].pricing[0].segment_pricing) == 1

    assert first_result.trips[0].pricing[0].sale_total == 'USD69.00'
    assert first_result.trips[0].pricing[0].adults == 1
    assert first_result.trips[0].pricing[0].fares[0].id == 'A+yi0+pn2eL1pf3nKwZazHIVDvsw2Ru8zx5LByC/kQaA'
    assert first_result.trips[0].pricing[0].segment_pricing[0].segment_id == 'G4Yqn7Md2QltVrzT'
