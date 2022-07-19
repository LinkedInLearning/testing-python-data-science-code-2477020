from ipaddress import IPv4Address

import pandas as pd
import pandera as pa


def is_ipv4(v):
    try:
        IPv4Address(v)
        return True
    except ValueError:
        return False


sales_schema = pa.DataFrameSchema({
    'time': pa.Column(pd.Timestamp),
    'value': pa.Column(pd.Int64Dtype, checks=pa.Check.greater_than(0)),
    'ip': pa.Column(str, pa.Check(is_ipv4, element_wise=True)),
})
