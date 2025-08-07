import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss
import numpy as np

class StationarityTester:
    # A utility class for testing stationarity in time series data

    def adfuller_test(self, series, max_lags=None, regression='c'):
        result = adfuller(series, maxlag=max_lags, regression=regression)
        return {
            'test_statistic': result[0],
            'p_value': result[1],
            'critical_values': result[4],
            'n_lags': result[2],
            'n_obs': result[3]
        }

    def kpss_test(self, series, regression='c'):
        result = kpss(series, regression=regression)
        return {
            'test_statistic': result[0],
            'p_value': result[1],
            'critical_values': result[3],
            'n_lags': result[2]
        }
    
    def summary(self, series):
        
        adf = self.adfuller_test(series)
        kpss = self.kpss_test(series)
        
        return pd.DataFrame({
            'Test': ['ADF', 'KPSS'],
            'Statistic': [adf['test_statistic'], kpss['test_statistic']],
            'p-value': [adf['p_value'], kpss['p_value']],
            'Result': [
                "Stationary" if adf['p_value'] < 0.05 else "Non-Stationary",
                "Stationary" if kpss['p_value'] > 0.05 else "Non-Stationary"
            ]
        })
    def make_stationary(self, series, method='log_diff'):
        
        if method == 'log_diff':
            transformed = np.log(series).diff().dropna()
            order = 1
        elif method == 'diff':
            transformed = series.diff().dropna()
            order = 1
        elif method == 'log':
            transformed = np.log(series)
            order = 0
        else:
            raise ValueError("Method must be 'log_diff', 'diff', or 'log'")
        
        return transformed, order