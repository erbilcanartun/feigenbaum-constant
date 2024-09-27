import numpy as np
import plotly.graph_objs as go
import plotly.io as pio

from utils import *
from models import *

# Parameters for the bifurcation diagram
r_min = 3.55        # Minimum r value
r_max = 3.555        # Maximum r value
num_r = 2000      # Number of r values to evaluate
num_iterations = 10000   # Number of iterations for each r
last_iterations = 1000   # Number of iterations to plot (after reaching steady state)

# Generate bifurcation data
r_output, x_values = bifurcation_diagram(r_min, r_max, num_r, num_iterations, last_iterations)

# Create a scatter plot using plotly for interactivity
trace = go.Scattergl(
    x=r_output,
    y=x_values,
    mode='markers',
    marker=dict(
        color='black',
        size=1,
        opacity=0.5),
    hovertemplate='r: %{x}<br>x: %{y}<extra></extra>',)  # Show r and x values on hover

# Set up the layout for the plot
layout = go.Layout(
    title="Interactive Bifurcation Diagram of Logistic Map",
    xaxis=dict(title="r", range=[r_min, r_max]),
    yaxis=dict(title="x", range=[0, 1]),
    showlegend=False,
    height=900,
    width=1800)

# Create the figure
fig = go.Figure(data=[trace], layout=layout)

# Display the figure
pio.show(fig)