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

def user_help(request='all'):
    """Return the commands to the user"""
    
    commands = get_commands()
        
    if request != 'all':
        commands = commands[request]

    return commands


