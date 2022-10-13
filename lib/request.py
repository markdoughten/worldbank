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

def get_url(country_code, indicator):
    
    url = f'https://api.worldbank.org/v2/en/country/{country_code}/indicator/{indicator}?format=json&per_page=32700'
    
    return url

def get_data(url):
    """Send GET request to the Word Bank API based on URL"""
    
    response = requests.get(url)

    return response.json()

def country_data(country_code, indicator):
    """Send GET request to the Word Bank API based on URL"""
        
    # set variables
    x = []
    y = []
    url = ''

    # send a request to the API with the indicator
    url = get_url(country_code, indicator)
    
    # request country data
    dataset = get_data(url)
    
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

def country_codes():
    
    # request data
    country_codes = get_data('https://api.worldbank.org/v2/country/?format=json&page=1&per_page=2000')
    
    # store the values in a list for the df
    country = []
    codes = []
 
    # store the country and country code
    for code in country_codes[1]:
        country.append(code['name'])
        codes.append(code['id'])
    
    # create a dataframe based on json
    df = pd.DataFrame({'code': codes, 'country': country})   
    
    return df

