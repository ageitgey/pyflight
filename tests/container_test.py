# Tests the various Containers / Classes found in results.py

# Change Directory to Parent Directory
import os
import sys

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
    assert str(first_tax) == '9B1: Example Tax'
    assert str(second_tax) == '7B3: Another Example Tax'
    assert str(third_tax) == '9B1: Example Tax'

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


