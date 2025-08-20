from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration
prices = [
    {"date": "2022-01-01", "price": 80.5},
    {"date": "2022-01-02", "price": 81.2},
    # ...  data
]

changepoints = [
    {"date": "2008-08-05", "mean_before": 0.0003, "mean_after": -0.0001, "var_before": 0.0005, "var_after": 0.0008}
    # ...  change points
]

events = [
    {"start_date": "2008-08-01", "end_date": "2008-08-10", "description": "Global Financial Crisis"},
    # ...  events
]

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Dashboard backend is running.'})

@app.route('/api/prices', methods=['GET'])
def get_prices():
    return jsonify(prices)

@app.route('/api/changepoints', methods=['GET'])
def get_changepoints():
    return jsonify(changepoints)

@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)