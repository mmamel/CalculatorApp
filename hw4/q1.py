import unittest

def volume(l):
	if type(l) not in [int, float]:
		raise TypeError
	if l < 0:
		raise ValueError
	return l*l*l
	
class TestVolume(unittest.TestCase):
	def test_volume(self):
		with self.assertRaises(ValueError):
			volume(-2)
		with self.assertRaises(TypeError):
			volume(3j)

		self.assertEqual(volume(3),27)


if __name__ == '__main__':
    unittest.main()


