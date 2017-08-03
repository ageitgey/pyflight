# Tests the various Containers / Classes found in results.py

import os
import sys

import util

from pyflight.result import *
from pyflight.models.flight_data import FlightData


# Test the FlightData Container
def test_flight_data():
    first_data = FlightData('9B1', 'Example Data')
    second_data = FlightData('7B3', 'Another Example Data')
    third_data = FlightData('9B1', 'Example Data')

    # Test the __eq__ overload
    assert first_data != second_data
    assert first_data == third_data
    assert third_data == first_data

    # Test the __str__ overload
    assert str(first_data) == 'Example Data'
    assert str(second_data) == 'Another Example Data'
    assert str(third_data) == 'Example Data'

    # Test the as_dict method
    assert first_data.as_dict() == {
        'code': '9B1',
        'name': 'Example Data'
    }
    assert second_data.as_dict() == {
        'code': '7B3',
        'name': 'Another Example Data'
    }
    assert third_data.as_dict() == {
        'code': '9B1',
        'name': 'Example Data'
    }


# Test the Airport Container
def test_airport():
    first_airport = Airport({'code': '13', 'city': 'C83', 'name': 'Some Airport'})
    second_airport = Airport({'code': '58', 'city': '337', 'name': 'Another Airport'})
    third_airport = Airport({'code': '31', 'city': '958', 'name': 'Airport Airport'})

    # Test the __eq__ overload
    assert first_airport == first_airport
    assert first_airport != second_airport
    assert first_airport != third_airport
    assert second_airport == second_airport
    assert second_airport != third_airport
    assert third_airport == third_airport

    # Test the __str__ overload
    assert str(first_airport) == 'Some Airport'
    assert str(second_airport) == 'Another Airport'
    assert str(third_airport) == 'Airport Airport'

    # Test the as_dict method
    assert first_airport.as_dict() == {
        'code': '13',
        'city': 'C83',
        'name': 'Some Airport'
    }
    assert second_airport.as_dict() == {
        'code': '58',
        'city': '337',
        'name': 'Another Airport'
    }
    assert third_airport.as_dict() == {
        'code': '31',
        'city': '958',
        'name': 'Airport Airport'
    }


first_result = Result(util.download_file_if_not_exists(
    url="https://developers.google.com/qpx-express/v1/json.samples/SFOLAX.out.json",
    filename="response_1.json"
))
second_result = Result(util.download_file_if_not_exists(
    url="https://developers.google.com/qpx-express/v1/json.samples/OGGNCE.out.json",
    filename="response_2.json"
))


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
    assert first_result.airports[0].code == 'LAX'
    assert first_result.airports[0].name == 'Los Angeles International'
    assert first_result.airports[0].city == 'LAX'

    assert first_result.airports[1].code == 'SFO'
    assert first_result.airports[1].name == 'San Francisco International'
    assert first_result.airports[1].city == 'SFO'

    assert second_result.airports[0].code == 'CDG'
    assert second_result.airports[0].name == 'Paris Charles de Gaulle'
    assert second_result.airports[0].city == 'PAR'

    assert second_result.airports[1].code == 'FRA'
    assert second_result.airports[1].name == 'Frankfurt International'
    assert second_result.airports[1].city == 'FRA'


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
