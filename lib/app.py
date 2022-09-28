from lib import chart, menu, request

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np 
import pandas as pd
import requests
import json
import multiprocessing 
import time

def validation(line):
    """Validate a country code is used before sending off to API"""    
 
    try:
        line[1]
    except IndexError:
        print(f"please use the following syntax: {line[0]} <country_code>\nlist of country codes : codes" )
        return False

def interpreter(line):
    """Interprets each line passed from the user and routes to next steps for the application"""

    # exit the program
    if line[0] == 'exit':
        return False
    
    # load the country code mapping
    elif line[0] == 'codes':
        
        # number labels            
        counter = 0

        # print the country codes
        country_codes = request.request_country_codes()
        
        # build dictionary based on country and country code
        for codes in country_codes[1]:
            counter += 1
            print(str(counter) + '. ' + codes['name'] + ': ' + codes['id'])

        return
    
    # available commands
    elif line[0] == 'help':
       
        try: 
            print(menu.user_help(line[1]))
        except IndexError:
            print(menu.user_help('all'))
        
        return
    
    # validate the line has a country code
    elif validation(line) == False:
        return 
    
        # execute the gdp command
    elif line[0] == 'gdp':
         
        # gross domestic product
        indicator = 'NY.GDP.MKTP.CD'
        
        # generate the chart
        chart.create_chart(line[1], indicator, '$')

        return

    elif line[0] == 'electricity':
        
        # the percentage of population with electricity                                
        indicator = '1.1_ACCESS.ELECTRICITY.TOT'
        
        # create a chart based on the data            
        chart.create_chart(line[1], indicator, '%')

        return
        
    elif line[0] == 'population':
        
        # total population
        indicator = 'SP.POP.TOTL'
        
        # create the chart            
        chart.create_chart(line[1], indicator, '')

        return

    else:
       # provide the help command
       print('try : help <command> or : help')
        
    return

