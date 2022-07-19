import numpy as np
import pandas as pd

x = 20
assert x > 10, 'x too small'

x > 10

assert x > 100, 'x too small'
x > 100

# 0 numbers are False
for n in [0, 0.0, 0+0j]:
    print(f'{n!r} -> {bool(n)}')

# Empty collections are False
for c in [(), {}, '']:
    print(f'{c!r} -> {bool(c)}')

# None is False
print(f'None -> {bool(None)}')

# False is False (doh!)
print(f'False -> {bool(False)}')

# Everything else is True
objs = ['Hi', 3.4, (5, 7), object(), np.nan]
for obj in objs:
    print(f'{obj!r} -> {bool(obj)}')


# However
v = np.array([-1, 2, 3])
assert v > 0, 'not positive'

cond = v > 0
print(cond)

cond.all()
cond.any()

s = pd.Series(v)
assert s > 0, 'not positive'