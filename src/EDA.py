# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class EDA:
    def __init__(self, data):
        self.data = data
    def summary_statistics(self):
        print("Summary Statistics:")
        print(self.data.describe())
        print("\nData Types:")
        print(self.data.dtypes)
        print("\nMissing Values:")
        print(self.data.isnull().sum())

    def plot_price_trend(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.data.index, self.data['Price'], label='Brent Oil Price', color='blue')
        plt.title('Brent Oil Price Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()

    def plot_log_returns_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['Log_Return'].dropna(), bins=50, kde=True)
        plt.title('Distribution of Log Returns')
        plt.xlabel('Log Return')
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()
    def run_eda(self):
        print("Running Exploratory Data Analysis...")
        self.summary_statistics()
        self.plot_price_trend()
        self.plot_log_returns_distribution()
        print("EDA completed.")
        return self.data