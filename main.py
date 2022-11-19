# customer libraries
from lib import app, chart, menu, request 

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
        
        if len(sys.argv) == 1:
            pairs = [sys.argv]
        else:
            pairs = app.seperate(sys.argv)

        # create a process and submit the line to the interpreter
        app.interpreter(pairs)
        
    else:
        print('syntax: python main.py <country_code> <indicator>')
        exit()
 
if __name__ == '__main__':
    main()
