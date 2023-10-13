from typing import List, Tuple, Dict
from queue import PriorityQueue
import numpy as np
import math


"""
Algorithms for project

bfs, cautious, copy
"""

def bfs(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Breadth first search

    Returns a list of tuples of the path, where [0] is start and [-1] is goal.
    Returns [(-1,-1)] if no path is found.
    """

    parents = {}
    parents[start] = None

    visited = [start]

    fringe = [start]

    path = []


    while fringe:
        curr = fringe.pop(0)

        # found goal
        if curr == goal:
            
            # Backtracking
            path.append(curr)
            parent = parents[curr]
            while parent != None:
                path.append(parent)
                parent = parents[parent]
            path.reverse()
            return path
        

        children = _get_unvisited_children(grid, visited, curr)
        for child in children:
            if not (child in visited):  # Check if we haven't visited this child before, VERY POOR COMPLEXITY(TRY TO FIX LATER)
                visited.append(child)
                parents[child] = curr
                fringe.append(child)

    return None

def _get_unvisited_children(grid: List[List[int]], visited: List[Tuple[int, int]], curr: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Returns a list of tuples of the unvisited children of the current node
    """
    children = []
    x, y = curr
    grid_max_ind = len(grid) - 1
    if x != grid_max_ind and (grid[x+1][y] == 1 or grid[x+1][y] == 2):
        children.append((x+1,y))
    if x != 0 and (grid[x-1][y] == 1 or grid[x-1][y] == 2):
        children.append((x-1,y))
    if y != grid_max_ind and (grid[x][y+1] == 1  or grid[x][y+1] == 2):
        children.append((x,y+1))
    if y != 0 and (grid[x][y-1] == 1 or grid[x][y-1] == 2):
        children.append((x,y-1))

    # does not return visited nodes
    for child in children:
        if child in visited:
            children.remove(child)
    
    return children

def cautious(grid: List[List[int]]) -> List[List[int]]:
    """
    Returns a grid with the fires moved one step outwards to open cells

    !!! WARNING: ASSUMES FIRE CANNOT BURN BUTTON !!!
    """
    grid_cautious = _copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == -1:
                if i != len(grid) - 1 and grid[i+1][j] == 1:
                    grid_cautious[i+1][j] = -1
                if i != 0 and grid[i-1][j] == 1:
                    grid_cautious[i-1][j] = -1
                if j != len(grid) - 1 and grid[i][j+1] == 1:
                    grid_cautious[i][j+1] = -1
                if j != 0 and grid[i][j-1] == 1:
                    grid_cautious[i][j-1] = -1
    return grid_cautious

def _copy(grid: List[List[int]]) -> List[List[int]]:
    """
    Returns a copy of the grid
    """
    copy = []
    for row in grid:
        copy.append(row.copy())
    return copy

def find(grid: List[List[int]], value: int) -> Tuple[int, int]:
    """
    Returns the position of the first instance of value in grid
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == value:
                return (i,j)
    return None

def ufcs(grid: List[List[int]], utils: np.ndarray, root: Tuple[int, int]) -> List[Tuple[int, int]]:
    
    """
    Returns a grid of the shortest path from root to all other nodes
    utils values are caclulated by <cell distance from nearest fire> - <cell distance from root> - <cell distance from goal>
    formula: starting value will be (length of grid / 2) + how many cells away it is from button. Smaller values are better. For
    a 10x10 grid, a cell that is right next to fire will have a value of 5. A cell that is 5 cells away from fire will have a value of 1.
    If a cell is 3 cells away from the button its value will be increased by 3.
    Example: 10x10 grid, fire is at (0,0), button is at (3,3). Cell at (0,1). Assuming there are no closed cells, cell will have a value of
    5(from fire) + 5(from distance from button) = 10
    """
    
    # goal = find(grid, 2)
    # distances = {}
    # prev = {}
    # fringe = PriorityQueue()
    # distances[root] = 0
    # prev[root] = None
    # fringe.put(root, 0 )
    # while fringe:
    #     curr = fringe.get()
    #     if curr is goal:
    #         return "Success!", prev, distances
    #     for child in curr:
    #         temp_dist = distances[curr] + utils[child]
    #         if child not in distances or temp_dist < distances[ child ]:
    #             distances[ child ] = temp_dist
    #             prev[ child ] = curr
    #             fringe.put( child, temp_dist )
    #     return "Failure", None, None

    print("ufcs")
    goal = find(grid, 2)

    parents = {}
    parents[root] = None
    
    distances = {root: 0}

    fringe = PriorityQueue()
    fringe.put((root, 0))

    path = []

    while not fringe.empty():
        curr, curr_cost = fringe.get()

        # found goal
        if curr == goal:
            
            # Backtracking
            path.append(curr)
            parent = parents[curr]
            while parent != None:
                path.append(parent)
                parent = parents[parent]
            path.reverse()
            return path
        

        children = _get_unvisited_children(grid, distances, curr[0])
        for child in children:
            temp_dist = distances[curr] + utils[child[0], child[1]]
            if (not (child in distances)) or (temp_dist < distances[child]):  # Check if we haven't visited this child before, VERY POOR COMPLEXITY(TRY TO FIX LATER)
                distances[child] = temp_dist
                parents[child] = curr[0]
                fringe.put((child, temp_dist))

    return None
    
    

def root_to_all(grid: List[List[int]], root: Tuple[int, int]) -> List[List[int]]:
    """
    Returns a grid of the shortest paths from root to all other nodes
    """
    """
    Breadth first search

    Returns a list of tuples of the path, where [0] is start and [-1] is goal.
    Returns [(-1,-1)] if no path is found.
    """

    if root == None:
        print("root is none, NO BUTTON")
        return None

    parents = {}
    parents[root] = None

    visited = [root]

    fringe = [root]

    depths = [[0 for i in range(len(grid))] for j in range(len(grid))]

    while fringe:
        curr = fringe.pop(0)


        children = _get_unvisited_children(grid, visited, curr)
        for child in children:
            if not (child in visited):
                # Check if we haven't visited this child before, VERY POOR COMPLEXITY(TRY TO FIX LATER)
                x, y = child

                visited.append(child)
                parents[child] = curr
                fringe.append(child)
                depths[x][y] = depths[curr[0]][curr[1]] + 1

    return depths


def util_fire(grid: List[List[int]]) -> np.ndarray:
    """
    Returns a grid of the utility values of the cells
    """
    outer_fire = get_outer_fire(grid)
    util_fire_grid = np.zeros((len(grid), len(grid)))
        
    for fire in outer_fire:
        util_fire_grid = np.add(util_fire_grid, get_fire_aura(grid, fire, int(len(grid)/2)))
    return util_fire_grid


def get_outer_fire(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Returns a grid of the outer fire cells
    """
    outer_fire = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == -1:
                if i != len(grid) - 1 and (grid[i+1][j] == 1 or grid[i+1][j] == 2):
                    outer_fire.append((i,j))
                elif i != 0 and (grid[i-1][j] == 1 or grid[i-1][j] == 2):
                    outer_fire.append((i,j))
                elif j != len(grid) - 1 and (grid[i][j+1] == 1 or grid[i][j+1] == 2):
                    outer_fire.append((i,j))
                elif j != 0 and (grid[i][j-1] == 1 or grid[i][j-1] == 2):
                    outer_fire.append((i,j))
    return outer_fire

def get_fire_aura(grid: List[List[int]], root: Tuple[int, int], length: int) -> np.ndarray:
    parents = {}
    parents[root] = None

    visited = [root]

    fringe = [root]

    depths = np.zeros((len(grid), len(grid)))

    while fringe:
        curr = fringe.pop(0)
        if depths[curr[0],curr[1]] == length:
            continue
        children = _get_unvisited_children(grid, visited, curr)
        # delete children that are too far away

        for child in children:
            if not (child in visited):
                # Check if we haven't visited this child before, VERY POOR COMPLEXITY(TRY TO FIX LATER)
                x, y = child

                visited.append(child)
                parents[child] = curr
                fringe.append(child)
                depths[x, y] = depths[curr[0], curr[1]] + 1

    depths[depths > 0] = length - depths[depths > 0] + 1

    return depths
    
def get_utils(grid: List[List[int]], goal: Tuple[int, int]) -> List[List[int]]:
    to_all = root_to_all(grid, goal)
    fire_utils = util_fire(grid)
    utils = np.add(to_all, fire_utils)
    utils[find(grid, 2)] = 0
    return utils