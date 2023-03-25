# builtin libraries
import pandas as pd
import statsmodels.api as sm
import statsmodels.tsa.api as tsa
import warnings

class Forecast:

    def convert_index(self, df, column_name):
        
        # create a series based on a dataframe
        df[column_name] = pd.to_datetime(df[column_name], format='%Y') + pd.offsets.YearEnd(1)
        df = df.set_index(column_name)
        df.index = pd.DatetimeIndex(df.index).to_period('A')
        
        return df


    def split(self, df, column_name='value'):
        # 8:2 ratio on the split
        divide = len(df) - int(0.2 * len(df))
        train, test = df[column_name][0:divide], df[column_name][divide:]

        return train, test


    def calculate_error(self, actual, result):
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


    def get_arima(self, df, horizon):
       
        results = tsa.ARIMA(df, order=(1, 1, 0), freq=None)\
            .fit()\
            .forecast(horizon)\
            .rename('arima')
        
        
        return results


    def get_sarimax(self, df, horizon):
        
        results = tsa.SARIMAX(df).fit(disp=False)\
            .forecast(horizon)\
            .rename('sarimax')
        
        return results


    def get_ardl(self, df, horizon):
        results = tsa.ARDL(df, lags=horizon)\
            .fit()\
            .forecast(horizon)\
            .rename('ardl')

        return results


    def get_simple_exponential_smoothing(self, df, horizon):
        results = tsa.SimpleExpSmoothing(df, initialization_method="estimated") \
            .fit() \
            .forecast(horizon)\
            .rename('simple exponential smoothing')

        return results


    def get_holt(self, df, horizon, exponential=False, damped_trend=False):
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

    def combine(self, actuals, prediction):
        
        prediction = prediction.to_frame('value')
        output = pd.concat([actuals, prediction])

        return output

    def search(self, test, forecasts):
        # set error to none
        error = None
        winner = None

        # search the forecasts for the best rmse when compared to test
        for method in forecasts:
            if error is None:
                # set error
                error = self.calculate_error(test, method)['Root Mean Squared Percentage Error']
                winner = method
            else:
                # save forecast with the lowest error
                if error > self.calculate_error(test, method)['Root Mean Squared Percentage Error']:
                    error = self.calculate_error(test, method)['Root Mean Squared Percentage Error']
                    winner = method

        return winner.name


    def get_forecasts(self, train, horizon, select='all'):
        # forecasting methods
        if select == 'simple exponential smoothing':
            simple = self.get_simple_exponential_smoothing(train, horizon)
            return simple
        elif select == 'exponential trend':
            holt_exponential = self.get_holt(train, horizon, exponential=True)
            return holt_exponential
        elif select == 'additive damped trend':
            holt_damped = self.get_holt(train, horizon, damped_trend=True)
            return holt_damped
        elif select == "Holt's linear trend":
            holt = self.get_holt(train, horizon)
            return holt
        elif select == 'arima':
            arima = self.get_arima(train, horizon)
            return arima
        elif select == 'sarimax':
            sarimax = self.get_sarimax(train, horizon)
            return sarimax
        elif select == 'ardl':
            ardl = self.get_ardl(train, horizon)
            return ardl
        else:
            simple = self.get_simple_exponential_smoothing(train, horizon)
            holt = self.get_holt(train, horizon)
            holt_exponential = self.get_holt(train, horizon, exponential=True)
            holt_damped = self.get_holt(train, horizon, damped_trend=True)
            arima = self.get_arima(train, horizon)
            sarimax = self.get_sarimax(train, horizon)
            ardl = self.get_ardl(train, horizon)

            forecasts = [simple, holt, holt_exponential, holt_damped, arima, sarimax, ardl]
           
            return forecasts

    
        
    def reset_index(self, actuals, prediction, horizon):

        year = actuals.index[len(actuals.index)-1]+1
        prediction.index = pd.date_range(str(year), periods=horizon, freq="Y") 
        prediction.index = pd.DatetimeIndex(prediction.index).to_period('A')
 
        return prediction
        

    def percentage(self, df):

        # cap % forecast at 100    
        df.loc[df['value'] >= 100, 'value'] = 100    

        return df
        
    def forecast(self, actuals, horizon, units):
        
        # ignore warnings from forecasting packages
        warnings.filterwarnings("ignore")

        # remove unavailable data
        actuals.dropna(inplace=True)

        # convert a df to a series
        actuals = self.convert_index(actuals, 'date') 

        # split the dataset for training and testing
        train, test = self.split(actuals)    
    
        # create a list of forecasts
        forecasts = self.get_forecasts(train, len(test), select='all')

        # find the lowest rmse
        forecast = self.search(test, forecasts)

        # use the winner to forecast the horizon
        forecast = self.get_forecasts(actuals, horizon, select=forecast)
        forecast = self.reset_index(actuals, forecast, horizon)
        
        # convert winner to a dataframe and combine with the original
        prediction = self.combine(actuals, forecast).to_timestamp(freq='A')
        
        if units == '%':
            prediction = self.percentage(prediction)
        
        return prediction
