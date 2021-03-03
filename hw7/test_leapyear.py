import unittest
import leapyear
class TestCase(unittest.TestCase):

	def test1(self):
		self.assertEqual(leapyear.leapyear(1904), True)
		self.assertEqual(leapyear.leapyear(2001), False)
		self.assertEqual(leapyear.leapyear(2020), True)
		self.assertEqual(leapyear.leapyear(1873), False)


if __name__ == '__main__':
    unittest.main()