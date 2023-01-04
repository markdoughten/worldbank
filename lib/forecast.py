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

def arima_method(series, horizon):
    
    fit = tsa.ARIMA(series, order=(5, 0, 2)).fit()
    forecast = fit.forecast(horizon)
    
    return fit, forecast

def sarimax_method(series, horizon):
    
    fit = tsa.SARIMAX(series, order=(5, 0, 2)).fit(disp=False)
    forecast = fit.forecast(horizon)
    
    return fit, forecast

def ardl_method(series, horizon):
    
    fit = tsa.ARDL(series, lags=horizon).fit()
    forecast = fit.forecast(horizon)
    
    return fit, forecast

def simple_expontential_smoothing(series, horizon):

    fit = tsa.SimpleExpSmoothing(series, initialization_method="estimated").fit()
    forecast = fit.forecast(horizon).rename(r"$\alpha=%s$" % fit.model.params["smoothing_level"])
   
    return fit, forecast

def holt_method(df, horizon, exponential=False, damped_trend=False):
    
    if exponential:
        fit = tsa.Holt(df, exponential=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False)
        forecast = fit.forecast(horizon).rename("Exponential trend")

    elif damped_trend:
        fit = tsa.Holt(df, damped_trend=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2)
        forecast = fit.forecast(horizon).rename("Additive damped trend")

    else:
        fit = tsa.Holt(df, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False)
        forecast = fit.forecast(horizon).rename("Holt's linear trend")

    return fit, forecast

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
    
    return winner

def methods(train, horizon):
    
    # forecasting methods
    fit, simple = simple_expontential_smoothing(train, horizon)
    fit, holt = holt_method(train, horizon)
    fit, holt_exponential = holt_method(train, horizon, exponential=True)
    fit, holt_damped = holt_method(train, horizon, damped_trend=True)
    fit, arima = arima_method(train, horizon)
    fit, sarima = sarimax_method(train, horizon)
    fit, ardl = ardl_method(train, horizon)
    
    return [simple, holt, holt_exponential, holt_damped, arima, sarima, ardl]   

def forecast(df):
   
    # ignore warnings
    warnings.filterwarnings("ignore")
 
    # convert a df to a series
    series = convert_series(df, 'date')

    train, test = split(df)

    forecasts = methods(train, len(test))     
    
    winner = search(test, forecasts)

    df = winner.forecast(df, 5)
    
    return df
