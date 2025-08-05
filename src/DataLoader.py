# import necessary libraries
import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Load data from the specified file path."""
        try:
            self.data = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
            return self.data
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except pd.errors.EmptyDataError:
            print("No data found in the file.")
        except pd.errors.ParserError:
            print("Error parsing the file. Please check the file format.")
        return None
