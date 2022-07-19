import pandas as pd


def load_sales(file_name):
    return pd.read_csv(file_name, parse_dates=['time'])