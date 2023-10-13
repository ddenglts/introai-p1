import random
from typing import List, Tuple, Dict
"""
__PYCACHE__ SOMETIMES BUGS OUT FIRE.PY DURING TESTING :skull::skull::skull::skull::skull::skull::skull::skull:
"""
def spread(grid: List[List[int]], q: float) -> None:
    """
    Spreads the fire according to the rules of the game
    fire can burn button
    """
    on_fire_cells = _get_on_fire_cells(grid)
    for cell in on_fire_cells:
        x, y = cell
        grid_max_ind = len(grid) - 1
        #right neighbor
        if x != grid_max_ind and grid[x+1][y] != 0:
            if random.random() <= (1 - (1 - q)**_num_adj_fire_cells(grid, (x+1, y))):
                grid[x+1][y] = -1
        #left neighbor
        if x != 0 and grid[x-1][y] != 0:
            if random.random() <= (1 - (1 - q)**_num_adj_fire_cells(grid, (x-1, y))):
                grid[x-1][y] = -1
        #up neighbor
        if y != grid_max_ind and grid[x][y+1] != 0:
            if random.random() <= (1 - (1 - q)**_num_adj_fire_cells(grid, (x, y+1))):
                grid[x][y+1] = -1
        #down neighbor
        if y != 0 and grid[x][y-1] != 0:
            if random.random() <= (1 - (1 - q)**_num_adj_fire_cells(grid, (x, y-1))):
                grid[x][y-1] = -1



def _get_on_fire_cells(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Returns a list of tuples of the on fire cells
    """
    on_fire_cells = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == -1:
                on_fire_cells.append((i,j))
    return on_fire_cells

def _num_adj_fire_cells(grid: List[List[int]], curr: Tuple[int, int]) -> int:
    """
    Returns the number of adjacent cells that are on fire
    """
    x, y = curr
    grid_max_ind = len(grid) - 1
    num_adj_fire_cells = 0
    #right neighbor
    if x != grid_max_ind and grid[x+1][y] == -1:
        num_adj_fire_cells += 1
    #left neighbor
    if x != 0 and grid[x-1][y] == -1:
        num_adj_fire_cells += 1
    #up neighbor
    if y != grid_max_ind and grid[x][y+1] == -1:
        num_adj_fire_cells += 1
    #down neighbor
    if y != 0 and grid[x][y-1] == -1:
        num_adj_fire_cells += 1
    return num_adj_fire_cells
      
    

        
        
# def spread(grid: List[List[int]], q: float) -> None:
#     future_on_fire_cells = []
#     on_fire_cells = _get_on_fire_cells(grid)
#     print(on_fire_cells)
#     for cell in on_fire_cells:
#         adj = []
#         k = 0
#         x, y = cell
#         grid_max_ind = len(grid) - 1
    
#         #right neighbor
#         if x != grid_max_ind and grid[x+1][y] == 1:
#             adj.append((x+1,y))
#         if x != grid_max_ind and grid[x+1][y] == -1:
#             k += 1
#         #left neighbor
#         if x != 0 and grid[x-1][y] == 1:
#             adj.append((x-1,y))
#         if x != 0 and grid[x-1][y] == -1:
#             k += 1
#         #up neighbor
#         if y != grid_max_ind and grid[x][y+1] == 1:
#             adj.append((x,y+1))
#         if y != grid_max_ind and grid[x][y+1] == -1:
#             k += 1
#         #down neighbor
#         if y != 0 and grid[x][y-1] == 1:
#             adj.append((x,y-1))
#         if y != 0 and grid[x][y-1] == -1:
#             k += 1
#         # rand = 1 - (1 - q)**k
#         # """
#         # !!! WARNING: RANDOM.RANDOM is [0, 1) !!!
#         # """
#         # if random.random() <= rand:
#         #     future_on_fire_cells.append((x,y))
        
#         future_on_fire_cells.append((x,y))
    
#     #update ship grid to spread calculations
#     print(adj)
#     for i in adj:
#         grid[i[0]][i[1]] = -1