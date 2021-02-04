import unittest

def average(elements):
	length = len(elements)
	if length == 0:
		raise ValueError
	accum = 0
	for x in elements:
		if type(x) not in [int, float]:
			raise TypeError
		accum+=x
	return accum/length
	
class TestAverage(unittest.TestCase):
	def test_volume(self):
		with self.assertRaises(ValueError):
			average([])
		with self.assertRaises(TypeError):
			average(['a','b',3])

		self.assertEqual(average([5,-5,3]),1)


if __name__ == '__main__':
    unittest.main()


