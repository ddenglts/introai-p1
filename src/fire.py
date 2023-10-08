import random
from typing import List, Tuple, Dict
        
def spread(grid: List[List[int]], q: float) -> None:
    future_on_fire_cells = []
    on_fire_cells = _get_on_fire_cells(grid)
    for cell in on_fire_cells:
        adj = []
        k = 0
        x = cell[0]
        y = cell[1]
        
        if grid[x][y] == 1:
            #right neighbor
            if grid[x+1][y] and grid[x+1][y] == 1:
                adj.append((x+1,y))
            elif grid[x+1][y] and grid[x+1][y] == -1:
                k += 1
            #left neighbor
            if grid[x-1][y] and grid[x-1][y] == 1:
                adj.append((x-1,y))
            elif grid[x-1][y] and grid[x-1][y] == -1:
                k += 1
            #up neighbor
            if grid[x][y+1] and grid[x][y+1] == 1:
                adj.append((x,y+1))
            elif grid[x][y+1] and grid[x][y+1] == -1:
                k += 1
            #down neighbor
            if grid[x+1][y] and grid[x][y-1] == 1:
                adj.append((x,y-1))
            elif grid[x][y-1] and grid[x][y-1] == -1:
                k += 1
        rand = 1 - (1 - q)**k
        """
        !!! WARNING: RANDOM.RANDOM is [0, 1) !!!
        """
        if random.random() <= rand:
            
            future_on_fire_cells.append((x,y))
    
    #update ship grid to spread calculations
    for i in future_on_fire_cells:
        grid[i[0]][i[1]] = -1



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
    

        
        
        