def scale(v, cutoff, factor):
    """Scale values above cutoff by factor"""
    v = v.copy()
    v[v>=cutoff] *= factor
    return v
