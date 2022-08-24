import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def chart(title, df, x, y):
    """Create a basic chart using x and y columns"""

    # instantiating a class     
    fig, ax = plt.subplots()
    
    # plot
    plt.title(title)
    ax.plot(x, y) 
    plt.show()
    
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

