import numpy as np
import pandas as pd

lat_km = 92
lng_km = 111


def load_csv(csv_file):
    """Load track data from CSV file."""
    return pd.read_csv(csv_file, parse_dates=['time'])


def calc_distance(lat1, lng1, lat2, lng2):
    """Return Euclidean distance in kilometers."""
    delta_lat = (lat1 - lat2) * lat_km
    delta_lng = (lng1 - lng2) * lng_km
    return np.hypot(delta_lat, delta_lng)


def running_speed(df):
    """Calculate running speed."""
    lat1, lat2 = df['lat'], df['lat'].shift()
    lng1, lng2 = df['lng'], df['lng'].shift()
    dist_km = calc_distance(lat1, lng1, lat2, lng2)
    duration = df['time'].diff()
    duration_hours = duration / pd.Timedelta(hours=1)
    return dist_km / duration_hours