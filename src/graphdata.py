import numpy as np
import matplotlib.pyplot as plt
from Scenario import *


TOTAL_BOT_TESTS_PER_Q = 40
Q_INCREMENT = 0.1
GRID_SIZE = 10


tests_avg = np.load('tests.npy')



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
