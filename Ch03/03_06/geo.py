import numpy as np

earth_radius_km = 6373


def haversine(lat1, lng1, lat2, lng2):
    """Return distance in km between two coordinates."""
    phi1 = np.deg2rad(90 - lat1)
    phi2 = np.deg2rad(90 - lat2)

    theta1 = np.deg2rad(lng1)
    theta2 = np.deg2rad(lng2)

    cos = (np.sin(phi1) * np.sin(phi2) * np.cos(theta1 - theta2) +
           np.cos(phi1) * np.cos(phi2))
    arc = np.arccos(cos)
    return arc * earth_radius_km
