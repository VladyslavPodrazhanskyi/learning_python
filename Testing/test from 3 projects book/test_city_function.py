import unittest
from city_functions import city_function

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city = city_function("Kharkiv", "Ukraine")
        self.assertEqual(city, "Kharkiv, Ukraine")


    def test_city_country_population(self):
        city = city_function("Rome", "Italy", 2873000)
        self.assertEqual(city, "Rome, Italy - population 2873000.")


if __name__ == "__main__":
    unittest.main()