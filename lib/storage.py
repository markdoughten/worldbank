# builtin libraries
import pandas as pd


def get_commands():
    """Return the commands available with the indicators programmed"""

    # a list of all the commands currently available
    commands = {
        'countries': {'description': 'country codes', 'syntax': 'countries <letter>'},
        'help': {'description': 'programmed commands', 'syntax': 'help <command>'},
        'gdp': {'indicator': 'NY.GDP.MKTP.CD', 'syntax': 'gdp <country_code>', 'units': '$',
                'description': 'gross domestic product'},
        'electricity': {'indicator': '1.1_ACCESS.ELECTRICITY.TOT', 'syntax': 'electricity <country_code>',
                        'units': '%', 'description': 'electricity access'},
        'population': {'indicator': 'SP.POP.TOTL', 'syntax': 'population <country code>',
                       'description': 'population size'},
        'land': {'indicator': 'AG.LND.AGRI.ZS', 'syntax': 'land <country code>', 'units': '%',
                 'description': 'land for agriculture'},
        'export':{'indicator': 'NE.EXP.GNFS.CD', 'syntax': 'export <country_code>', 'units': '$',
                'description': 'goods and services exported'},
        'import':{'indicator': 'NE.IMP.GNFS.CD', 'syntax': 'import <country_code>', 'units': '$',
                'description': 'goods and services imported'},
        'internet':{'indicator': 'IT.NET.BBND', 'syntax': 'internet <country_code>', 'units': '',
                'description': 'broadband subscriptions'},
        'unemployment':{'indicator': 'SL.UEM.TOTL.NE.ZS', 'syntax': 'unemployment <country_code>', 'units': '%',
                'description': 'unemployed seeking employment'}

    }

    return commands


def get_indicator(command):
    # load the commands
    commands = get_commands()

    # handle no command
    try:
        indicator = commands[command]['indicator']
    except KeyError:
        indicator = ''

    return indicator


def get_units(indicator):
    # load the commands
    commands = get_commands()

    # handle no indicator    
    try:
        units = commands[indicator]['units']
    except KeyError:
        units = ''

    return units


def user_help(request='all', sort_by='command'):
    """Return the commands to the user"""

    df = pd.DataFrame.from_dict(get_commands(), 'index').fillna("")
    df.index.name = 'command'
    df.drop('indicator', axis=1, inplace=True)

    if request == 'all':
        df.sort_values(sort_by, inplace=True)
    else:
        if request in df.index:
            df = df.filter(like=request, axis=0)

    return df
