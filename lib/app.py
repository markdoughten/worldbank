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
        'help': {'description': 'return the programmed commands'}, 
        'gdp': {'indicator': 'NY.GDP.MKTP.CD', 'syntax': '<country code> gdp', 'units': '$', 'description': 'return the target country\'s recorded gdp per year (USD)'}, 
        'electricity': {'indicator': '1.1_ACCESS.ELECTRICITY.TOT','syntax': '<country code> electricity ', 'units': '%', 'description': 'return the target country\'s recorded electriciy access as percent of population'}, 
        'population': {'indicator': 'SP.POP.TOTL','syntax': '<country code> population', 'description': 'return the target country\'s recorded population'}, 
        'land': {'indicator': 'AG.LND.AGRI.ZS','syntax': '<country code> land', 'units': '%', 'description': 'return the target country\'s % land dedicated to agriculture'}, 
        'exit': {'description': 'exit the program'}
        }

    return commands

def get_indicator(command):

    # load the commands
    commands = get_commands()
    
     # handle no command    
    try:
        indicator = commands[command]['indicator']
    except KeyError:
        indicator = ''

    return indicator 

def get_units(indicator):
   
    # load the commands 
    commands = get_commands()

    # handle no indicator    
    try:
        units = commands[indicator]['units']
    except KeyError:
        units = ''

    return units 

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
    
    return [country_codes, command]
 
def interpreter(pair):
    """Interprets each line passed from the user and routes to next steps for the application"""

    commands = get_commands()
  
    # load the country code mapping
    if pair[1][0] == 'codes':
        
        # see if a user enters a string to search the countries
        if len(pair[1]) == 2:
            # request the country codes
            country_codes = request.country_codes(pair[1][1])
        else:
            country_codes = request.country_codes()
        
        print(tabulate(country_codes, headers='keys', showindex=False))        
    
        return
   
    # available commands
    elif pair[1][0] == 'help':
       
        try: 
            pprint(menu.user_help(pair[1][1]))
        except IndexError:
            pprint(menu.user_help('all'))
        
        return
    
    # search the commands for the indicator
    elif pair[1]:
        
        # generate the chart with country codes and commands
        chart.chart(pair[0], pair[1])

    else:
       # provide the help command
       print('try : help <command> or : help')
        
    return

