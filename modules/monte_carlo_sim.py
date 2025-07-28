
# monte_carlo_sim.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class MonteCarloSimulator:
    def __init__(self, mean_demand=500, std_dev=50, unit_price=10, unit_cost=6, num_simulations=1000):
        self.mean_demand = mean_demand
        self.std_dev = std_dev
        self.unit_price = unit_price
        self.unit_cost = unit_cost
        self.num_simulations = num_simulations

    def run_simulation(self):
        np.random.seed(42)
        demand = np.random.normal(self.mean_demand, self.std_dev, self.num_simulations).round()
        profit = (self.unit_price - self.unit_cost) * demand
        self.results = pd.DataFrame({'Simulation': range(1, self.num_simulations + 1), 'Demand': demand, 'Profit': profit})
        return self.results

    def save_results(self, csv_file='monte_carlo_output.csv'):
        self.results.to_csv(csv_file, index=False)
        print(f"Results saved to {csv_file}")

    def plot_histogram(self, output_file='monte_carlo_profit_histogram.png'):
        plt.figure(figsize=(10, 6))
        plt.hist(self.results['Profit'], bins=30, color='skyblue', edgecolor='black')
        plt.axvline(self.results['Profit'].mean(), color='red', linestyle='dashed', linewidth=2, label=f"Mean Profit = {self.results['Profit'].mean():.2f}")
        plt.title("Monte Carlo Simulation of Profit")
        plt.xlabel("Profit")
        plt.ylabel("Frequency")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(output_file)
        print(f"Histogram saved to {output_file}")

if __name__ == "__main__":
    sim = MonteCarloSimulator()
    sim.run_simulation()
    sim.save_results()
    sim.plot_histogram()
