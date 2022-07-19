import pandas as pd


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
