# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataPreprocessing:
    def __init__(self, data):
        self.data = data

    def changeformat(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='mixed', dayfirst=False)
        self.data = self.data.sort_values(by='Date')
        self.data = self.data.set_index('Date')
        print("Date format changed and data sorted by date.")
        print("First few rows of the data after changing format:")
        print(self.data.head())
        return self.data
    def handle_missing_values(self):
        # This is crucial for time series data to maintain continuity
        self.data['Price'] = self.data['Price'].interpolate(method='time')
        # Add log returns
        self.data['Log_Return'] = np.log(self.data['Price']).diff().dropna()

         # The time series for analysis will be the 'Price' for ruptures and 'Log_Return' for PyMC
        time_series_price = self.data['Price']
        time_series_log_return = self.data['Log_Return'].dropna() # Ensure log returns are also dropped if NaN

        print("Brent Oil Prices Time Series Head:")
        display(time_series_price.head())
        print("\nBrent Oil Prices Time Series Tail:")
        display(time_series_price.tail())
        print("\nBrent Oil Log Returns Time Series Head:")
        display(self.data['Log_Return'].head())
        print("\nBrent Oil Log Returns Time Series Tail:")
        display(self.data['Log_Return'].tail())

        return self.data
    def preprocess(self):
        print("Starting data preprocessing...")
        self.data = self.changeformat()
        self.data = self.handle_missing_values()
        print("Data preprocessing completed.")
        return self.data
    
