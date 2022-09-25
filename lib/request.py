# customer libraries
from lib import app, chart, menu 

# builtin libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np 
import pandas as pd
import requests
import json
import multiprocessing 
import time

def request_data(country_code, indicator):
    """Send GET request to the Word Bank API based on URL"""
    
    url = f'https://api.worldbank.org/v2/en/country/{country_code}/indicator/{indicator}?format=json&per_page=32700'
    
    response = requests.get(url)

    return response.json()

def request_country_codes():
    """Load the country codes from the World Bank API"""
    
    # country code url    
    url = 'https://api.worldbank.org/v2/country/?format=json&page=1&per_page=2000'

    # request the World Bank API for country codes
    response = requests.get(url)
    
    return response.json() 

def load(country_code, indicator):
    """Send GET request to the Word Bank API based on URL"""
        
    # set variables
    x = []
    y = []
        
    # send a request to the API with the indicator
    dataset = request_data(country_code, indicator)
    
    # store the data
    for data in dataset[1]:

        # store the x values
        x.append(int(data['date']))
        
        # store the y values
        y.append(data['value'])
    
    # reverse the list data
    x.reverse()
    y.reverse()

    # get the units
    units = dataset[1][0]['indicator']['value']

    # get the country
    country = dataset[1][0]['country']['value']
    
    # create a dataframe based on json
    df = pd.DataFrame({'date': x, 'value': y})   
    
    # generate the title
    title =  country + " - " + units       
    
    return title, df, x, y

