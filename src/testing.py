import Algo

# # bfs test
# # 7x7 grid filled with zeros, with a cross of 1s
# grid = [[0 for i in range(7)] for j in range(7)]
# for i in range(7):
#     grid[3][i] = 1
#     grid[i][3] = 1

# for i in grid:
#     print(i)

# # start at (0,3) and goal at (3,6)
# path = Algo.bfs(grid, (0,3), (0,3))
# print(path)

"""
------------------------------------------------------------------------------------------------------------------------
"""

# cautious() test
# 7x7 grid filled with 1s, with a cross of -1s
grid = [[1 for i in range(7)] for j in range(7)]
for i in range(7):
    grid[3][i] = -1
    grid[i][3] = -1

for i in grid:
    print(i)

# start at (0,3) and goal at (3,6)
grid_cautious = Algo.cautious(grid)
for i in grid_cautious:
    print(i)