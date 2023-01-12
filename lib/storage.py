# customer libraries
from lib import app, chart, request 

# builtin libraries
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
        'codes': {'description': 'country codes'}, 
        'help': {'description': 'programmed commands'}, 
        'gdp': {'indicator': 'NY.GDP.MKTP.CD', 'syntax': '<country code> gdp', 'units': '$', 'description': 'a country\'s recorded gdp per year (USD)'}, 
        'electricity': {'indicator': '1.1_ACCESS.ELECTRICITY.TOT','syntax': '<country code> electricity ', 'units': '%', 'description': 'a country\'s recorded electriciy access as percent of population'}, 
        'population': {'indicator': 'SP.POP.TOTL','syntax': '<country code> population', 'description': 'a country\'s recorded population'}, 
        'land': {'indicator': 'AG.LND.AGRI.ZS','syntax': '<country code> land', 'units': '%', 'description': 'a country\'s % land dedicated to agriculture'}, 
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

def menu(commands, sort_by='indicator'):

    df = pd.DataFrame.from_dict(commands, 'index').fillna("")
    df.index.name = 'commands'
    df.sort_values(sort_by, ascending=False, inplace=True)
    
    return df.to_markdown()

def user_help(request='all'):
    """Return the commands to the user"""
    
    commands = get_commands()
        
    if request != 'all':
        commands = commands[request]

    return menu(commands)


