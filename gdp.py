import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import requests
import json

def chart(title, df, x, y):
    """Create a basic chart using x and y columns"""

    # instantiating a class     
    fig, ax = plt.subplots()
    
    # plot
    plt.title(title)
    ax.plot(x, y) 
    plt.show()

    return

def print_prompt():
    """Print a message on startup to the user"""
    
    # print a welcome message to the console for the user
    welcome = "welcome to the gdp tool!\n"

    # a basic description about the application
    description = "an application that allows users to look up countries based on code to see change in gdp"

    # a could syntax examples
    examples = "example commands:\n" + ":gdp slb\n" + ":exit\n" + ":help"
    
    return welcome + description + examples
 
def get_line():
    """Record input from the user"""
    
    # print : and get input from the user
    line = input(': ')
    tokenized = line.split()

    return tokenized

def user_help():
    """Return the commands to the user"""
    
    # a list of all the commands currently available
    built_in = {'dictionary': 'return the country to country code mapping', 'gdp': 'gdp <country code>', 'exit': 'exit the program'}
    
    return built_in

def request():
    """Send GET request to the Word Bank API based on URL"""
    
    url = 'https://prices.runescape.wiki/api/v1/osrs'

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'  # This is another valid field
    }

    response = requests.get(url, headers=headers)

    return response


def load_gdp(country_code):
    """Send GET request to the Word Bank API based on URL"""
        
    # set variables
    x = []
    y = []
        
    # load the Solomon Islands GDP json
    gdp = load_json('solomon-islands.json')
    
    # store the data
    for data in gdp[1]:

        # each data point in the set
        for key in data:
            
            # store the x values
            x.append(key['data'])
            
            # store the y values
            y.append(key['value'])


    # get the units
    units = gdp[1][1]['indicator']['value']

    # get the country
    country = gdp[1][1]['country']['value']
    
    # generate the title
    title =  country + " - " + units 
    
    # call the chart function to build the chart
    chart(title, df, x, y)       
    
    return 

def load_country_codes():

    # load JSON file
    country_codes = load_json('dictionary.json')

    # build dictionary based on country and country code
    for codes in country_codes[1]:
        for key in codes:
            print(key['name'], key['id'])
           
    return 

def load_json(file):
    
    # open the file
    f = open(file)
    
    # load the json data
    data = json.load(f)

    # close the file
    f.close()
    
    # return data
    return data

if __name__ == '__main__':
    
    # start the loop for the user
    while True:
        
        # print prompt to the user
        print_prompt()

        # get the input from the user
        line = get_line()
        
        # print the avaiable commands
        if line[0] == 'help':
            user_help()

        # execute the gdp command
        elif line[0] == 'gdp':
            gdp(upper(string[1]))
        
        # exit the program
        elif line[0] == 'exit':
            False
        
        # provide the help command
        else:
            print('try: help')
