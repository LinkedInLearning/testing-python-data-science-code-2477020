import pandas as pd
import pandera as pa

metrics_schema = pa.DataFrameSchema({
    'time': pa.Column(pd.DatetimeTZDtype('ns', 'UTC')),
    'metric': pa.Column(pa.String, checks=pa.Check.isin({'cpu', 'mem'})),
    'value': pa.Column(pa.Float, checks=pa.Check.greater_than(0)),
})


@pa.check_output(metrics_schema)
def load_metrics(jsonl_file):
    return pd.read_json(
        jsonl_file,
        orient='records',
        lines=True,
        convert_dates=['time'],
    )


# testing
if __name__ == '__main__':
    from pathlib import Path

    here = Path(__file__).absolute().parent
    jsonl_file = here / 'metrics.jsonl'

    load_metrics(jsonl_file)
