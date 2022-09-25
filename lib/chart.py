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

def create_chart(country_code, indicator, units):

    # create a dataframe based on json request
    title, df, x, y = request.load(country_code, indicator)
               
    # call the chart function to build the chart
    chart(title, x, y, units) 
    
    return

def chart(title, x, y, units):
    """Create a basic chart using x and y columns"""

    # instantiating a class     
    fig, ax = plt.subplots()
    
    # plot
    ax.plot(x, y)
    ax.set_xticks(np.arange(min(x), max(x), 10))

    # units
    if units == '$':
        ax.yaxis.set_major_formatter(currency)
    elif units == '%':
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
    else:
        ax.yaxis.set_major_formatter(standard)

    # plot attributes
    plt.title(title)
    plt.show()

    return

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

