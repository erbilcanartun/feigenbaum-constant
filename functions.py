import numpy as np

def logistic_map(r, x):
    
    return r * x * (1 - x)

def generate_series(r, length):

    x0 = 0.4
    series = [x0]
    x = x0
    for i in range(length - 1):
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