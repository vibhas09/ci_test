import cal

class TestCal:
	def test_addn(self):
		assert 4 == cal.add(2,2)
		assert 5 == cal.add(2,4)
