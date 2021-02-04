import unittest
import calc
class TestCalcMethods(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc.add(2,4.3), 6.3)
		self.assertEqual(calc.add(-3,1), -2)

	def test_sub(self):
		self.assertEqual(calc.sub(10.3,2.4), 7.9)
		self.assertEqual(calc.sub(-3,-5),2)
	def test_mul(self):
		self.assertEqual(calc.mul(3,9), 27)
		self.assertEqual(calc.mul(-1,0), 0)
	def test_div(self):
		self.assertEqual(calc.div(3,2), 1.5)
		with self.assertRaises(ZeroDivisionError):
		 	calc.div(3,0)

if __name__ == '__main__':
    unittest.main()


