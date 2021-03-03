import unittest
import fizzbuzz
class TestCase(unittest.TestCase):

	def test1(self):
		self.assertEqual(fizzbuzz, ['FizzBuzz', 2, 3, 'Fizz', 5, 'Buzz', 'Fizz', 8, 9, 'Fizz', 'Buzz', 12, 'Fizz', 14, 15, 'FizzBuzz', 17, 18, 'Fizz', 20, 'Buzz', 'Fizz', 23, 24, 'Fizz', 'Buzz', 27, 'Fizz', 29, 30, 'FizzBuzz', 32, 33, 'Fizz', 35, 'Buzz', 'Fizz', 38, 39, 'Fizz', 'Buzz', 42, 'Fizz', 44, 45, 'FizzBuzz', 47, 48, 'Fizz', 50, 'Buzz', 'Fizz', 53, 54, 'Fizz', 'Buzz', 57, 'Fizz', 59, 60, 'FizzBuzz', 62, 63, 'Fizz', 65, 'Buzz', 'Fizz', 68, 69, 'Fizz', 'Buzz', 72, 'Fizz', 74, 75, 'FizzBuzz', 77, 78, 'Fizz', 80, 'Buzz', 'Fizz', 83, 84, 'Fizz', 'Buzz', 87, 'Fizz', 89, 90, 'FizzBuzz', 92, 93, 'Fizz', 95, 'Buzz', 'Fizz', 98, 99, 'Fizz'])


if __name__ == '__main__':
    unittest.main()