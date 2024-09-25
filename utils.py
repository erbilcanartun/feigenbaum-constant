import numpy as np
import mpmath as mp
from models import *

def array_round(series, decimal_precision):

    series_ = []
    for x in series:

        x_ = mp.mpf(mp.nstr(x, decimal_precision))
        series_.append(x_)

    return np.array(series_)

def generate_series(f, fparam, x0, length):

    x = x0
    series = []

    for i in range(length):
        x = f(fparam, x)
        series.append(x)

    return np.array(series)

def find_bifurcation_points(f, fparam_range, x0, fparam_step_size=1e-4, series_length=int(1e7), round_tolerance=1e-6):

    bifurcations = []
    prev_unique_count = None

    parameter_values = np.arange(*parameter_range, fparam_step_size)
    #parameter_values = np.linspace(*fparam_range, 10000)

    for parameter in parameter_values:

        series = generate_series(f, parameter, x0, int(series_length))[-int(N * .1):]
        unique_count = np.unique(series.round(decimals=int(-np.log10(round_tolerance)))).size

        if prev_unique_count is not None and unique_count != prev_unique_count:
            bifurcations.append(parameter)

        prev_unique_count = unique_count

    return bifurcations