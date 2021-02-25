import unittest
import fibonacci
class TestCalcMethods(unittest.TestCase):

	def test_fib(self):
		self.assertEqual(fibonacci.fib(7), [0, 1, 1, 2, 3, 5, 8])
		self.assertEqual(fibonacci.fib(0), [])
	def test_fact(self):
		self.assertEqual(fibonacci.fact(0), 1)
		self.assertEqual(fibonacci.fact(1), 1)
		self.assertEqual(fibonacci.fact(5), 120)


if __name__ == '__main__':
    unittest.main()