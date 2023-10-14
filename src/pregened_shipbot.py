import Ship
import numpy as np
import random

GRID_SIZE = 50

ship_grids = []

for i in range(GRID_SIZE):
    grid = Ship.build(GRID_SIZE)
    bot_pos = (0,0)
    while True:
                bot_pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
                if grid[bot_pos[0]][bot_pos[1]] == 1:
                    break
                      
    ship_grids[i] = (Ship.build(50), bot_pos) 


np.save("shipbot.npy", ship_grids)