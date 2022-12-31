# builtin libraries
import numpy as np 
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.api as tsa

def fill_missing(values):

    return

def convert_series(df, column_name):
    
    # create a series based on a dataframe
    df[column_name] = pd.to_datetime(df[column_name], format='%Y') + pd.offsets.YearEnd(1)
    series = df.set_index(column_name)

    return series
 
def year(df, column_name='date'):

    df[column_name] = pd.to_datetime(df[column_name], format='%Y')

    return df

def read(path):
    
    df = pd.read_csv(path)

    return df

def split(df, column_name='value'):

    # 8:2 ratio on the split
    split = len(df) - int(0.2*len(df))
    train, test = df[column_name][0:split], df[column_name][split:]
    
    return train, test

def pacf(series):

    plot_pacf(series)
    plt.show()

    return

def acf(series):

    sm.plot_acf(series)
    plt.show()

    return

def decomposition(series, model='multiplicative'):
    
    # show the decomposition
    result = sm.seasonal_decompose(series, model=model)
    result.plot()
    plt.show()
    
    return

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

def arima(series, horizon):
    
    fit = tsa.ARIMA(series, order=(5, 0, 2)).fit()
    forecast = fit.forecast(horizon)
    
    return fit, forecast

def sarimax(series, horizon):
    
    fit = tsa.SARIMAX(series, order=(5, 0, 2)).fit()
    forecast = fit.forecast(horizon)
    
    return fit, forecast

def auto_reg(series, horizon):
    
    fit = tsa.AutoReg(series, order=(5, 0, 2)).fit()
    forecast = fit.forecast(horizon)
    
    return fit, forecast

def ardl(series, horizon):
    
    fit = tsa.ARDL(series, lags=horizon).fit()
    forecast = fit.forecast(horizon)
    
    return fit, forecast

def uecm(series, horizon):

    fit = tsa.UECM(series, lags=horizon).fit()
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

def naive():
    
    # generate a basic naive forecast

    return     

def forecast():
    
    # read the df from app
    df = read('../docs/out.csv')

    # convert a df to a series
    series = convert_series(df, 'date')

    #acf(series)
    #pacf(series)
    #decomposition(series)

    train, test = split(df)

    plt.plot(train, color='black')
    plt.plot(test, color='red')

    fit, simple = simple_expontential_smoothing(train, horizon=len(test))
    (line1,) = plt.plot(simple)

    fit, holt = holt_method(train, len(test))
    (line2,) = plt.plot(holt)

    fit, holt_exponential = holt_method(train, len(test), exponential=True)
    (line3,) = plt.plot(holt_exponential)

    fit, hold_damped = holt_method(train, len(test), damped_trend=True)
    (line4,) = plt.plot(hold_damped)

    fit, arima_output = arima(train, len(test))
    (line5,) = plt.plot(arima_output)

    fit, sarima_output = sarimax(train, len(test))
    (line6,) = plt.plot(sarima_output)

    fit, ardl_output = ardl(train, len(test))
    (line7,) = plt.plot(ardl_output)

    plt.legend([line1, line2, line3, line4, line5, line6, line7], 
                [simple.name, holt.name, holt_exponential.name, hold_damped.name, arima_output.name, sarima_output.name, ardl_output.name])
    plt.show()

    calculate_error(test, arima_output)

forecast()
