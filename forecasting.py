import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def moving_average(data, window=3):
    return data.rolling(window=window).mean()

def exponential_smoothing(data, alpha=0.3):
    result = [data[0]]  # first value is same as series
    for n in range(1, len(data)):
        result.append(alpha * data[n] + (1 - alpha) * result[n-1])
    return result

if __name__ == "__main__":
    # Load your demand data (you can replace this with any CSV of choice)
    df = pd.read_csv("sample_demand.csv")  # Ensure this CSV exists in the repo
    df["Moving_Avg"] = moving_average(df["Demand"], window=3)
    df["Exp_Smooth"] = exponential_smoothing(df["Demand"], alpha=0.2)

    # Plotting
    plt.figure(figsize=(10,5))
    plt.plot(df["Period"], df["Demand"], label="Actual Demand", marker='o')
    plt.plot(df["Period"], df["Moving_Avg"], label="Moving Average", linestyle="--")
    plt.plot(df["Period"], df["Exp_Smooth"], label="Exponential Smoothing", linestyle="-.")
    plt.xticks(rotation=45)
    plt.legend()
    plt.title("Demand Forecasting")
    plt.tight_layout()
    plt.show()
