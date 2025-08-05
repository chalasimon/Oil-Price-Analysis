# Change Point Detection and Analysis of Oil Prices
This repository contains a comprehensive analysis of oil prices, focusing on change point detection and exploratory data analysis (EDA). The project is structured to facilitate understanding of oil price trends and anomalies.
## Overview
The project is divided into several key components:
- **Data Loading**: The `DataLoader` class is responsible for loading the oil price
    data from a specified path.
- **Data Preprocessing**: The `DataPreprocessing` class handles the cleaning and preparation of the data for analysis.
- **Exploratory Data Analysis (EDA)**: The `EDA` class performs various analyses
    to uncover insights from the oil price data, including visualizations and statistical summaries.
- **Change Point Detection**: The `ChangePointDetection` class implements algorithms to identify significant changes in the oil price data, helping to pinpoint periods of volatility or trend shifts.
- **Visualization**: The `Visualization` class provides methods to visualize the results of the EDA and change point detection, making it easier to interpret the findings.
## Usage
To use this project, follow these steps:
1. Clone the repository to your local machine.
2. Ensure you have the required dependencies installed. You can install them using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Update the `data_path` variable in the `notebook/exploratory_analysis.ipynb` file to point to your local copy of the oil price data.
4. Run the Jupyter notebook `notebook/exploratory_analysis.ipynb` to perform the analysis. This notebook will:
   - Load the oil price data.
   - Preprocess the data.
   - Perform exploratory data analysis.
   - Detect change points in the oil price data.
   - Visualize the results.
5. Review the findings and visualizations to gain insights into oil price trends and anomalies.