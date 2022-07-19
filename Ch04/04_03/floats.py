import numpy as np
import pandas as pd

# Floating points are inexact
0.1 + 0.1

# NaN is ... interesting
np.nan == np.nan

# To ∞ and beyond
np.inf > np.inf - 1

# NaN functions
v = np.array([1.1, np.nan, 3.3])
v.sum()

s = pd.Series(v)
s.sum()

# Float info
np.finfo(np.float64)
