import numpy as np
import mpmath as mp

def array_round(series, decimal_precision):

    series_ = []
    for x in series:
        
        x_ = mp.mpf(mp.nstr(x, decimal_precision))
        series_.append(x_)

    return np.array(series_)

def logistic_map(r, x):
    r = mp.mpf(r)
    x = mp.mpf(x)
    
    return r * x * (1 - x)

def generate_series(r, x0, length):

    x = x0
    series = []
    
    for i in range(length):
        x = logistic_map(r, x)
        series.append(x)

    return np.array(series)

def find_bifurcation_points(parameter_range, length=int(1e7), tolerance=1e-8):

    bifurcations = []
    prev_unique_count = None

    #parameter_values = np.arange(*parameter_range, step)
    parameter_values = np.linspace(*parameter_range, 10000)

    for parameter in parameter_values:
        
        series = generate_series(parameter, length)[-1000:]
        unique_count = np.unique(series.round(decimals=int(-np.log10(tolerance)))).size

        if prev_unique_count is not None and unique_count != prev_unique_count:
            bifurcations.append(parameter)

        prev_unique_count = unique_count

    return bifurcations