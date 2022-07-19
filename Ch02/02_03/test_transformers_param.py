import numpy as np
import pytest
import transformers as tr

v = np.array([0.1, 1.0, 1.1])
scale_cases = [
    # v, cutoff, factor, expected
    [v, 1, 1.1, [0.1, 1.1, 1.21]],
    [v, v.max() + 1, 0, v],
    # ...
]


@pytest.mark.parametrize('v, cutoff, factor, expected', scale_cases)
def test_scale_many(v, cutoff, factor, expected):
    out = tr.scale(v, cutoff, factor)

    assert np.allclose(expected, out)
