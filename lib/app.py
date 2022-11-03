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
        'land': {'indicator': 'AG.LND.AGRI.ZS','syntax': '<country code> land', 'units': '%', 'description': 'return the target country\'s % land dedicated to agriculture'}, 
        'exit': {'description': 'exit the program'}
        }

    return commands

def generate_pairs(command):
    """Returns the pairs passed through the command line"""
    
    pairs = []
   
    country_codes, indicators = seperate(command)
    
    # creates pairs for the interpreter and combines help with first command after 
    if country_codes:
        for country_code in country_codes: 
            for indicator in indicators:
                pairs.append([country_code, indicator])
    else:
        if indicators:
            pairs.append([indicators[0], indicators[1]])

    return pairs

def seperate(command):
    """Seperates the original system args into the codes and the indicators"""

    commands = get_commands()
    country_codes = []
    
    # search the command and store the country codes in a list and send the rest of the command back
    while len(command) > 0:
        if command[0] in commands.keys():
            break
        else: 
            country_codes.append(command[0])
            command.pop(0)
    
    return country_codes, command
 
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

