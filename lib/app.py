from lib import chart, menu, request

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np 
import pandas as pd
import requests
import json
import multiprocessing 
import time

def generate_pairs(command):
    """Returns the pairs passed through the command line"""
    
    country_code = command.pop(0)
    pairs = []
    
    for code in command:
        pairs.append([country_code, code])

    return pairs


def validation(pair):
    """Validate a country code is used before sending off to API"""    
 
    try:
        pair[1]
    except IndexError:
        print(f"please use the following syntax: {pair[0]} <country_code>\nlist of country codes : codes" )
        return False

def interpreter(pair):
    """Interprets each line passed from the user and routes to next steps for the application"""
    
    # load the country code mapping
    if pair[0] == 'codes':
       
        # request the country codes
        country_codes = request.country_codes()

        return country_codes
    
    # available commands
    elif pair[0] == 'help':
       
        try: 
            print(menu.user_help(pair[1]))
        except IndexError:
            print(menu.user_help('all'))
        
        return
    
    # validate the line has a country code
    elif validation(pair) == False:
        return 
    
    # execute the gdp command
    elif pair[1] == 'gdp':
         
        # gross domestic product
        indicator = 'NY.GDP.MKTP.CD'
        
        # generate the chart
        chart.create_chart(pair[0], indicator, '$')

        return

    elif pair[1] == 'electricity':
        
        # the percentage of population with electricity                                
        indicator = '1.1_ACCESS.ELECTRICITY.TOT'
        
        # create a chart based on the data            
        chart.create_chart(pair[0], indicator, '%')

        return
        
    elif pair[1] == 'population':
        
        # total population
        indicator = 'SP.POP.TOTL'
        
        # create the chart            
        chart.create_chart(pair[0], indicator, '')

        return

    else:
       # provide the help command
       print('try : help <command> or : help')
        
    return

