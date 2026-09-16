import pytest
from implementations.naive import NaiveLIS

@pytest.fixture
def alg():
    return NaiveLIS()

def test_empty(alg):
    assert alg.compute([]) == 0

def test_simple(alg):
    seq = [3, 1, 2, 1, 8]
    assert alg.compute(seq) == 3  # LIS: [1,2,8]

def test_all_descending(alg):
    seq = [5,4,3,2,1]
    assert alg.compute(seq) == 1
