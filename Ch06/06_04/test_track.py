from pathlib import Path

import numpy as np
from testbook import testbook

here = Path(__file__).absolute().parent
ipynb = here / 'track.ipynb'

@testbook(ipynb, execute=True)
def test_distance(tb):
    calc_distance = tb.ref('calc_distance')
    dist = calc_distance(0, 0, 1, 1)
    assert np.allclose(144.17003, dist)