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

def get_line():
    """Record input from the user"""
    
    # print : and get input from the user       
    try:
        line = input(': ')
    except:
        print('EOF')

    line = line.split()
    
    # convert to lower case
    line = [x.lower() for x in line]
    
    if line[0] != 'exit' or line[0] != '':
        return line
    else:
        return None

def prompt():
    """Print a message on startup to the user"""
    
    # print a welcome message to the console for the user
    welcome = "welcome to the country lookup tool\n"

    # a basic description about the application
    description = "an application for visualizing specific country data"

    return welcome + description
      

def user_help(request='all'):
    """Return the commands to the user"""
    
    # a list of all the commands currently available
    commands = {
        'codes': {'description': 'return the country to country code mapping'}, 
        'gdp': {'syntax': 'gdp <country code>', 'description': 'return the target country\'s recorded gdp per year(USD)'}, 
        'electricity': {'syntax': 'electricity <country code>', 'description': 'return the target country\'s recorded electriciy access as percent of population'}, 
        'population': {'syntax': 'population <country code>', 'description': 'return the target country\'s recorded population'}, 
        'exit': {'description': 'exit the program'}
        }

    if request == 'all':
        return commands
    else:
        # the specific description and syntax
        return commands[request]

