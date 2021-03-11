import calculator

class TestCalculator:
	def test_add(self):
		assert 6 == calculator.add(1, 5)

	def test_subtract(self):
		assert 2 == calculator.subtract(4,2)
