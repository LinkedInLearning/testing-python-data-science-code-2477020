# Test geo.haversine using hypothesis
# - Latitudes are between -90 to 90
# - Longitudes are between -180 to 180
# - No NaN
import numpy as np
from hypothesis import given
from hypothesis.strategies import floats, composite

import geo


@composite
def lats(draw):
    return draw(floats(min_value=-90, max_value=90, allow_nan=False))


@composite
def lngs(draw):
    return draw(floats(min_value=-180, max_value=180, allow_nan=False))


@given(lats(), lngs(), lats(), lngs())
def test_haversine_fuzz(lat1, lng1, lat2, lng2):
    dist = geo.haversine(lat1, lng1, lat2, lng2)

    if not np.isnan(dist):
        assert dist >= 0
