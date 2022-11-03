# customer libraries
from lib import app, chart, request 

# builtin libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np 
import pandas as pd
import requests
import json
import multiprocessing 
import time

def user_help(request='all'):
    """Return the commands to the user"""
    
    commands = app.get_commands()
        
    if request == 'all':
        return commands
    else:
        # the specific description and syntax
        return commands[request]

