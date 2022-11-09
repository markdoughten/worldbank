# customer libraries
from lib import app, chart, menu, request 

# builtin libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np 
import pandas as pd
import requests
import json
import multiprocessing 
import time

def create_chart(country_code, commands):
    
    fig, axs = plt.subplots(1, len(commands), figsize=(15, 5))
    i = 0

    for command in commands:
        
        # create a dataframe based on json request
        country, title, df, x, y = request.country_data(country_code, app.get_indicator(command))
        
        # call the chart function to build the chart
        axs[i] = chart(title, x, y, axs[i])
    
        # set the title
        axs[i].set_title(title)

        # format the y-axis
        axs[i] = set_units(axs[i], app.get_units(command)) 
        
        # count the subplots        
        i += 1
    
    fig.suptitle(country)
    plt.show()
     
    return

def chart(title, x, y, ax):
    """Create a basic chart using x and y columns"""

    # plot
    ax.plot(x, y)
    ax.set_xticks(np.arange(min(x), max(x), int((max(x)-min(x))/5)))

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

