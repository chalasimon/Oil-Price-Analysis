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

## Getting Started
To get started with this project, you'll need to have Python 3.13.3 installed, along with the required dependencies. You can set up a virtual environment and install the dependencies using the following commands:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
source .venv/Scripts/activate  # On macOS/Linux
pip install -r requirements.txt
```
# Project Structure
The project is structured as follows:

```
Oil-Price-Analysis/
├── .gitignore
├── .vscode/
├── data/
├── notebooks/
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── visualization.py
├── requirements.txt
├── README.md
├── LICENSE
└── .venv/

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.