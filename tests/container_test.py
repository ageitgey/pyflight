# Tests the various Containers / Classes found in results.py

import json
import os
import sys

# Change Directory to Parent Directory
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path + '/../')

from pyflight.results import *


# Test the Tax Container
def test_tax():
    first_tax = Tax('9B1', 'Example Tax')
    second_tax = Tax('7B3', 'Another Example Tax')
    third_tax = first_tax

    # Test the __eq__ overload
    assert first_tax != second_tax
    assert second_tax != first_tax
    assert first_tax == third_tax
    assert third_tax == first_tax

    # Test the __len__ overload
    assert len(first_tax) == 11
    assert len(second_tax) == 19
    assert len(third_tax) == 11

    # Test the __str__ overload
    assert str(first_tax) == 'Example Tax'
    assert str(second_tax) == 'Another Example Tax'
    assert str(third_tax) == 'Example Tax'

    # Test the as_dict method
    assert first_tax.as_dict() == {'id': '9B1', 'name': 'Example Tax'}
    assert second_tax.as_dict() == {'id': '7B3', 'name': 'Another Example Tax'}
    assert third_tax.as_dict() == {'id': '9B1', 'name': 'Example Tax'}


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


# Test the Aircraft Container
def test_aircraft():
    first_aircraft = Aircraft('350', 'Example Aircraft')
    second_aircraft = Aircraft('021', 'Another Aircraft')
    third_aircraft = Aircraft('358', 'Yet Another Aircraft')

    # Test the __len__ overload
    assert len(first_aircraft) == 16
    assert len(second_aircraft) == 16
    assert len(third_aircraft) == 20

    # Test the __eq__ overload
    assert first_aircraft == first_aircraft
    assert first_aircraft != second_aircraft
    assert first_aircraft != third_aircraft
    assert second_aircraft == second_aircraft
    assert third_aircraft == third_aircraft

    # Test the __str__ overload
    assert str(first_aircraft) == 'Example Aircraft'
    assert str(second_aircraft) == 'Another Aircraft'
    assert str(third_aircraft) == 'Yet Another Aircraft'

    # Test the as_dict method
    assert first_aircraft.as_dict() == {
        'id': '350',
        'name': 'Example Aircraft'
    }
    assert second_aircraft.as_dict() == {
        'id': '021',
        'name': 'Another Aircraft'
    }
    assert third_aircraft.as_dict() == {
        'id': '358',
        'name': 'Yet Another Aircraft'
    }


# Test the Result Container
def test_results():
    # Get sample Data from JSON
    with open('tests/response_1.json') as f:
        first_result = json.load(f)
    with open('tests/response_2.json') as f:
        second_result = json.load(f)

    first_result = Result(first_result)
    second_result = Result(second_result)

    assert first_result.request_id == 'eBJXPDdjvK4zDogeE0JJp3'
    assert second_result.request_id == 'hRI7zJ7vwhikqNiwU0JKDA'
