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
 
    return fig, height, spec

def chart(country_codes, commands):
   
    fig, height, spec = subplots(commands)
    
    y_pos = height - 1
        
    while y_pos >= 0: 

        # the starting x_pos is the remainder after filled rows
        x_pos = len(commands) % 3
       
        # reset the x_pos once it hits 0 
        if x_pos == 0:
            x_pos = 2
        else:
            x_pos -= 1
            
        while x_pos >= 0:

            command = commands.pop(0)
            
            ax = fig.add_subplot(spec[y_pos, x_pos]) 
            
            # plot each country
            for country_code in country_codes:
            
                # create a dataframe based on json request
                data = request.country_data(country_code, storage.get_indicator(command))

                if data: 
                  
                    # set variables 
                    country, title, df = [data[i] for i in (0, 1, 2)]
                   
                    # call the chart function to build the plot
                    ax = plot(country, df['date'].values.tolist(), df['value'].values.tolist(), ax)
                    ax.set_title(title)

                    # format the y-axis
                    ax = set_units(ax, storage.get_units(command))

                    # show legend
                    ax.legend() 
    
            x_pos -= 1
            
        # count the subplots        
        y_pos -= 1
    
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

