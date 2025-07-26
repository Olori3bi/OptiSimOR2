# demand_forecast.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DemandForecaster:
    def __init__(self, demand_data):
        self.data = pd.Series(demand_data)
    
    def simple_moving_average(self, window=3):
        return self.data.rolling(window=window).mean()
    
    def exponential_smoothing(self, alpha=0.5):
        return self.data.ewm(alpha=alpha, adjust=False).mean()

    def plot_forecasts(self, sma_window=3, alpha=0.5):
        sma = self.simple_moving_average(window=sma_window)
        es = self.exponential_smoothing(alpha=alpha)

        plt.figure(figsize=(10, 6))
        plt.plot(self.data, label='Original Demand', marker='o')
        plt.plot(sma, label=f'{sma_window}-period SMA', linestyle='--')
        plt.plot(es, label=f'Exponential Smoothing (α={alpha})', linestyle='-.')
        plt.title('Demand Forecasting')
        plt.xlabel('Time Period')
        plt.ylabel('Demand')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == "__main__":
    sample_demand = [120, 130, 125, 145, 150, 160, 170, 180, 175, 165]
    forecaster = DemandForecaster(sample_demand)
    forecaster.plot_forecasts(sma_window=3, alpha=0.3)
