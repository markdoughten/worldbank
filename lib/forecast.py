# builtin libraries
import numpy as np 
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

def fill_missing(values):

    return

def series(df, column_name):
    
    # create a series based on a dataframe
    df[column_name] = pd.to_datetime(df[column_name], format='%Y') + pd.offsets.YearEnd(1)
    series = df.set_index(column_name)

    return series
 
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
    split = len(df) - int(0.2*len(df))
    train, test = df[column_name][0:split], df[column_name][split:]
    
    return train, test

def pacf(series):

    plot_pacf(series)
    plt.show()

    return

def acf(series):

    plot_acf(series)
    plt.show()

    return

def decomposition(series, model='multiplicative'):
    
    # show the decomposition
    result = seasonal_decompose(series, model=model)
    result.plot()
    plt.show()
    
    return

def simple_expontential_smoothing(series, horizon):

    fit = SimpleExpSmoothing(series, initialization_method="estimated").fit()

    forecast = fit.forecast(horizon).rename(r"$\alpha=%s$" % fit.model.params["smoothing_level"])
   
    return fit, forecast

def error(actual, forecast):
    
    # compare test forecast to actuals
    error = actual - forecast
    
    ME = sum(error)*1.0/len(actual)
    MAE = sum(abs(error))*1.0/len(actual)
    MSE = sum(error**2)*1.0/len(actual)
   
    PE = (error/actual)*100    
    MPE = sum(error)/len(forecast)
    MAE = sum(abs(error))/len(forecast)

    print('Summary of errors resulting from actuals & forecast:')
    
    results = {'Errors': ['ME', 'MAE', 'MSE', 'MPE', 'MAPE'], 'Value': [ME, MAE, PE, MPE, MAE]}

    output = pd.DataFrame(results, columns=['Errors', 'Value'])

    print(output)       
    
    return output

def holt_method(df, horizon, exponential=False, damped_trend=False):
    
    if exponential:
        fit = Holt(df, exponential=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False)
        forecast = fit.forecast(horizon).rename("Exponential trend")

    elif damped_trend:
        fit = Holt(df, damped_trend=True, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2)
        forecast = fit.forecast(horizon).rename("Additive damped trend")

    else:
        fit = Holt(df, initialization_method="estimated").fit(smoothing_level=0.8, smoothing_trend=0.2, optimized=False)
        forecast = fit.forecast(horizon).rename("Holt's linear trend")

    return fit, forecast

def naive():
    
    # generate a basic naive forecast

    return     


# read the df from app
df = read('../docs/out.csv')

# convert a df to a series
series = series(df, 'date')

#acf(series)
#pacf(series)
#decomposition(series)

train, test = split(df)

plt.plot(train, color='black')
plt.plot(test, color='red')

fit, simple = simple_expontential_smoothing(train, horizon=len(test))
(line1,) = plt.plot(simple, color='purple')

fit, holt = holt_method(train, len(test))
(line2,) = plt.plot(holt, color='orange')

fit, holt_exponential = holt_method(train, len(test), exponential=True)
(line3,) = plt.plot(holt_exponential, color='blue')

fit, hold_damped = holt_method(train, len(test), damped_trend=True)
(line4,) = plt.plot(hold_damped, color='green')

plt.legend([line1, line2, line3, line4], [simple.name, holt.name, holt_exponential.name, hold_damped.name])
plt.show()

error(test, simple)
