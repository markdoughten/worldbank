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
    
    pass

def get_line():
    """Record input from the user"""

    line = input(': ')
    tokenized = line.split()

    return tokenized

def user_help():
    """Return the commands to the user"""
    
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
    title =   
    
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


if __name__ == "__main__":
    
    # file name
    file = 'gdp.csv'
    country = 'Solomon Islands'
    title = 'GDP (current US$) - ' + country
    
    # load data
    df = pd.read_csv(file)
    x, y = df[df.columns[0]], df[df.columns[1]]
     
    # mark chart
    chart(title, df, x, y)

if __name__ == '__main__':
    
    # start the loop for the user
    while True:
        
        # get the input from the user
        user = get_line()

        # loop through the get the response from the user
        for commands in user:

            # print the avaiable commands
            if commands[0] == 'help':
                user_help()

            # execute the gdp command
            elif commands[0] == 'gdp':
                gdp(commands[1])
            
            # exit the program
            elif commands[0] == 'exit':
                return 
            
            # provide the help command
            else:
                print('try: help')
