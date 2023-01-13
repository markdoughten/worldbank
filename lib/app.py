from lib import chart, storage, request, forecast
from tabulate import tabulate
from pprint import pprint

import numpy as np 
import pandas as pd

def seperate(command):
    """Seperates the original system args into the codes and the indicators"""

    commands = storage.get_commands()
    country_codes = []
    i = 0 
    
    # store the commands and country codes in a list and send the rest of the command back
    while i < len(command):
        if command[i] not in commands.keys():
            country_codes.append(command[i])
            command.pop(i)
        i += 1    

    return country_codes, command

def codes(command):
    
    # see if a user enters a string to search the countries
    if len(command) == 2:
        
        # request the country codes with search
        country_codes = request.country_codes(command[1])
    
    else:
        country_codes = request.country_codes()       

    return tabulate(country_codes, headers='keys', showindex=False)

def user_help(commands):

    try: 
       output = storage.user_help(commands[1])
    except IndexError:
       output = storage.user_help('all')

    return output

def reset(pos):

    # reset the x_pos once it hits 0 
    if pos == 0:
        pos = 2
    else:
        pos -= 1
    
    return pos

def build(country_codes, commands):

    fig, spec = chart.chart(country_codes, commands)

    y_pos = spec._nrows - 1
        
    while y_pos >= 0: 

        # the starting x_pos is the remainder after filled rows
        x_pos = len(commands) % 3
       
        x_pos = reset(x_pos)
                    
        while x_pos >= 0:

            command = commands.pop(0)
            
            ax = chart.add_axis(fig, spec, y_pos, x_pos)
            
            # plot each country
            for country_code in country_codes:
                
                # set default to none
                data = None 
                
                # create a dataframe based on json request
                country_name, units, data = request.country_data(country_code, storage.get_indicator(command))

                if data is not None: 
                    
                    # forecast the dataframe
                    prediction = forecast.forecast(data)
                    
                    # plot the axis
                    ax = chart.plot(ax, prediction)
                    
                    # set the label 
                    ax = chart.set_label(ax, country_name)
                    
                    # change the units 
                    ax = chart.set_units(ax, units)
                   
                    # show legend
                    ax.legend() 
    
            x_pos -= 1
            
        # count the subplots        
        y_pos -= 1
    
    return fig.show()

def interpreter(country_codes, commands):
    """Interprets each line passed from the user and routes to next steps for the application"""

    # load the country code mapping
    if commands[0] == 'codes':
        return codes(commands)
   
    # available commands
    elif commands[0] == 'help':
        return user_help(commands)
           
    # search the commands for the indicator
    elif commands:
        return build(country_codes, commands)
    
    # error output
    else:
        return 'try : help <command> or : help'

def app(sys):
       
    # seperate into country codes and commands 
    country_codes, commands = seperate(sys.argv)
    
    # create a process and submit the line to the interpreter
    return interpreter(country_codes, commands)
    
    
    
    
