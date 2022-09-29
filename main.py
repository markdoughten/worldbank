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
    
    # remove the file name
    sys.argv.pop(0)    
 
    # timer
    start = time.time()

    # create a process and submit the line to the interpreter
    p = multiprocessing.Process(target=app.interpreter, args=(sys.argv,))
    processes.append(p)
    p.start()
    
    # hang main so chart can get produced 
    time.sleep(time.time()-start)
 
if __name__ == '__main__':
    main()
