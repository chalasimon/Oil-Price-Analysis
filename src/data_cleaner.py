# import necessary libraries
import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, missing_threshold=0.05):
        self.threshold = missing_threshold
        
    def transform_oil(self, df):
        """Handle missing values and datetime conversion"""
        df = df.interpolate()
        df['Date'] = pd.to_datetime(df['Date'])
        return df

    def transform_event(self, df):
        """Handle missing values and datetime conversion"""
        df = df.interpolate()
        df['Start_Date'] = pd.to_datetime(df['Start_Date'])
        df['End_Date'] = pd.to_datetime(df['End_Date'])
        return df