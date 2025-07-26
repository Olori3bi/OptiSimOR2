import numpy as np
import matplotlib.pyplot as plt

# Parameters
annual_demand = 1200       # units/year
order_cost = 50            # cost per order
holding_cost = 2           # cost per unit per year
lead_time_days = 5
service_level = 0.95
std_dev_demand = 2         # daily demand std dev
working_days = 300

# EOQ Formula
def calculate_eoq(D, S, H):
    return int(np.sqrt((2 * D * S) / H))

eoq = calculate_eoq(annual_demand, order_cost, holding_cost)
daily_demand = annual_demand / working_days
reorder_point = int((daily_demand * lead_time_days) + 
                    (std_dev_demand * np.sqrt(lead_time_days) * 1.65))  # Z=1.65 for 95%

# Simulate inventory over time
np.random.seed(0)
days = 100
inventory = []
stock = eoq
orders = []
lead_time_counter = -1

for day in range(days):
    demand_today = int(np.random.normal(daily_demand, std_dev_demand))
    stock -= demand_today
    if stock < reorder_point and lead_time_counter < 0:
        orders.append((day + lead_time_days, eoq))
        lead_time_counter = lead_time_days

    for i, (arrival_day, qty) in enumerate(orders):
        if day == arrival_day:
            stock += qty
            orders[i] = (-1, 0)  # Mark as received

    inventory.append(max(stock, 0))
    lead_time_counter -= 1

# Plot
plt.figure(figsize=(10, 5))
plt.plot(inventory, label='Inventory Level')
plt.axhline(y=reorder_point, color='r', linestyle='--', label='Reorder Point')
plt.title('Inventory Simulation with EOQ')
plt.xlabel('Day')
plt.ylabel('Inventory')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
