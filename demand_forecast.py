# demand_forecast.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

class DemandForecaster:
    def __init__(self, demand_data):
        self.data = pd.Series(demand_data).reset_index(drop=True)
    
    def simple_moving_average(self, window=3):
        return self.data.rolling(window=window).mean()

    def exponential_smoothing(self, alpha=0.5):
        return self.data.ewm(alpha=alpha, adjust=False).mean()
    
    def arima_forecast(self, order=(1,1,1)):
        model = ARIMA(self.data, order=order)
        model_fit = model.fit()
        return model_fit.predict(start=1, end=len(self.data)-1, typ='levels')

    def plot_forecasts(self, sma_window=3, alpha=0.5, arima_order=(1,1,1)):
        sma = self.simple_moving_average(window=sma_window)
        es = self.exponential_smoothing(alpha=alpha)
        arima = self.arima_forecast(order=arima_order)

        plt.figure(figsize=(12, 6))
        plt.plot(self.data, label='Actual Demand', marker='o')
        plt.plot(sma, label=f'{sma_window}-period SMA', linestyle='--')
        plt.plot(es, label=f'Exponential Smoothing (α={alpha})', linestyle='-.')
        plt.plot(range(1, len(self.data)), arima, label=f'ARIMA{arima_order}', linestyle=':')
        plt.title('Demand Forecasting Comparison')
        plt.xlabel('Time Period')
        plt.ylabel('Demand')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def evaluate_models(self, sma_window=3, alpha=0.5, arima_order=(1,1,1)):
        print("Model RMSE Comparison:")
        try:
            sma = self.simple_moving_average(window=sma_window).dropna()
            print(f"SMA ({sma_window}): {mean_squared_error(self.data[sma_window-1:], sma, squared=False):.2f}")
        except Exception as e:
            print("SMA error:", e)
        try:
            es = self.exponential_smoothing(alpha=alpha)
            print(f"Exponential Smoothing: {mean_squared_error(self.data, es, squared=False):.2f}")
        except Exception as e:
            print("Exponential Smoothing error:", e)
        try:
            arima = self.arima_forecast(order=arima_order)
            print(f"ARIMA{arima_order}: {mean_squared_error(self.data[1:], arima, squared=False):.2f}")
        except Exception as e:
            print("ARIMA error:", e)

if __name__ == "__main__":
    # Option 1: Load from CSV
    try:
        df = pd.read_csv("demand_data.csv")
        demand_series = df["Demand"]
    except:
        # Option 2: Fall back to hardcoded sample
        demand_series = [120, 130, 125, 145, 150, 160, 170, 180, 175, 165]

    forecaster = DemandForecaster(demand_series)
    forecaster.plot_forecasts(sma_window=3, alpha=0.3, arima_order=(1,1,1))
    forecaster.evaluate_models(sma_window=3, alpha=0.3, arima_order=(1,1,1))
