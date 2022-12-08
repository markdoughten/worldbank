# builtin libraries
import numpy as np 
import pandas as pd
import requests
import json
from statsmodels.tsa.arima_model import ARIMA

def forecast(df):
    
    # takes a dataframe and splits into train and test


    # returns dataframe with forecasted values
    return df

def year(df, column_name):

    df[column_name] = pd.to_datetime(df[column_name], format='%Y')

    return df

def read(path):
    
    df = pd.read_csv(path)

    return df

def divide(df):

    # 8:2 ratio on the split
    split = len(df) - int(0.2*(df))
    train, test = df['value'][0:split], df['value'][split:]
    
    return train, test

df = read('../out.csv')

print(df.head())
   
df = year(df, 'date')
    
print(df.info())

train, test = divide(df)

model = ARIMA(train.values, order=(5, 0, 2))
model_fit = model.fit(disp=False)

predictions = model_fit.predict(len(test))
test_ = pandas.DataFrame(test)
test_['predictions'] = predictions[0:1871]

plt.plot(df['value'])
plt.plot(test_.predictions)
plt.show()
