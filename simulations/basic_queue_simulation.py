import random
import numpy as np
import matplotlib.pyplot as plt

class MM1Queue:
    def __init__(self, arrival_rate, service_rate, simulation_time):
        self.lambda_ = arrival_rate
        self.mu = service_rate
        self.simulation_time = simulation_time
        self.clock = 0
        self.queue = []
        self.server_busy = False
        self.event_list = []
        self.waiting_times = []
        self.service_times = []
        self.interarrival_times = []
        self.time_last_event = 0
        self.total_idle_time = 0
        self.total_customers = 0

    def exponential(self, rate):
        return np.random.exponential(1 / rate)

    def schedule_event(self, time, event_type):
        self.event_list.append((self.clock + time, event_type))
        self.event_list.sort()

    def run(self):
        # Schedule first arrival
        self.schedule_event(self.exponential(self.lambda_), "arrival")

        while self.clock < self.simulation_time:
            if not self.event_list:
                break

            self.clock, event_type = self.event_list.pop(0)

            if event_type == "arrival":
                self.handle_arrival()
            elif event_type == "departure":
                self.handle_departure()

    def handle_arrival(self):
        self.total_customers += 1
        self.interarrival_times.append(self.clock - self.time_last_event)
        self.time_last_event = self.clock
        self.schedule_event(self.exponential(self.lambda_), "arrival")

        if not self.server_busy:
            self.server_busy = True
            service_time = self.exponential(self.mu)
            self.service_times.append(service_time)
            self.waiting_times.append(0)
            self.schedule_event(service_time, "departure")
        else:
            self.queue.append(self.clock)

    def handle_departure(self):
        if self.queue:
            arrival_time = self.queue.pop(0)
            waiting_time = self.clock - arrival_time
            self.waiting_times.append(waiting_time)
            service_time = self.exponential(self.mu)
            self.service_times.append(service_time)
            self.schedule_event(service_time, "departure")
        else:
            self.server_busy = False
            self.total_idle_time += self.exponential(self.lambda_)

    def report(self):
        print("\n--- Simulation Report ---")
        print(f"Total customers served: {self.total_customers}")
        print(f"Average waiting time: {np.mean(self.waiting_times):.2f}")
        print(f"Average service time: {np.mean(self.service_times):.2f}")
        print(f"Average interarrival time: {np.mean(self.interarrival_times):.2f}")
        print(f"Server Utilization: {(1 - self.total_idle_time / self.simulation_time) * 100:.2f}%")

        plt.hist(self.waiting_times, bins=20, color='skyblue', edgecolor='black')
        plt.title("Distribution of Waiting Times")
        plt.xlabel("Waiting Time")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    arrival_rate = 1.0     # average of 1 customer per time unit
    service_rate = 1.25    # faster service
    simulation_time = 1000 # simulate 1000 time units

    sim = MM1Queue(arrival_rate, service_rate, simulation_time)
    sim.run()
    sim.report()
