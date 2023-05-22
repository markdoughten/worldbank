from lib.chart import Chart
from lib.storage import Storage
from lib.request import Request
from lib.forecast import Forecast
from tabulate import tabulate
from matplotlib import pyplot as plt
import pandas as pd
import random

class App:

    storage = Storage()
    forecast = Forecast()
    request = Request()
    chart = Chart()   
 
    def separate(self, command):
        """Separates the original system args into the codes and the indicators"""

        commands = App.storage.commands
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


    def codes(self, command, letter=None):
        # see if a user enters a string to search the countries
        if letter:
            # request the country codes with search
            country_codes = App.request.country_codes(letter)

        else:
            country_codes = App.request.country_codes()

        return country_codes


    def user_help(self, commands):
        try:
            output = App.storage.user_help(commands[1])
        except IndexError:
            output = App.storage.user_help('all')

        return output.to_markdown()


    def reset(self, pos):
        # reset the x_pos once it hits 0
        if pos == 0:
            pos = 2
        else:
            pos -= 1

        return pos

    def display(self, fig, ax):

        if ax.lines:
            plt.tight_layout()
            plt.show()
            return "build sucessful"
        else:
            return "no data"

    def build(self, country_codes, commands):
        
        fig, height, spec = App.chart.chart(commands)
        y_pos = height - 1

        while y_pos >= 0:

            # the starting x_pos is the remainder after filled rows
            x_pos = len(commands) % 3
            x_pos = self.reset(x_pos)

            while x_pos >= 0:

                command = commands.pop(0)
                fig, ax = App.chart.add_window(fig, spec, y_pos, x_pos)

                # plot each country
                for country_code in country_codes:
                    
                    # create a dataframe based on json request
                    data = App.request.country_data(country_code, App.storage.get_indicator(command))

                    if data:
                       
                        if data['data']['value'].any():
                            
                            # get the units    
                            units = App.storage.get_units(command)     
                            
                            # forecast the dataframe skip errors
                            prediction = App.forecast.forecast(data['data'], int(len(data['data'])*.05), units)

                            # plot the axis
                            ax = App.chart.plot(ax, prediction, data['country_name'])

                            # set the label 
                            ax.set_title(data['units'], wrap=True)

                            # change the units 
                            ax = App.chart.set_units(ax, units)

                            # show legend
                            ax.legend()

                        else:
                            pass
                        
     
                x_pos -= 1

            # count the subplots        
            y_pos -= 1
        
        return self.display(fig, ax)
        
    def interpreter(self, country_codes, commands):
        """Interprets each line passed from the user and routes to next steps for the application"""

        if not commands:
            return 'try: python main.py help'
        
        # available commands
        elif commands[0] == 'help':
            return self.user_help(commands)
        
        # load the country code mapping
        elif commands[0] == 'countries':
            if len(country_codes) > 0:
                return self.codes(commands, country_codes[0])
            else:
                return self.codes(commands)
        
        # search the commands for the indicator
        else:
            return self.build(country_codes, commands)

    def app(self, sys):
        
        # separate into country codes and commands
        country_codes, commands = self.separate(sys.argv)

        # create a process and submit the line to the interpreter
        return self.interpreter(country_codes, commands)
