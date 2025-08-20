import matplotlib.pyplot as plt
import pandas as pd

class BrentVisualizer:
    def __init__(self, df):
        """Initialize with processed DataFrame"""
        self.df = df
        
    def plot_raw_prices(self, events=None):
        plt.figure(figsize=(14, 6))
        
        # Main price plot
        plt.plot(self.df['Date'], self.df['Price'], 
                label='Brent Price', linewidth=1.5)
        
        # Event markers if provided
        if events is not None and not events.empty:  # Proper DataFrame check
            for _, row in events.iterrows():
                plt.axvline(pd.to_datetime(row['Start_Date']),  # Ensure datetime
                           color='red', alpha=0.3, 
                           linestyle='--', linewidth=1)
        
        plt.title('Brent Crude Oil Prices with Event Markers')
        plt.xlabel('Date')
        plt.ylabel('Price (USD/barrel)')
        plt.grid(alpha=0.3)
        plt.legend()
        plt.tight_layout()
        # return plt.gcf()