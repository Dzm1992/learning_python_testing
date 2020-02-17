class Employee():
	"""Tworzy pracownika."""
	
	def __init__(self, name, surname, salary):
		"""Inicjalizajcja atrybutów."""
		self.name = name
		self.surname = surname
		self.salary = int(salary)
		
	def give_raise(self, more_money=5000):
		"""Daje podwyżkę."""
		self.salary += more_money
		print(self.salary)
	
		
Janek = Employee('Janek', 'Kowalski', 5000)
Janek.give_raise()
Janek.give_raise()
Janek.give_raise()	
		
import unittest

class TestEmployee(unittest.TestCase):
	"""Testy dla klasy Employee."""
	
	def setUp(self):
		"""Utworzenie standardowych odpowiedzi."""
		Pszemek = Employee('Janek', 'Kowalski', 5000)
		self.podwyzka = Janek.give_raise()
		
	def test_give_custom_raise(self):
		"""Sprawdzenie czy podwyżka jest równa x."""
		self.assertEqual(self.podwyzka, Janek.give_raise(5000))
	
	def test_give_default_raise1(self):
		"""Sprawdzenie czy podwyżka jest równa x."""
		self.assertEqual(self.podwyzka, Janek.give_raise())
	
unittest.main()

