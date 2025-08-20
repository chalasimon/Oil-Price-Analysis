from flask import Flask, jsonify
from flask_cors import CORS
import sys
import os
import pandas as pd
from glob import glob

from pathlib import Path
from importlib import reload
# add the project root to the path
project_root = Path("..").resolve()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Loading the module
from src.DataLoader import DataLoader
import src.DataLoader
reload(src.DataLoader)

# data path
oil_data_path ="../data/BrentOilPrices.csv"
event_data_path = "../data/event.csv"

# initialize the DataLoader
oil_data_loader = DataLoader(oil_data_path)
event_data_loader = DataLoader(event_data_path)
# load the data
# load the data
oil_data = oil_data_loader.load_data()
event_data = event_data_loader.load_data()

# Ensure Date column is datetime
oil_data['Date'] = pd.to_datetime(oil_data['Date'])



app = Flask(__name__)
CORS(app)  # Enable CORS for all routes



changepoints = [
    {"date": "2008-08-05", "mean_before": 0.0003, "mean_after": -0.0001, "var_before": 0.0005, "var_after": 0.0008}
    # ...  change points
]


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Dashboard backend is running.'})

@app.route('/api/prices', methods=['GET'])
def get_prices():
    price_list = [
        {"date": row['Date'].strftime('%Y-%m-%d'), "price": row['Price']}
        for _, row in oil_data.iterrows()
    ]
    return jsonify(price_list)

@app.route('/api/changepoints', methods=['GET'])
def get_changepoints():
    return jsonify(changepoints)


@app.route('/api/events', methods=['GET'])
def get_events():
    event_list = event_data.to_dict(orient='records')
    return jsonify(event_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)