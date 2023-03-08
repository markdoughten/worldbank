# customer libraries
from lib import app, chart, storage 

# builtin libraries
import numpy as np 
import pandas as pd
import requests
import json

class Request:
    
    base_url = 'https://api.worldbank.org/v2/'
    
    def get_url(self, country_code, indicator):
        
        url = f'{self.base_url}country/en/{country_code}/indicator/{indicator}?format=json&per_page=32700'
        
        return url

    def get_data(self, url):
        """Send GET request to the Word Bank API based on URL"""
         
        try:
            response = requests.get(url).json()
        except:
            return None

        if response[0]['total'] == 0:
            return None 

        return response

    def country_data(self, country_code, indicator):
        """Send GET request to the Word Bank API based on URL"""
            
        # set variables
        x = []
        y = []
        url = ''

        # send a request to the API with the indicator
        url = get_url(country_code, indicator)
        
        # request country data
        dataset = get_data(url)
       
        if dataset: 
            
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
            country_name = dataset[1][0]['country']['value']
            
            # create a dataframe based on json
            df = pd.DataFrame({'date': x, 'value': y})   
            
            return {'country_name': country_name, 'units': units, 'data': df}

        return None

    def country_codes(self, character=None):
        
        # request data
        country_codes = get_data(f'{self.base_url}/country/?format=json&page=1&per_page=2000')
        
        # store the values in a list for the df
        country = []
        codes = []
     
        # store the country and country code
        if country_codes:
            for code in country_codes[1]:
                country.append(code['name'])
                codes.append(code['id'])
            
            # create a dataframe based on json
            df = pd.DataFrame({'country': country}, index=codes)
            df.index.name = 'code'
            df.index = df.index.str.lower()
            
            # filter the df based on the user's request
            if character:
                df = df[df['country'].str.lower().str.startswith((character.lower()))]
            
            if df.empty:
                return f"no countries start with {character.lower()}"
        
            return df.to_markdown()
        else:
            return "countries codes not available at the moment"

