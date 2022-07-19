import numpy as np
from freq import first_digit_freq
from hypothesis import given
from hypothesis.extra.numpy import arrays
from hypothesis.strategies import integers

strategy = arrays(
    dtype=np.int64,
    shape=integers(min_value=1, max_value=10_000),
    elements=integers(min_value=0, max_value=np.iinfo(np.int64).max-1),
)

@given(strategy)
def test_freq(values):
    freqs = first_digit_freq(values)
    assert freqs.shape == (10,)
    assert ((freqs>=0) & (freqs<=1)).all()
    assert np.allclose(freqs.sum(), 1)
