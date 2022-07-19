import numpy as np

v = np.array([0.1, np.nan, 1.1])
n = 1.1
expected = np.array([0.11, np.nan, 1.21])
out = v * n 
out == expected

out

np.allclose(expected, out)