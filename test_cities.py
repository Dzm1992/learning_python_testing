from city_functions import miasta_panstwa
import unittest

class CityTestCase(unittest.TestCase):
	"""Testy dla programu 'city_functions.py'."""
	
	def test_miasta_panstwa(self):
		"""Czy funkcja działa prawidłowo?"""
		
		formatted_cities = miasta_panstwa('santiago', 'chile')
		self.assertEqual(formatted_cities, 'Santiago, Chile')
		
unittest.main()
