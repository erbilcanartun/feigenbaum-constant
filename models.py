import numpy as np
import mpmath as mp

class mpfDataType:

    def __init__(self, mpf_dtype):
        global mpf
        mpf = mpf_dtype

def logistic_map(r, x):

    if mpf:
        r = mp.mpf(r)
        x = mp.mpf(x)

    return r * x * (1 - x)