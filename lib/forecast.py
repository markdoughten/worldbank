# builtin libraries
import pandas as pd
import statsmodels.api as sm
import statsmodels.tsa.api as tsa
import warnings


def convert_index(df, column_name):
    
    # create a series based on a dataframe
    df[column_name] = pd.to_datetime(df[column_name], format='%Y') + pd.offsets.YearEnd(1)
    df = df.set_index(column_name)

    return df


def split(df, column_name='value'):
    # 8:2 ratio on the split
    divide = len(df) - int(0.2 * len(df))
    train, test = df[column_name][0:divide], df[column_name][divide:]

    return train, test


def calculate_error(actual, result):
    errors = {'Mean Bias': sm.tools.eval_measures.bias(actual, result),
              'IQR': sm.tools.eval_measures.iqr(actual, result),
              'Maximum Absolute Error': sm.tools.eval_measures.maxabs(actual, result),
              'Mean Absolute Error': sm.tools.eval_measures.meanabs(actual, result),
              'Median Absolute Error': sm.tools.eval_measures.medianabs(actual, result),
              'Median Bias': sm.tools.eval_measures.medianbias(actual, result),
              'Mean Squared Error': sm.tools.eval_measures.mse(actual, result),
              'Root Mean Squared Error': sm.tools.eval_measures.rmse(actual, result),
              'Root Mean Squared Percentage Error': sm.tools.eval_measures.rmspe(actual, result),
              'Standard Deviation of Error': sm.tools.eval_measures.stde(actual, result),
              'Variance of Error': sm.tools.eval_measures.vare(actual, result)
              }

    return errors


def get_arima(df, horizon):
    results = tsa.ARIMA(df, order=(5, 0, 2))\
        .fit()\
        .forecast(horizon)\
        .rename('arima')

    return results


def get_sarimax(df, horizon):
    results = tsa.SARIMAX(df, order=(5, 0, 2)).fit(disp=False)\
        .forecast(horizon)\
        .rename('sarimax')

    return results


def get_ardl(df, horizon):
    results = tsa.ARDL(df, lags=horizon)\
        .fit()\
        .forecast(horizon)\
        .rename('ardl')

    return results


def get_simple_exponential_smoothing(df, horizon):
    results = tsa.SimpleExpSmoothing(df, initialization_method="estimated") \
        .fit() \
        .forecast(horizon)\
        .rename('simple exponential smoothing')

    return results


def get_holt(df, horizon, exponential=False, damped_trend=False):
    if exponential:
        results = tsa.Holt(df, exponential=True, initialization_method="estimated") \
            .fit(smoothing_level=0.8,
                 smoothing_trend=0.2,
                 optimized=False) \
            .forecast(horizon)\
            .rename("exponential trend")
    elif damped_trend:
        results = tsa.Holt(df, damped_trend=True, initialization_method="estimated") \
            .fit(smoothing_level=0.8,
                 smoothing_trend=0.2) \
            .forecast(horizon)\
            .rename("additive damped trend")
    else:
        results = tsa.Holt(df, initialization_method="estimated") \
            .fit(smoothing_level=0.8, smoothing_trend=0.2,
                 optimized=False).forecast(horizon)\
            .rename("Holt's linear trend")

    return results

def combine(actuals, prediction):
    
    prediction = prediction.to_frame('value')
    output = pd.concat([actuals, prediction])

    return output

def search(test, forecasts):
    # set error to none
    error = None
    winner = None

    # search the forecasts for the best rmse when compared to test
    for method in forecasts:
        if error is None:
            # set error
            error = calculate_error(test, method)['Root Mean Squared Percentage Error']
            winner = method
        else:
            # save forecast with the lowest error
            if error > calculate_error(test, method)['Root Mean Squared Percentage Error']:
                error = calculate_error(test, method)['Root Mean Squared Percentage Error']
                winner = method

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

    if select == 'all':
        return forecasts
    else:
        for method in forecasts:
            if method.name == select:
                return method


def forecast(df):
    
    # ignore warnings from forecasting packages
    warnings.filterwarnings("ignore")

    # remove unavailable data
    df.dropna(inplace=True)

    # convert a df to a series
    df = convert_index(df, 'date')

    # split the dataset for training and testing
    train, test = split(df)

    # create a list of forecasts
    forecasts = get_forecasts(train, len(test), select='all')

    # find the lowest rmse
    winner = search(test, forecasts)

    # use the winner to forecast the horizon
    winner = get_forecasts(df, len(test), select=winner)   
    
    # convert winner to a dataframe and combne with the original
    prediction = combine(df, winner)

    return prediction
