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
import math

def subplots(commands):

    height = math.ceil(len(commands)/3)
    
    if len(commands) < 3:
        width = len(commands)
    else:
        width = 3

    fig, axs = plt.subplots(height, width, figsize=(15, 5))

    return fig, axs, height

def chart(country_codes, commands):
   
    fig, axs, height = subplots(commands)
    
    y_pos = height - 1
        
    while y_pos >= 0: 

        x_pos = len(commands) % 3
        
        if x_pos == 0:
            x_pos = 2
            
        while x_pos >= 0:

            command = commands.pop(0)
            
            # plot each country
            for country_code in country_codes:
            
                # create a dataframe based on json request
                country, title, df, x, y = request.country_data(country_code, app.get_indicator(command))
                
                ax = axs[y_pos, x_pos]
         
                # call the chart function to build the plot
                ax = plot(country, x, y, ax)
                
                # set the title
                ax.set_title(title)

                # format the y-axis
                ax = set_units(ax, app.get_units(command))
            
            x_pos -= 1
            
        # count the subplots        
        y_pos -= 1
    
    plt.legend() 
    plt.show()
     
    return

def plot(country, x, y, ax):
    """Create a basic chart using x and y columns"""

    # plot
    ax.plot(x, y, label=country)
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

