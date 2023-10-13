import numpy as np
import matplotlib.pyplot as plt
from Scenario import *

bot1 = []
bot2 = []
bot3 = []
bot4 = []

# I've replaced range with np.arange for the decimal increments
for q in np.arange(0, 1.01, 0.1):
    for bot_type in range(1, 4):  # Adjusted to include bot 4
        for i in range(25):
            scenario = Scenario(10, bot_type, q)
            while True:
                out = scenario.timestep()
                if out in [1, -1]:
                    if bot_type == 1:
                        bot1.append((scenario.q, out))
                    elif bot_type == 2:
                        bot2.append((scenario.q, out))
                    elif bot_type == 3:
                        bot3.append((scenario.q, out))
                    # elif bot_type == 4:
                    #     bot4.append((scenario.q, out))
                    break
            print("Scenario " + str(i) + " finished")

# Function to compute the success rate
def compute_success_rate(data):
    q_values = np.arange(0, 1.01, 0.1)
    rates = []
    for q in q_values:
        successes = sum(1 for x in data if x[0] == q and x[1] == 1)
        total = sum(1 for x in data if x[0] == q)
        rate = successes / total if total != 0 else 0
        rates.append(rate)
    return rates

# Plotting the data
plt.figure(figsize=(10, 6))

plt.plot(np.arange(0, 1.01, 0.1), compute_success_rate(bot1), label='Bot 1')
plt.plot(np.arange(0, 1.01, 0.1), compute_success_rate(bot2), label='Bot 2')
plt.plot(np.arange(0, 1.01, 0.1), compute_success_rate(bot3), label='Bot 3')
# plt.plot(np.arange(0, 1.01, 0.01), compute_success_rate(bot4), label='Bot 4')

plt.title('Success Rate of Bots')
plt.xlabel('q value')
plt.ylabel('Success Rate')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.show()
