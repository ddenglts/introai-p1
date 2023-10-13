import numpy as np
import matplotlib.pyplot as plt
from Scenario import *
import glob


TOTAL_BOT_TESTS_PER_Q = 100
Q_INCREMENT = 0.05
GRID_SIZE = 25


# Load all files that match the pattern 'tests_*.npy'
files = glob.glob('tests_bot*.npy')
tests_avg = [np.load(file) for file in files]
tests_avg = np.add(np.add(tests_avg[0], tests_avg[1]), np.add(tests_avg[2], tests_avg[3]))



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
plt.ylim(-1, 1)
plt.grid(True)
plt.legend()
plt.show()
