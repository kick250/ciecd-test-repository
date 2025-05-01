import test
from src.sum_one import SumOne

def test_sum_one():
	value = 10
	described_class = SumOne()
	assert 11 == described_class.execute(value)
