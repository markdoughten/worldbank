from lib import chart, storage, request, forecast
from tabulate import tabulate
from matplotlib import pyplot as plt
import pandas as pd
import random

class App(storage, request, forecast):

    def separate(command):
        """Separates the original system args into the codes and the indicators"""

        commands = storage.get_commands()
        country_codes = []
        indicators = []
        i = 0
        
        # store the commands and country codes in a list and send the rest of the command back
        for item in command:
            if item in commands.keys():
                indicators.append(item)
            else:    
                country_codes.append(item)

        return country_codes, indicators


    def codes(command, letter=None):
        # see if a user enters a string to search the countries
        if letter:
            # request the country codes with search
            country_codes = request.country_codes(letter)

        else:
            country_codes = request.country_codes()

        return country_codes


    def user_help(commands):
        try:
            output = storage.user_help(commands[1])
        except IndexError:
            output = storage.user_help('all')

        return output.to_markdown()


    def reset(pos):
        # reset the x_pos once it hits 0
        if pos == 0:
            pos = 2
        else:
            pos -= 1

        return pos

    def display(fig, ax):

        if ax.lines:
            plt.tight_layout()
            plt.show()
            return "build sucessful"
        else:
            return "no data"

    def build(country_codes, commands):
        
        fig, height, spec = chart.chart(commands)
        y_pos = height - 1

        while y_pos >= 0:

            # the starting x_pos is the remainder after filled rows
            x_pos = len(commands) % 3
            x_pos = reset(x_pos)

            while x_pos >= 0:

                command = commands.pop(0)
                fig, ax = chart.add_window(fig, spec, y_pos, x_pos)

                # plot each country
                for country_code in country_codes:
                    
                    # create a dataframe based on json request
                    data = request.country_data(country_code, storage.get_indicator(command))

                    if data:
                       
                        if data['data']['value'].any():
                            
                            # get the units    
                            units = storage.get_units(command)     
                            
                            # forecast the dataframe skip errors
                            prediction = forecast.forecast(data['data'], 10, units)

                            # plot the axis
                            ax = chart.plot(ax, prediction, data['country_name'])

                            # set the label 
                            ax.set_title(data['units'], wrap=True)

                            # change the units 
                            ax = chart.set_units(ax, units)

                            # show legend
                            ax.legend()

                        else:
                            pass
                        
     
                x_pos -= 1

            # count the subplots        
            y_pos -= 1
        
        return display(fig, ax)
        
    def interpreter(country_codes, commands):
        """Interprets each line passed from the user and routes to next steps for the application"""

        if not commands:
            return 'try: python main.py help'
        
        # available commands
        elif commands[0] == 'help':
            return user_help(commands)
        
        # load the country code mapping
        elif commands[0] == 'countries':
            if len(country_codes) > 0:
                return codes(commands, country_codes[0])
            else:
                return codes(commands)
        
        # search the commands for the indicator
        else:
            return build(country_codes, commands)

    def app(sys):
        
        # separate into country codes and commands
        country_codes, commands = separate(sys.argv)

        # create a process and submit the line to the interpreter
        return interpreter(country_codes, commands)
