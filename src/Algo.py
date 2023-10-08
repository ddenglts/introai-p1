from typing import List, Tuple, Dict

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
    if x != grid_max_ind and (grid[x+1][y] == 1 or grid[x+1][y] == 3):
        children.append((x+1,y))
    if x != 0 and (grid[x-1][y] == 1 or grid[x-1][y] == 3):
        children.append((x-1,y))
    if y != grid_max_ind and (grid[x][y+1] == 1  or grid[x][y+1] == 3):
        children.append((x,y+1))
    if y != 0 and (grid[x][y-1] == 1 or grid[x][y-1] == 3):
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
    return (-1,-1)