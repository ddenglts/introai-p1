import numpy as np
import matplotlib.pyplot as plt
from Scenario import *


TOTAL_BOT_TESTS_PER_Q = 40
Q_INCREMENT = 0.1
GRID_SIZE = 10

# bot type -> q -> success rates
tests = np.zeros((4, int(1/Q_INCREMENT), int(TOTAL_BOT_TESTS_PER_Q/4)))

for bot_type in range(4):
    for q in np.arange(0, 1, Q_INCREMENT):
        for i in range(int(TOTAL_BOT_TESTS_PER_Q / 4)):
            scenario = Scenario(GRID_SIZE, bot_type + 1, q)
            while True:
                out = scenario.timestep()
                if out in [1, -1]:
                    tests[bot_type, int(q/Q_INCREMENT), i] = out
                    break


# average out tests
tests_avg = np.zeros((4, int(1/Q_INCREMENT)))
for bot_type in range(4):
    for q in np.arange(0, 1, Q_INCREMENT):
        tests_avg[bot_type, int(q/Q_INCREMENT)] = np.average(tests[bot_type, int(q/Q_INCREMENT)])



# save to file
np.save('tests.npy', tests_avg)




# Plotting the data
plt.figure()

plt.plot(np.arange(0, 1, Q_INCREMENT), tests_avg[0], label='Bot 1')
plt.plot(np.arange(0, 1, Q_INCREMENT), tests_avg[1], label='Bot 2')
plt.plot(np.arange(0, 1, Q_INCREMENT), tests_avg[2], label='Bot 3')
plt.plot(np.arange(0, 1, Q_INCREMENT), tests_avg[3], label='Bot 4')

plt.title('Success Rate of Bots')
plt.xlabel('q value')
plt.ylabel('Success Rate')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.show()
