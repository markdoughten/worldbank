import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import requests

def chart(title, df, x, y):
    """Create a basic chart using x and y columns"""

    # instantiating a class     
    fig, ax = plt.subplots()
    
    # plot
    plt.title(title)
    ax.plot(x, y) 
    plt.show()


def print_prompt():
    print('Welcome to the Grand Exchange')


def get_line():
    line = input(': ')
    tokenized = line.split()
    return tokenized


def user_help():
    built_in = {'help': 'list the built in commands',
                'item': 'item syntax: item <item on the grand exchange>',
                'price': 'price syntax: price <price on the grand exchange'}
    for item in built_in:
        print(built_in[item])


def request():

    # Source:
    # https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python/10606260#10606260

    url = 'https://prices.runescape.wiki/api/v1/osrs'

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'  # This is another valid field
    }

    response = requests.get(url, headers=headers)

    return response


def user_item(item):
    pass


def user_price(item):
    pass

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
    print_prompt()
    while True:
        user = get_line()
        for commands in user:
            if commands[0] == 'help':
                user_help()
            elif commands[0] == 'item':
                user_item(commands[1])
            else:
                print('Try: help')
