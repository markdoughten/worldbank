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
    ax.set_xticks(np.arange(min(x), max(x), 5))

    # units
    if units == '$':
        ax.yaxis.set_major_formatter(currency)
    elif units == '%':
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
    else:
        pass

    # plot attributes
    plt.title(title)
    plt.show()

    return

def currency(x, pos):
    """Format the currency values for the chart"""
        
    x = '${:1.1f}B'.format(x*1e-9)

    return x    

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

def user_help():
    """Return the commands to the user"""
    
    # a list of all the commands currently available
    built_in = {'commands': [
        {'codes': {'description': 'return the country to country code mapping'}}, 
        {'gdp': {'syntax': 'gdp <country code>', 'description': 'return the target country\'s recorded gdp per year(USD)'}}, 
        {'electricity': {'syntax': 'electricity <country code>', 'description': 'return the target country\'s recorded electriciy useage as percent of population'}}, 
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

def load(country_code, indicator):
    """Send GET request to the Word Bank API based on URL"""
        
    # set variables
    x = []
    y = []
        
    # send a request to the API with the indicator
    dataset = load_json(indicator)
    
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

def load_country_codes():
    """Load the country codes from the World Bank API"""

    # load JSON file
    country_codes = load_json('./json/dictionary.json')
    
    return country_codes 

def load_json(file):
    """Opens up the local json file for testing and should get replaced with request"""

    # open the file
    f = open(file)
    
    # load the json data
    data = json.load(f)

    # close the file
    f.close()
    
    # return data
    return data

def create_chart(command, indicator, units):

    # create a dataframe based on json request
    title, df, x, y = load(command, indicator)
               
    # call the chart function to build the chart
    chart(title, x, y, units) 
    
    return        

def interpreter(line):
   
    # available commands
    if line[0] == 'help':
        print(user_help())
    
    # execute the gdp command
    elif line[0] == 'gdp':
        
        # gross domestic product
        indicator = 'NY.GDP.MKTP.CD'
        indicator = './json/solomon-islands.json'
                    
        create_chart('gdp', indicator, '$')

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
    
    elif line[0] == 'electricity':
        
        # the percentage of population with electricity                                
        indicator = '1.1_ACCESS.ELECTRICITY.TOT'
        indicator = './json/electricity.json'
        
        # create a chart based on the data            
        create_chart('electricity', indicator, '%')
        
    elif line[0] == 'population':
        
        # total population
        indicator = 'NY.GDP.MKTP.CD'
        indicator = './json/population.json'
        
        # create the chart            
        create_chart('population', indicator, '')

    # exit the program
    elif line[0] == 'exit':
        return None

    else:
       # provide the help command
       print('try :help')

def main():
    
    # record the created threads       
    processes = []

    while True: 
        
        # load queue
        line = get_line()
        
        if line is None:
           for p in processes:
               p.join()
               p.close() 
           exit()
        
        # record time to wait main
        t1 = time.time() * 1000
  
        # create a process and submit the line to the interpreter
        p = multiprocessing.Process(target=interpreter, args=(line,))
        p.start()
        processes.append(p)
        
        # get the difference
        d = time.time() * 1000 - t1
        
        if 1 < (d/1000):
            time.sleep(d)
        else:
            # hang main
            time.sleep(1)       
 
if __name__ == '__main__':
    main()
