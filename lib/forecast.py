# builtin libraries
import numpy as np 
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.api as tsa
import warnings

def convert_series(df, column_name):
    
    # create a series based on a dataframe
    df[column_name] = pd.to_datetime(df[column_name], format='%Y') + pd.offsets.YearEnd(1)
    series = df.set_index(column_name)

    return series
 
def split(df, column_name='value'):

    # 8:2 ratio on the split
    split = len(df) - int(0.2*len(df))
    train, test = df[column_name][0:split], df[column_name][split:]
    
    return train, test

def calculate_error(actual, forecast):

    errors = {'Mean Bias': sm.tools.eval_measures.bias(actual, forecast), 
    'IQR': sm.tools.eval_measures.iqr(actual, forecast),
    'Maximum Absolute Error': sm.tools.eval_measures.maxabs(actual, forecast),
    'Mean Absolute Error': sm.tools.eval_measures.meanabs(actual, forecast),
    'Median Absolute Error': sm.tools.eval_measures.medianabs(actual, forecast),       
    'Median Bias': sm.tools.eval_measures.medianbias(actual, forecast),       
    'Mean Squared Error': sm.tools.eval_measures.mse(actual, forecast),      
    'Root Mean Squared Error': sm.tools.eval_measures.rmse(actual, forecast),  
    'Root Mean Squared Percentage Error': sm.tools.eval_measures.rmspe(actual, forecast),       
    'Standard Deviation of Error': sm.tools.eval_measures.stde(actual, forecast),       
    'Variance of Error': sm.tools.eval_measures.vare(actual, forecast)       
    }
    
    return errors 

def get_arima(series, horizon):
    
    forecast = tsa.ARIMA(series, order=(5, 0, 2)).fit().forecast(horizon).rename('arima')

    return forecast

def get_sarimax(series, horizon):
    
    forecast = tsa.SARIMAX(series, order=(5, 0, 2)).fit(disp=False).forecast(horizon).rename('sarimax')
    
    return forecast

def get_ardl(series, horizon):
    
    forecast = tsa.ARDL(series, lags=horizon).fit().forecast(horizon).rename('ardl')
 
    return forecast

def get_simple_exponential_smoothing(series, horizon):

    forecast = tsa.SimpleExpSmoothing(series, initialization_method="estimated").fit().forecast(horizon).rename('Simple exponential smoothing')

    return forecast

def get_holt(df, horizon, exponential=False, damped_trend=False):
    
    if exponential:
        forecast = tsa.Holt(df, exponential=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False).forecast(horizon).rename("exponential trend")
    elif damped_trend:
        forecast = tsa.Holt(df, damped_trend=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2).forecast(horizon).rename("additive damped trend")
    else:
        forecast = tsa.Holt(df, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False).forecast(horizon).rename("Holt's linear trend")
    
    return forecast

def search(test, forecasts):
   
    # set error to none 
    error = None
    
    # search the forecasts for the best rmse when compared to test
    for forecast in forecasts:
        if error is None:
            # set error
            error = calculate_error(test, forecast)['Root Mean Squared Percentage Error']
            winner = forecast
        else:
            # save forecast with the lowest error
            if error > calculate_error(test, forecast)['Root Mean Squared Percentage Error']:
                error = calculate_error(test, forecast)['Root Mean Squared Percentage Error']
                winner = forecast
    
    return winner.name

def get_forecasts(train, horizon, select='all'):
    
    # forecasting methods
    simple = get_simple_exponential_smoothing(train, horizon)
    holt = get_holt(train, horizon)
    holt_exponential = get_holt(train, horizon, exponential=True)
    holt_damped = get_holt(train, horizon, damped_trend=True)
    arima = get_arima(train, horizon)
    sarima = get_sarimax(train, horizon)
    ardl = get_ardl(train, horizon)

    forecasts = [simple, holt, holt_exponential, holt_damped, arima, sarima, ardl]

    for method in forecasts:
        print(method.name)
        if method.name == select:
            return method
        else:
            return forecasts

def forecast(df):
    
    # ignore warnings from forecasting packages
    warnings.filterwarnings("ignore")
    
    # remove unavailable data
    df.dropna(inplace=True) 

    # convert a df to a series
    series = convert_series(df, 'date')
    
    # split the dataset for training and testing
    train, test = split(series)
    
    # create a list of forecasts
    forecasts = get_forecasts(train, len(test), select='all')     
    
    # find the lowest rmse
    winner = search(test, forecasts)
    
    print(winner) 
    
    # use the winner to forecast the horizon
    series = get_forecasts(series, len(test), select=winner)
    
    return series
