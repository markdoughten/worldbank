# builtin libraries
import numpy as np 
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose

def fill_missing(values):

    return
 
def forecast(df, column_name='value'):
    
    # takes a dataframe and splits into train and test
    train, test = split(df)
    df = year(df)
    
    model = ARIMA(train.values, order=(5, 0, 2))
    model_fit = model.fit(disp=False)

    predictions = model_fit.predict(len(test))
    test_ = pandas.DataFrame(test)
    test_['predictions'] = predictions[0:1871]

    plt.plot(df[column_name])
    plt.plot(test_.predictions)
    plt.show()

    # returns dataframe with forecasted values
    return df

def year(df, column_name='date'):

    df[column_name] = pd.to_datetime(df[column_name], format='%Y')

    return df

def read(path):
    
    df = pd.read_csv(path)

    return df

def split(df, column_name='value'):

    # 8:2 ratio on the split
    split = len(df) - int(0.2*(df))
    train, test = df[column_name][0:split], df[column_name][split:]
    
    return train, test

def pacf(df, column_name='value'):

    plot_pacf(df[column_name])
    plt.show()

    return


def acf(df, column_name='value'):

    plot_acf(df[column_name])
    plt.show()

    return

def decomposition(df, column_name='value', model='multiplicative'):
    
    # show the decomposition
    result = seasonal_decompose(df, model=model)
    result.plot()
    plt.show()
    
    return

def error(actual, forecast):
    
    # compare test forecast to actuals
    error = actual - forecast
    
    
    ME = sum(error)*1.0/len(actual)
    MAE = sum(abs(error))*1.0/len(actual)
    MSE = sum(error**2)*1.0/len(actual)
   
    PE = (error/actual)*100    
    MPE = sum(error)/len(forecast)
    MAE = sum(abs(error))len(forecast)

    print('Summary of errors resulting from actuals & forecast:')
    
    results = {'Errors': ['ME', 'MAE', 'MSE', 'MPE', 'MAPE'], 'Value': [ME, MAE, PE, MPE, MAE]}

    output = pd.DataFrame(results, columns=['Errors', 'Value'])

    print(output)       
    
    return output

def naive():
    
    # generate a basic naive forecast

    return     


df = read('../docs/out.csv')

acf(df)
pacf(df)

df = pd.read_csv('../docs/out.csv', parse_dates=['date'], index_col='date')

decomposition(df)
