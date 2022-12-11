from lib import chart, storage, request
from tabulate import tabulate
from pprint import pprint

import numpy as np 
import pandas as pd

def seperate(command):
    """Seperates the original system args into the codes and the indicators"""

    commands = storage.get_commands()
    country_codes = []
    
    # search the command and store the country codes in a list and send the rest of the command back
    while len(command) > 0:
        if command[0] in commands.keys():
            break
        else: 
            country_codes.append(command[0])
            command.pop(0)
    
    return [country_codes, command]
 
def interpreter(pair):
    """Interprets each line passed from the user and routes to next steps for the application"""

    commands = storage.get_commands()
  
    # load the country code mapping
    if pair[1][0] == 'codes':
        
        # see if a user enters a string to search the countries
        if len(pair[1]) == 2:
            # request the country codes
            country_codes = request.country_codes(pair[1][1])
        else:
            country_codes = request.country_codes()
        
        print(tabulate(country_codes, headers='keys', showindex=False))        
    
        return
   
    # available commands
    elif pair[1][0] == 'help':
       
        try: 
            pprint(storage.user_help(pair[1][1]))
        except IndexError:
            pprint(storage.user_help('all'))
        
        return
    
    # search the commands for the indicator
    elif pair[1]:
        
        # generate the chart with country codes and commands
        chart.chart(pair[0], pair[1])

    else:
       # provide the help command
       print('try : help <command> or : help')
        
    return

