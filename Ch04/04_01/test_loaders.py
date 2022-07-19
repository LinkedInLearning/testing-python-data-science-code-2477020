from pathlib import Path

import loaders
from schema import sales_schema

here = Path(__file__).absolute().parent


def test_load_sales():
    csv_file = here / 'sales.csv'
    df = loaders.load_sales(csv_file)
    sales_schema.validate(df)
