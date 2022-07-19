import pandas as pd
from pandas.testing import assert_frame_equal


def test_model():
    # Calling model on data redacted
    out = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'is_fraud': [0.1, 0.97, 0.3, 0.2],
    })

    expected = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'is_fraud': [0.1, 0.972, 0.3, 0.2],
    })

    assert_frame_equal(out, expected, atol=0.01)
