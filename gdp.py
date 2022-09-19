import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np 
import pandas as pd
import requests
import json
import multiprocessing 
import time

def chart(title, x, y, units):
    """Create a basic chart using x and y columns"""

    # instantiating a class     
    fig, ax = plt.subplots()
    
    # plot
    ax.plot(x, y)
    ax.set_xticks(np.arange(min(x), max(x), 10))

    # units
    if units == '$':
        ax.yaxis.set_major_formatter(currency)
    elif units == '%':
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
    else:
        ax.yaxis.set_major_formatter(standard)

    # plot attributes
    plt.title(title)
    plt.show()

    return

def currency(x, pos):
    """Format the currency values for the chart"""
    
    if x >= 1e12:    
        x = '${:1.1f}T'.format(x*1e-12)
    elif x >= 1e9:
        x = '${:1.1f}B'.format(x*1e-9)
    else:
        x = '${:1.1f}M'.format(x*1e-6)
    return x

def standard(x, pos):
    """Format regular values"""
    
    if x >= 1e9:    
        x = '{:1.1f}B'.format(x*1e-9)
    else:
        x = '{:1.1f}M'.format(x*1e-6)
    return x

def prompt():
    """Print a message on startup to the user"""
    
    # print a welcome message to the console for the user
    welcome = "welcome to the country lookup tool\n"

    # a basic description about the application
    description = "an application for visualizing specific country data"

    return welcome + description
      
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
    
    if line[0] != 'exit':
        return line
    else:
        return None

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

def create_chart(country_code, indicator, units):

    # create a dataframe based on json request
    title, df, x, y = load(country_code, indicator)
               
    # call the chart function to build the chart
    chart(title, x, y, units) 
    
    return

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
        country_codes = request_country_codes()
        
        # build dictionary based on country and country code
        for codes in country_codes[1]:
            counter += 1
            print(str(counter) + '. ' + codes['name'] + ': ' + codes['id'])

        return
    
    # available commands
    elif line[0] == 'help':
       
        try: 
            print(user_help(line[1]))
        except IndexError:
            print(user_help('all'))
        
        return
    
    # validate the line has a country code
    elif validation(line) == False:
        return 
    
        # execute the gdp command
    elif line[0] == 'gdp':
         
        # gross domestic product
        indicator = 'NY.GDP.MKTP.CD'
        
        # generate the chart
        create_chart(line[1], indicator, '$')

        return

    elif line[0] == 'electricity':
        
        # the percentage of population with electricity                                
        indicator = '1.1_ACCESS.ELECTRICITY.TOT'
        
        # create a chart based on the data            
        create_chart(line[1], indicator, '%')

        return
        
    elif line[0] == 'population':
        
        # total population
        indicator = 'SP.POP.TOTL'
        
        # create the chart            
        create_chart(line[1], indicator, '')

        return

    else:
       # provide the help command
       print('try : help <command> or : help')
        
    return

def main():
    
    # record the created processes       
    processes = []

    # print prompt
    # print(prompt())
    
    while True: 
        
        # load queue
        line = get_line()
        
        # exit the program and join processes 
        if line is None:
           for p in processes:
               p.join()
               p.close() 
           exit()
        
        # create a process and submit the line to the interpreter
        p = multiprocessing.Process(target=interpreter, args=(line,))
        processes.append(p)
        p.start()
        
        # hang main so chart can get produced 
        time.sleep(2)
 
if __name__ == '__main__':
    main()
