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

    for parameter in parameter_values:

        series = generate_series(f, parameter, x0, int(series_length))[-int(N * .1):]
        unique_count = np.unique(series.round(decimals=int(-np.log10(round_tolerance)))).size

        if prev_unique_count is not None and unique_count != prev_unique_count:
            bifurcations.append(parameter)

        prev_unique_count = unique_count

    return bifurcations

def bifurcation_diagram(r_min, r_max, num_r, num_iterations, last_iterations):
    # Generate r values
    r_values = np.linspace(r_min, r_max, num_r)
    
    # Prepare an empty list to hold r and x values
    x_values = []
    r_output = []
    
    # Iterate over each r value
    for r in r_values:
        # Start with a random initial x value
        x = np.random.random()
        
        # Iterate the logistic map
        for i in range(num_iterations):
            x = logistic_map(r, x)
            # Store only the last 'last_iterations' iterations for the diagram
            if i >= (num_iterations - last_iterations):
                r_output.append(r)
                x_values.append(x)
    
    return r_output, x_values

def feigenbaum_constant(lst):
    if len(lst) < 3:
        raise ValueError("List must contain at least three elements.")
    
    ratios = []
    for i in range(len(lst) - 2):
        diff1 = lst[i+1] - lst[i]
        diff2 = lst[i+2] - lst[i+1]
        
        if diff2 == 0:
            ratios.append(None)  # Avoid division by zero
        else:
            ratios.append(diff1 / diff2)
    
    return ratios
    