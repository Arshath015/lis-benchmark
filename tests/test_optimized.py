import pytest
from implementations.optimized import OptimizedLIS

@pytest.fixture
def alg():
    return OptimizedLIS()

def test_empty(alg):
    assert alg.compute([]) == 0

def test_simple(alg):
    seq = [3, 1, 2, 1, 8]
    assert alg.compute(seq) == 3

def test_all_descending(alg):
    seq = [5,4,3,2,1]
    assert alg.compute(seq) == 1
