from hypothesis import given
from hypothesis.extra.pandas import column, data_frames
from hypothesis.strategies import floats, from_regex
from stocks import max_drop

strategy = data_frames([
    column('symbol', elements=from_regex(r'[A-Z]{2,7}', fullmatch=True)),
    column('high', elements=floats(min_value=1, max_value=10_000)),
    column('low', elements=floats(min_value=1, max_value=10_000)),
])


@given(strategy)
def test_max_drop(df):
    out = max_drop(df)
    unknown = set(out.index) - set(df['symbol'])
    assert not unknown
