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
        'codes': {'description': 'country codes', 'syntax': 'codes <letter>'}, 
        'help': {'description': 'programmed commands', 'syntax':'help <command>'}, 
        'gdp': {'indicator': 'NY.GDP.MKTP.CD', 'syntax': '<country code> gdp', 'units': '$', 'description': 'gross domestic product'}, 
        'electricity': {'indicator': '1.1_ACCESS.ELECTRICITY.TOT','syntax': '<country code> electricity ', 'units': '%', 'description': 'electriciy access'}, 
        'population': {'indicator': 'SP.POP.TOTL','syntax': '<country code> population', 'description': 'population size'}, 
        'land': {'indicator': 'AG.LND.AGRI.ZS','syntax': '<country code> land', 'units': '%', 'description': 'land for agriculture'}, 
        'exit': {'description': 'exit the program', 'syntax': 'exit'}
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

def user_help(request='all', sort_by='syntax'):
    """Return the commands to the user"""
    
    df = pd.DataFrame.from_dict(get_commands(), 'index').fillna("")
    df.index.name = 'command'
    df.drop('indicator', axis=1, inplace=True)
    
    if request == 'all':
        df.sort_values(sort_by, inplace=True)
    else:
        if request in df.index:
            df = df.filter(like=request, axis=0)
    
    return df.to_markdown()


