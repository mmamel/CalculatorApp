import unittest

def fullName(first, last):
	lenF = len(first)
	lenL = len(last)
	if lenL == 0 or lenF == 0:
		raise ValueError
	if not all(ele in [str] for ele in (type(first), type(last))):
		raise TypeError
	return first +" " + last
	
class TestAverage(unittest.TestCase):
	def test_volume(self):
		with self.assertRaises(ValueError):
			fullName('','')
		with self.assertRaises(TypeError):
			fullName(3,[])

		self.assertEqual(fullName("mac" ,"hombre"), "mac hombre")


if __name__ == '__main__':
    unittest.main()


