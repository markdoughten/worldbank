import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import requests
import json

def chart(title, x, y):
    """Create a basic chart using x and y columns"""

    # instantiating a class     
    fig, ax = plt.subplots()
    
    # plot
    ax.plot(x, y)
    ax.set_xticks(np.arange(min(x), max(x), 5)
    
    # plot attributes
    plt.title(title)
    plt.show()

    return

def prompt():
    """Print a message on startup to the user"""
    
    # print a welcome message to the console for the user
    welcome = "welcome to the gdp tool!\n"

    # a basic description about the application
    description = "an application that allows users to look up countries\n based on code to see change in gdp\n"

    # a could syntax examples
    examples = "example commands:\n" + str(user_help())
    
    return welcome + description + examples
 
def get_line():
    """Record input from the user"""
    
    # print : and get input from the user
    line = input(': ')
    line = line.split()

    return line

def user_help():
    """Return the commands to the user"""
    
    # a list of all the commands currently available
    built_in = {'commands': [
        {'codes': {'description': 'return the country to country code mapping'}}, 
        {'gdp': {'syntax': 'gdp <country code>', 'description': 'return the country to country code mapping'}}, 
        {'exit': {'description': 'exit the program'}}]}
    
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
    gdp = load_json('./json/solomon-islands.json')
    
    # store the data
    for data in gdp[1]:

        # store the x values
        x.append(int(data['date']))
        
        # store the y values
        y.append(data['value'])
    
    # reverse the list data
    x.reverse()
    y.reverse()

    # get the units
    units = gdp[1][0]['indicator']['value']

    # get the country
    country = gdp[1][0]['country']['value']

    df = pd.DataFrame({'years': x, 'gdp': y})   
    
    # generate the title
    title =  country + " - " + units 
    
    # call the chart function to build the chart
    chart(title, x, y)       
    
    return df

def load_country_codes():

    # load JSON file
    country_codes = load_json('./json/dictionary.json')
    
    return country_codes 

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
       
        # get the input from the user
        line = get_line()

        # convert to lower case
        line = [x.lower() for x in line]
        
        if line:

            # available commands
            if line[0] == 'help':
                print(user_help())

            # execute the gdp command
            elif line[0] == 'gdp':
                load_gdp(line[1])
            
            # load the country code mapping
            elif line[0] == 'codes':
                
                # number labels            
                counter = 0

                # print the country codes
                country_codes = load_country_codes()
                
                # build dictionary based on country and country code
                for codes in country_codes[1]:
                    
                    # increment counter
                    counter += 1
                    
                    # print to the console
                    print(str(counter) + '. ' + codes['name'] + ': ' + codes['id'])
                       
            # exit the program
            elif line[0] == 'exit':
               break 
            
            # provide the help command
            else:
                print('try: help')
