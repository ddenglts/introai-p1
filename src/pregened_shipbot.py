import Ship
import numpy as np
import random

NUM_SHIPS = 25
GRID_SIZE = 75

ship_grids = []
bot_poses = []

for i in range(NUM_SHIPS):
    grid = Ship.build(GRID_SIZE)
    bot_pos = (0,0)
    while True:
        bot_pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        if grid[bot_pos[0]][bot_pos[1]] == 1:
            break
    ship_grids.append(grid)
    bot_poses.append(bot_pos)
    print(f"{i} done")



np.save("ship_grids.npy", ship_grids)

np.save("bot_poses.npy", bot_poses)