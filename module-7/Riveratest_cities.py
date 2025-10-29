# test_cities.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_name = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')

    def test_city_country_population_language(self):
        formatted_name = city_country('santiago', 'chile', 5000000, 'spanish')
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000, Spanish')

if __name__ == '__main__':
    unittest.main()
