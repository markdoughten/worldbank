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

def main():
    
    # record the created processes       
    processes = []

    # print prompt
    print(menu.prompt())
    
    while True: 
        
        # load queue
        line = menu.get_line()

        # exit the program and join processes 
        if line is None:
           for p in processes:
               p.join()
               p.close() 
           exit()
        
        # create a process and submit the line to the interpreter
        p = multiprocessing.Process(target=app.interpreter, args=(line,))
        processes.append(p)
        p.start()
        
        # hang main so chart can get produced 
        time.sleep(2)
 
if __name__ == '__main__':
    main()
