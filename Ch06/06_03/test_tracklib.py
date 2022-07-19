import numpy as np
import tracklib as tl


def test_calc_distance():
    dist = tl.calc_distance(0, 0, 1, 1)
    assert np.allclose(144.17003, dist)