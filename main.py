# customer libraries
from lib import app, chart, storage, request 

# builtin libraries
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np 
import pandas as pd
import requests
import json
import multiprocessing 
import time
import sys

def main():
    
    # record the created processes       
    processes = []
    
    if len(sys.argv) >= 2:
        
        # remove the file name
        sys.argv.pop(0)
      
        # send command to app
        return print(app.app(sys))
        
    else:
        
        return print('syntax: python main.py <country_code> <indicator>')
 
if __name__ == '__main__':
    main()
