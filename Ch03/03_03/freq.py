import numpy as np


def first_digit(n):
    return str(n)[0]


def first_digit_freq(values):
    """Return frequency of first digits in values.
    
    >>> first_digit_freq([18, 19, 20, 21, 22])
    array([0. , 0.4, 0.6, 0. , 0. , 0. , 0. , 0. , 0. , 0. ])
    """
    firsts = [first_digit(n) for n in values]
    freqs = np.bincount(firsts, minlength=10)
    return freqs / len(values)