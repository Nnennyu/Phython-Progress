#page 250
#UNIT TEST AND TEST CASES
""" A module unittest from python library is used to verify that one specific aspect of a function's
 behavior is correct. A test case with full coverage includes a full range of unit tests covering
  all the possible ways you can use a function."""

#Exercise 11-1 pg255
"""To write a test case for a function, import the unittest module and the function you want to test. 
Then create a class that inherits from unittest.TestCase, and write a series of methods to test different 
aspects of your function’s behavior"""
'''
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Test for 'city_functions.py'. """

    def test_city_and_country_names(self):
        """To make sure city and country names like 'Paris, France' works."""
        city = city_country("paris", "france")
        self.assertEqual(city, 'Paris, France')

unittest.main()
'''

#EXERCISE 11-2 modifying city_functions and adding Population
import unittest
from city_functions import formatted_city_country

class FormattedCityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py' ."""

    def test_city_country_names(self):
        """To make sure city and country names like 'London, UK' works. """
        city = formatted_city_country('london', 'united kingdom')
        self.assertEqual(city, 'London, United Kingdom')

    def test_city_country_name_and_population(self):
        """To make sure city information in this form
        'London, United Kingdom - population 8900000' works."""
        city_information = formatted_city_country('london', 'united kingdom', 8900000)
        self.assertEqual(city_information,
                         'London, United Kingdom - Population 8900000')

unittest.main()
