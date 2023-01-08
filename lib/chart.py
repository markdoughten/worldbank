# customer libraries
from lib import app, chart, storage, request 

# builtin libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.gridspec as gridspec
import numpy as np 
import pandas as pd
import math

def subplots(commands):
    
    # set the parameters
    height = math.ceil(len(commands)/3)
    width = len(commands)
   
    # adjust the width for small subplots 
    if width < 3: 
        fig = plt.figure(figsize=(width*5, height*4))
    else:
        fig = plt.figure(figsize=(15, height*4))
        width = 3
    
    # create the grid layout based on the command inputs 
    spec = gridspec.GridSpec(height, width, figure=fig)
 
    return fig, spec

def chart(country_codes, commands):
   
    fig, spec = subplots(commands)
    
    return fig, spec

def plot(country, x, y, ax):
    """Create a basic chart using x and y columns"""

    # plot
    ax.plot(x, y, label=country)
    ax.set_xticks(np.arange(min(x), max(x), int((max(x)-min(x))/5)))

    return ax

def add_axis(fig, spec, y_pos, x_pos):

    ax = fig.add_subplot(spec[y_pos, x_pos])

    return ax

def plot(ax):

    ax = plot(country, df['date'].values.tolist(), df['value'].values.tolist(), ax)
    
    return ax

def set_label(ax, country_name):
    
    ax.set_title(country_name)

    return ax

def set_units(ax, units):
 
    # units
    if units == '$':
        ax.yaxis.set_major_formatter(currency)
    elif units == '%':
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
    else:
        ax.yaxis.set_major_formatter(standard)
 
    return ax

def currency(x, pos):
    """Format the currency values for the chart"""
    
    if x >= 1e12:    
        x = '${:1.1f}T'.format(x*1e-12)
    elif x >= 1e9:
        x = '${:1.1f}B'.format(x*1e-9)
    else:
        x = '${:1.1f}M'.format(x*1e-6)
    return x

def standard(x, pos):
    """Format regular values"""
    
    if x >= 1e9:    
        x = '{:1.1f}B'.format(x*1e-9)
    else:
        x = '{:1.1f}M'.format(x*1e-6)
    return x

