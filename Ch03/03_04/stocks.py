def max_drop(stocks):
    """Return max drop per stocks.

    stocks is a data frame with symbol, high, low.
    """
    df = stocks.copy()
    df['diff'] = df['high'] - df['low']
    return df.groupby('symbol')['diff'].max()