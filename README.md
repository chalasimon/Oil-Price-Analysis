# Oil Price Analysis
The main goal of this project is to analyze  how important events affect Brent oil prices.
This will focus on finding out how changes in oil prices are linked to big events like
political decisions, conflicts in oil-producing regions, global economic sanctions, and
changes in Organization of the Petroleum Exporting Countries (OPEC) policies. The aim is
to provide clear insights that can help investors, analysts, and policymakers understand
and react to these price changes better.

## Analysis Workflow
This project uses Bayesian change point analysis to detect structural shifts in Brent oil prices and links these changes to major global events. The workflow includes:
- Data loading and cleaning
- Exploratory Data Analysis (EDA)
- Stationarity testing and log returns transformation
- Bayesian change point modeling (PyMC)
- Volatility clustering visualization
- Model diagnostics and convergence checks
- Impact quantification (mean/variance before and after change points)
- Event linkage and interpretation

The notebook provides step-by-step code, plots, and business insights for each stage.

# Getting Started
To get started with this project, you'll need Python 3.13.3 and Node.js installed. The project includes both a Jupyter notebook for analysis and an interactive dashboard (Flask backend + React frontend).

### Python Environment & Analysis
Set up a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
pip install -r requirements.txt
```

### Dashboard Setup (Flask + React)
1. **Backend (Flask):**
    - Navigate to `dashboard_backend` and run:
      ```bash
      python app.py
      ```
    - The backend serves API endpoints for prices, events, volatility, and change points.

2. **Frontend (React):**
    - Navigate to `dashboard_frontend` and run:
      ```bash
      npm install
      npm start
      ```
    - The dashboard will be available at `http://localhost:3000` and connects to the Flask backend.

### Features
- Bayesian change point analysis and volatility clustering in Jupyter notebook
- Interactive dashboard with:
  - Oil price and volatility visualization
  - Event overlays and legend
  - Date range filtering
  - Responsive UI (React + Recharts)
  - Flask REST API for data and analysis results
# Project Structure
The project is structured as follows:
```
Oil-Price-Analysis/
├── data/
├── dashboard_backend/   # Flask backend
│   └── app.py
├── dashboard_frontend/  # React frontend
│   └── src/
├── notebooks/
│   └── bayesian_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── DataLoader.py
│   ├── data_cleaner.py
│   ├── data_preprocessing.py
│   ├── EDA.py
│   ├── modeling.py
│   ├── stationarity.py
│   ├── visualization.py
├── requirements.txt
├── README.md
├── LICENSE
└── .venv/

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.