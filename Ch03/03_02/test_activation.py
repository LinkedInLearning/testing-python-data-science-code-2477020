import activation
from hypothesis import given
from hypothesis.strategies import floats
import numpy as np


@given(floats())
def test_relu(n):
    print(n)
    v = activation.relu(n)
    if not np.isnan(n):
        assert v >= 0
