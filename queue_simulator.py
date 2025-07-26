import numpy as np
import matplotlib.pyplot as plt
import random

class QueueSimulator:
    def __init__(self, arrival_rate, service_rate, simulation_time):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.simulation_time = simulation_time
        self.queue = []
        self.clock = 0
        self.wait_times = []

    def run(self):
        next_arrival = np.random.exponential(1 / self.arrival_rate)
        next_departure = float('inf')

        while self.clock < self.simulation_time:
            if next_arrival <= next_departure:
                self.clock = next_arrival
                self.queue.append(self.clock)
                next_arrival += np.random.exponential(1 / self.arrival_rate)
                if len(self.queue) == 1:
                    next_departure = self.clock + np.random.exponential(1 / self.service_rate)
            else:
                self.clock = next_departure
                arrival_time = self.queue.pop(0)
                self.wait_times.append(self.clock - arrival_time)
                if len(self.queue) > 0:
                    next_departure = self.clock + np.random.exponential(1 / self.service_rate)
                else:
                    next_departure = float('inf')

        print(f"Average wait time: {np.mean(self.wait_times):.2f} units")

    def plot(self):
        plt.hist(self.wait_times, bins=20, color='skyblue')
        plt.title('Distribution of Wait Times')
        plt.xlabel('Wait Time')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    sim = QueueSimulator(arrival_rate=2, service_rate=3, simulation_time=100)
    sim.run()
    sim.plot()
