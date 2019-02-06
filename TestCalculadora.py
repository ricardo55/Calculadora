import unittest
from Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

	def test_suma_2_mas_2(self):
		calc= Calculadora()
		self.assertEquals(4,calc.sumar(2,2))

	def test_suma_4_mas_4(self):
		calc= Calculadora()
		self.assertEquals(8,calc.sumar(4,4))


if __name__ == '__main__':
	unittest.main()
	
