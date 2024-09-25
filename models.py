import numpy as np
import mpmath as mp

def logistic_map(r, x, mpf=False):

    if mpf:
        r = mp.mpf(r)
        x = mp.mpf(x)

    return r * x * (1 - x)