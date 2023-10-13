from typing import List, Tuple, Dict
from Bot import Bot
import Algo, Check, Fire, Ship
import random

class Scenario:
    def __init__(self, grid_size: int, bot_type: int, q: float, manual_grid = None, manual_bot_pos = None) -> None:
        # debug: ###p.rints out init grid and bot position


        # builds ship grid to specs
        # places fire and button
        if manual_grid == None:
            self.grid = Ship.build(grid_size)
            self.time = 0
            self.q = q

            # place bot
            while True:
                bot_pos = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
                if self.grid[bot_pos[0]][bot_pos[1]] == 1:
                    self.bot = Bot(bot_type, bot_pos)
                    break

        else:
            self.grid = manual_grid
            self.bot = Bot(bot_type, manual_bot_pos)
            self.time = 0
            self.q = q

    def timestep(self) -> int:
        """
        1) check if bot is on fire - if so, return -1
        2) Bot moves, if fail return -1
        3) check if bot is on button - if so, return 1
        4) check if bot is on fire - if so, return -1
        5) advance fire
        6) check if bot is on fire - if so, return -1 (this fixes the delay issue when bot and fire go to same cell)
        7) return 0

        debug: 
        """

        while True:
            # 1) check if bot is on fire - if so, return False
            if Check.bot_on_fire(self.grid, self.bot.pos):
                return -1

            # 2) Bot moves
            if not self.bot.move(self.grid):
                return -1

            # 3) check if bot is on button - if so, return True
            if Check.bot_on_button(self.grid, self.bot.pos):
                return 1

            # 4) check if bot is on fire - if so, return False
            if Check.bot_on_fire(self.grid, self.bot.pos):
                return -1

            # 5) advance fire
            Fire.spread(self.grid, self.q)

            # 6) check if bot is on fire - if so, return False (this fixes the delay issue when bot and fire go to same cell)
            if Check.bot_on_fire(self.grid, self.bot.pos):
                return -1
            

            self.time += 1

            # 7) return 0
            return 0
        
        

