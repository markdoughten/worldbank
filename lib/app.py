from lib import chart, storage, request, forecast
from tabulate import tabulate
from matplotlib import pyplot as plt
import pandas as pd

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


def codes(command, letter):
    # see if a user enters a string to search the countries
    if letter:
        # request the country codes with search
        country_codes = request.country_codes(letter)

    else:
        country_codes = request.country_codes()

    return tabulate(country_codes, headers='keys', showindex=False)


def user_help(commands):
    try:
        output = storage.user_help(commands[1])
    except IndexError:
        output = storage.user_help('all')

    return output


def reset(pos):
    # reset the x_pos once it hits 0
    if pos == 0:
        pos = 2
    else:
        pos -= 1

    return pos


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
                country_name, units, data = request.country_data(country_code, storage.get_indicator(command))

                if data is not None:
                    
                    # forecast the dataframe
                    prediction = forecast.forecast(data)
                    
                    # plot the axis
                    ax = chart.plot(ax, prediction, country_name)

                    # set the label 
                    ax.set_title(units)

                    # change the units 
                    ax = chart.set_units(ax, storage.get_units(command))

                    # show legend
                    ax.legend()

            x_pos -= 1

        # count the subplots        
        y_pos -= 1

    plt.show()

    return "build sucessful"


def interpreter(country_codes, commands):
    """Interprets each line passed from the user and routes to next steps for the application"""

    # available commands
    if commands[0] == 'help':
        return user_help(commands)
    
    # load the country code mapping
    elif commands[0] == 'codes':
        return codes(commands, country_codes[0])

    # search the commands for the indicator
    elif commands:
        return build(country_codes, commands)

    # error output
    else:
        return 'try : help <command> or : help'


def app(sys):
    
    # separate into country codes and commands
    country_codes, commands = separate(sys.argv)

    # create a process and submit the line to the interpreter
    return interpreter(country_codes, commands)
