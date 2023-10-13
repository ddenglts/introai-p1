import numpy as np
import matplotlib.pyplot as plt
from Scenario import *
import multiprocessing
import time


def do_trials(bot_type):
    pass

    BOT_TESTS_PER_Q = 50
    Q_INCREMENT = 0.05
    GRID_SIZE = 50

    num_tests = int(1/Q_INCREMENT) * BOT_TESTS_PER_Q

    test_num = 0

    #q -> success rates
    tests = np.zeros((4, int(1/Q_INCREMENT), BOT_TESTS_PER_Q))

    for q in np.arange(0, 1, Q_INCREMENT):
        for i in range(BOT_TESTS_PER_Q):
            scenario = Scenario(GRID_SIZE, bot_type, q)
            while True:
                out = scenario.timestep()
                if out in [1, -1]:
                    tests[bot_type - 1, int(q/Q_INCREMENT), i] = out
                    test_num += 1
                    print(f"Bot {bot_type} test {test_num}/{num_tests} done")
                    break


    # average out tests
    tests_avg = np.zeros((4, int(1/Q_INCREMENT)))
    for q in np.arange(0, 1, Q_INCREMENT):
        tests_avg[bot_type, int(q/Q_INCREMENT)] = np.average(tests[bot_type, int(q/Q_INCREMENT)])



    # save to file
    filename = f'tests_bot{bot_type}_{int(time.time())}.npy'
    np.save(filename, tests_avg)


bot1 = multiprocessing.Process(target=do_trials, args=(1,))
bot2 = multiprocessing.Process(target=do_trials, args=(2,))
bot3 = multiprocessing.Process(target=do_trials, args=(3,))
bot4 = multiprocessing.Process(target=do_trials, args=(4,))

bot1.start()
bot2.start()
bot3.start()
bot4.start()

bot1.join()
bot2.join()
bot3.join()
bot4.join()


print("done collecting avgs")
