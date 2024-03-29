from Bot import *
from Scenario import *
import time, random
import Check, Algo, Ship, Fire
import numpy as np

# # bfs test
# # 7x7 grid filled with zeros, with a cross of 1s
# grid = [[0 for i in range(7)] for j in range(7)]
# for i in range(7):
#     grid[3][i] = 1
#     grid[i][3] = 1

# for i in grid:
#     ###p.rint(i)

# # start at (0,3) and goal at (3,6)
# path = Algo.bfs(grid, (0,3), (0,3))
# ###p.rint(path)

"""
------------------------------------------------------------------------------------------------------------------------
"""

# # cautious() test
# # 7x7 grid filled with 1s, with a cross of -1s
# grid = [[1 for i in range(7)] for j in range(7)]
# for i in range(7):
#     grid[3][i] = -1
#     grid[i][3] = -1

# for i in grid:
#     ###p.rint(i)

# # start at (0,3) and goal at (3,6)
# grid_cautious = Algo.cautious(grid)
# for i in grid_cautious:
#     ###p.rint(i)

"""
------------------------------------------------------------------------------------------------------------------------
"""

# # bot 1 test and check test
# # 7x7 grid filled with 0s, with a cross of 1s
# grid = [[0 for i in range(7)] for j in range(7)]
# for i in range(7):
#     grid[3][i] = 1
#     grid[i][3] = 1
# grid[3][0] = 1
# bot = Bot(1, (0,3))
# ###p.rint(bot.pos)
# while True:
#     out = bot.move(grid, (3,0))
#     ###p.rint(bot.pos)
#     ###p.rint(out)
#     if (out == False) or Check.bot_on_button(grid, bot.pos) == True:
#         break

"""
------------------------------------------------------------------------------------------------------------------------
"""

# # ship gen test
# ship = Ship.build(10)
# for i in ship:
#     ###p.rint(i)

"""
------------------------------------------------------------------------------------------------------------------------
"""

# # fire test
# grid = [[0 for i in range(7)] for j in range(7)]
# for i in range(7):
#     grid[3][i] = 1
#     grid[i][3] = 1
# grid[3][0] = -1
# for i in grid:
#     ###p.rint(i)
# while True:
#     Fire.spread(grid, 1)
#     ###p.rint("good")
#     for i in grid:
#         ###p.rint(i)
#     input("Press Enter to continue...")

"""
------------------------------------------------------------------------------------------------------------------------
"""

# # scenario test
# scenario = Scenario(10, 1, 0.5, debug=True)

# while True:
#     out = scenario.timestep()

#     ###p.rint(out)
#     if out == -1 or out == 1:
#         break
#     input("Press Enter to continue...")


import tkinter as tk

class GridGUI:
    def __init__(self, master, grid, scenario, TEMP):
        self.master = master
        self.grid = grid
        self.squares = []
        self.TEMP = TEMP
        self.text = [[None for i in range(len(self.grid))] for j in range(len(self.grid))]
        self.create_grid()
        self.create_button()
        self.scenario = scenario
        self.dot = None
        self.canvas = None
        self.show_result = False
        self.out = 0
        self.line = None
        

    def create_grid(self):
        self.canvas = tk.Canvas(self.master, width=750, height=750, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=len(self.grid[0]))
        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[i])):
                color = self.get_color(self.grid[i][j])
                square = self.canvas.create_rectangle(j*(750//len(self.grid)), i*(750//len(self.grid)), (j+1)*(750//len(self.grid)), (i+1)*(750//len(self.grid)), fill=color, outline="black")
                self.text[i][j] = self.canvas.create_text((j+0.5)*(750//len(self.grid)), (i+0.5)*(750//len(self.grid)), text=str(int(self.TEMP[i][j])), fill="black")
                row.append(square)
            self.squares.append(row)

    def create_button(self):
        button = tk.Button(self.master, text="next timestep", command=self.button_click)
        button.grid(row=len(self.grid)+1, column=0, columnspan=len(self.grid[0]))

    def button_click(self):
        # Update the grid and the GUI
        if not self.show_result:
            self.out = self.scenario.timestep()
            self.grid = self.scenario.grid
            if self.out == -1 or self.out == 1:
                self.show_result = True
            
            # update vars place
            if Algo.find(scenario.grid, 2) != None:
                self.TEMP = Algo.get_utils(scenario.grid, Algo.find(scenario.grid, 2))
            self.update(self.grid)
        else:
            exit()

    def get_color(self, value):
        if value == 0:
            # closed cells color
            return "black"
        elif value == 1:
            return "white"
        elif value == 2:
            return "blue"
        elif value == -1:
            return "red"
        else:
            return "blue"


    def update(self, grid):
        self.grid = grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                color = self.get_color(self.grid[i][j])
                self.canvas.itemconfig(self.squares[i][j], fill=color)
            
        if self.text is not None:
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    self.canvas.delete(self.text[i][j])
                    self.text[i][j] = self.canvas.create_text((j+0.5)*(750//len(self.grid)), (i+0.5)*(750//len(self.grid)), text=str(int(self.TEMP[i][j])), fill="black")
        if self.dot is not None:
            self.canvas.delete(self.dot)
        y, x = self.scenario.bot.pos
        if self.out == -1:
            self.dot = self.canvas.create_oval(x*(750//len(self.grid))+(150//len(self.grid)), y*(750//len(self.grid))+(150//len(self.grid)), x*(750//len(self.grid))+(600//len(self.grid)), y*(750//len(self.grid))+(600//len(self.grid)), fill="purple", outline="black")
        elif self.out == 1:
            self.dot = self.canvas.create_oval(x*(750//len(self.grid))+(150//len(self.grid)), y*(750//len(self.grid))+(150//len(self.grid)), x*(750//len(self.grid))+(600//len(self.grid)), y*(750//len(self.grid))+(600//len(self.grid)), fill="green", outline="black")
        else:
            self.dot = self.canvas.create_oval(x*(750//len(self.grid))+(150//len(self.grid)), y*(750//len(self.grid))+(150//len(self.grid)), x*(750//len(self.grid))+(600//len(self.grid)), y*(750//len(self.grid))+(600//len(self.grid)), fill="yellow", outline="black")


# mgrid = [
#     [  1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 0, -1],
#     [  1, 0, 1, 0, 1, 1, 1, 1, 0, -1, -1, -1],
#     [  1, 0, 1, 0, 1, -1, 0, -1, -1, -1, -1, -1],
#     [  1, 1, 1, 1, 1, -1, -1, 2, 0, 0, -1, 0],
#     [  0, 1, 0, -1, -1, -1, 0, 0, -1, -1, -1, -1],
#     [  1, 1, 0, 1, 0, -1, -1, -1, 0, -1, 0, 0],
#     [  0, 0, 0, -1, 0, -1, 0, -1, -1, -1, -1, -1],
#     [  1, 1, -1, -1, -1, 0, 0, 0, 0, -1, 0, -1],
#     [  0, 1, 0, 0, -1, -1, 0, -1, -1, -1, -1, -1],
#     [  1, 1, 1, 1, 0, -1, -1, -1, 0, -1, 0, -1],
#     [ 1, 1, 0, 0, -1, -1, -1, 0, -1, -1, -1, -1],
#     [  1, 1, -1, -1, -1, -1, 0, 0, 0, -1, 0, -1]
# ]


# ]



'''
!!! change BOT_TYPE to 1,2,3,4 to test different bots
'''
BOT_TYPE = 4

scenario = Scenario(10, BOT_TYPE, 1)
###p.rint("bot pos: ", scenario.bot.pos)
###p.rint(f"Flammibility is: {scenario.q * 100}%")
utils_grid = Algo.get_utils(scenario.grid, Algo.find(scenario.grid, 2))
###p.rint(utils_grid)
grid = scenario.grid
root = tk.Tk()
gui = GridGUI(root, grid, scenario, utils_grid)
gui.create_grid()
gui.update(grid)
root.mainloop()
