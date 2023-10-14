from typing import List, Tuple, Dict, Set, Optional
from queue import PriorityQueue
import numpy as np
import math
from collections import deque
from heapq import heappush, heappop


"""
Algorithms for project

bfs, cautious, copy
"""

def bfs(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Breadth first search

    Returns a list of tuples of the path, where [0] is start and [-1] is goal.
    Returns None if no path is found.
    """

    parents = {}
    parents[start] = None

    visited = {start}

    fringe = deque([start])

    while fringe:
        curr = fringe.popleft()

        # found goal
        if curr == goal:
            # Backtracking
            path = [curr]
            parent = parents[curr]
            while parent is not None:
                path.append(parent)
                parent = parents[parent]
            path.reverse()
            return path

        children = _get_unvisited_children(grid, visited, curr)
        for child in children:
            if child not in visited:
                visited.add(child)
                parents[child] = curr
                fringe.append(child)

    return None



def a_star(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    A* search

    Returns a list of tuples of the path, where [0] is start and [-1] is goal.
    Returns None if no path is found.
    """

    parents = {}
    parents[start] = None

    to_start = {start: 0}
    to_goal = {start: _heuristic(start, goal)}

    visited = {start}

    fringe = [(to_goal[start], start)]

    while fringe:
        curr_f, curr = heappop(fringe)

        # found goal
        if curr == goal:
            # Backtracking
            path = [curr]
            parent = parents[curr]
            while parent is not None:
                path.append(parent)
                parent = parents[parent]
            path.reverse()
            return path

        children = _get_unvisited_children(grid, visited, curr)
        for child in children:
            start_c = to_start[curr] + 1
            if child in to_start and start_c >= to_start[child]:
                continue
            visited.add(child)
            parents[child] = curr
            to_start[child] = start_c
            to_goal[child] = start_c + _heuristic(child, goal)
            heappush(fringe, (to_goal[child], child))

    return None

def _heuristic(node: Tuple[int, int], goal: Tuple[int, int]) -> float:
    """
    Returns the Euclidean distance between node and goal
    """
    return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5


def _get_unvisited_children(grid: List[List[int]], visited: Set[Tuple[int, int]], curr: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Returns a list of tuples of the unvisited children of the current node
    """
    children = []
    x, y = curr
    grid_max_ind = len(grid) - 1

    if x != grid_max_ind and (grid[x+1][y] == 1 or grid[x+1][y] == 2) and (x+1, y) not in visited:
        children.append((x+1,y))
    if x != 0 and (grid[x-1][y] == 1 or grid[x-1][y] == 2) and (x-1, y) not in visited:
        children.append((x-1,y))
    if y != grid_max_ind and (grid[x][y+1] == 1  or grid[x][y+1] == 2) and (x, y+1) not in visited:
        children.append((x,y+1))
    if y != 0 and (grid[x][y-1] == 1 or grid[x][y-1] == 2) and (x, y-1) not in visited:
        children.append((x,y-1))
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

