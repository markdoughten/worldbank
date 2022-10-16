from lib import chart, menu, request
from tabulate import tabulate
from pprint import pprint

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np 
import pandas as pd
import requests
import json
import multiprocessing 
import time


def get_commands():
    """Return the commands available with the indicators programmed"""
    
    # a list of all the commands currently available
    commands = {
        'codes': {'description': 'return the country to country code mapping'}, 
        'gdp': {'indicator': 'NY.GDP.MKTP.CD', 'syntax': '<country code> gdp', 'units': '$', 'description': 'return the target country\'s recorded gdp per year (USD)'}, 
        'electricity': {'indicator': '1.1_ACCESS.ELECTRICITY.TOT','syntax': '<country code> electricity ', 'units': '%', 'description': 'return the target country\'s recorded electriciy access as percent of population'}, 
        'population': {'indicator': 'SP.POP.TOTL','syntax': '<country code> population', 'description': 'return the target country\'s recorded population'}, 
        'land': {'indicator': 'SP.POP.TOTL','syntax': '<country code> land', 'units': '%', 'description': 'return the target country\'s % land dedicated to agriculture'}, 
        'exit': {'description': 'exit the program'}
        }

    return commands

def generate_pairs(command):
    """Returns the pairs passed through the command line"""
    
    country_code = command.pop(0)
    pairs = []
    
    for code in command:
        pairs.append([country_code, code])

    return pairs


def validation(pair):
    """Validate a country code is used before sending off to API"""    
    
    commands = get_commands()    

    if pair[0] in commands:
        print('try: ' + {commands[pair[0]]['syntax']})
        return False
    else:
        return True
    
def interpreter(pair):
    """Interprets each line passed from the user and routes to next steps for the application"""

    commands = get_commands()
   
    # load the country code mapping
    if pair[0] == 'codes':
       
        # request the country codes
        country_codes = request.country_codes()
       
        print(tabulate(country_codes, headers='keys', showindex=False))        
    
        return
   
    # available commands
    elif pair[0] == 'help':
       
        try: 
            pprint(menu.user_help(pair[1]))
        except IndexError:
            pprint(menu.user_help('all'))
        
        return
    
    # validate the line has a country code
    elif validation(pair) == False:
        return 
    
    # search the commands for the indicator
    elif pair[1] in commands:
        
        # get the list
        indicator = commands[pair[1]]['indicator']
        
        # handle no indicator    
        try:
            units = commands[pair[1]]['units']
        except KeyError:
            units = ''
            
        # generate the chart
        chart.create_chart(pair[0], indicator, units)

    else:
       # provide the help command
       print('try : help <command> or : help')
        
    return

