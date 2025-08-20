import pymc as pm  # Using PyMC v5
import numpy as np
import pandas as pd
import arviz as az
import matplotlib.pyplot as plt

class BayesianCPDetector:
    def __init__(self, n_change_points=1):
        self.n_cp = n_change_points
        self.date_index = None  # To store dates for interpretation
        
    def fit(self, series, dates=None):
        """
        Args:
            series: Time series values (stationary)
            dates: Corresponding dates for interpretation
        """
        self.date_index = dates
        
        with pm.Model():
            # 1. Change Point Priors
            tau = pm.DiscreteUniform(
                'tau', 
                lower=0, 
                upper=len(series)-1,
                shape=self.n_cp,
                initval=np.linspace(0, len(series)-1, self.n_cp+2)[1:-1].astype(int)
            )
            
            # 2. Segment Parameters
            mu = pm.Normal('mu', mu=0, sigma=10, shape=self.n_cp+1)
            sigma = pm.HalfNormal('sigma', sigma=1, shape=self.n_cp+1)
            
            # 3. Vectorized Segment Assignment
            segment_idx = pm.math.sum(
                [pm.math.ge(np.arange(len(series)), tau[i]) 
                 for i in range(self.n_cp)],
                axis=0
            )
            
            # 4. Likelihood
            pm.Normal('obs', 
                     mu=mu[segment_idx], 
                     sigma=sigma[segment_idx], 
                     observed=series)
            
            # 5. Sampling with robustness
            trace = pm.sample(
                draws=2000,
                tune=1000,
                target_accept=0.9,
                cores=2,
                chains=4,  # Add this for robust diagnostics
                init='adapt_diag'
            )
            
        return trace
    
    def get_change_dates(self, trace):
        """Convert tau samples to actual dates"""
        if self.date_index is None:
            raise ValueError("Dates not provided during fit()")
        return self.date_index.iloc[
            np.median(trace.posterior['tau'], axis=(0,1)).astype(int)
        ]
    
    def plot_results(self, trace, original_series):
        """Visualize change points on original series"""
        fig, ax = plt.subplots(figsize=(14,6))
        ax.plot(original_series.index, original_series)
        
        for cp in self.get_change_dates(trace):
            ax.axvline(cp, color='red', linestyle='--', alpha=0.7)
        
        ax.set_title("Brent Oil Prices with Detected Change Points")
        return fig