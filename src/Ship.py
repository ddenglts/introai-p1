from typing import List, Tuple, Dict
import random

def build(size: int) -> List[List[int]]:
    grid = [[0 for i in range(size)] for j in range(size)]

    #randomly open 1 interior cell
    grid[random.randint(1,size-2)][random.randint(1,size-2)] = 1

    while True:
        one_open_neighbor_cells = []
        
            #identify all closed cells that have a single open neighbor in the 4 cardinal directions
        for i in range(size):
            for j in range(size):
                num_open_neighbors = 0
                if grid[i][j] == 1:
                    continue
                if i != 0:
                    if grid[i-1][j] == 1:
                        num_open_neighbors += 1
                if i != size-1:
                    if grid[i+1][j] == 1:
                        num_open_neighbors += 1
                if j != 0:
                    if grid[i][j-1] == 1:
                        num_open_neighbors += 1
                if j != size-1:
                    if grid[i][j+1] == 1:
                        num_open_neighbors += 1
                if num_open_neighbors == 1:
                    one_open_neighbor_cells.append((i,j))
        
        #break if no open cells
        if len(one_open_neighbor_cells) == 0:
            break

        #open one of these cells at random
        if len(one_open_neighbor_cells) > 0:
            chosen_cell = one_open_neighbor_cells[random.randint(0,len(one_open_neighbor_cells)-1)]
            grid[chosen_cell[0]][chosen_cell[1]] = 1

    dead_ends = []
        
    for i in range(size):
        for j in range(size):
            #check to see if cell is open
            num_open_neighbors = 0
            if grid[i][j] == 1:
                if i != 0:
                    if grid[i-1][j] == 1:
                        num_open_neighbors += 1
                if i != size-1:
                    if grid[i+1][j] == 1:
                        num_open_neighbors += 1
                if j != 0:
                    if grid[i][j-1] == 1:
                        num_open_neighbors += 1
                if j != size-1:
                    if grid[i][j+1] == 1:
                        num_open_neighbors += 1
                if num_open_neighbors == 1:
                    dead_ends.append((i,j))
         
    num_dead_ends = len(dead_ends)/2
    c = 0

    while c < num_dead_ends:
        dead_ends.pop(random.randint(0,len(dead_ends)-1))
        c += 1

    opening_cell = []
    for i in range(len(dead_ends)):
        r = dead_ends[i][0]
        c = dead_ends[i][1]
        if r != 0:
            if grid[r-1][c] == 0:
                opening_cell.append((r-1,c))
        if r != size-1:
            if grid[r+1][c] == 0:
                opening_cell.append((r+1,c))
        if c != 0:
            if grid[r][c-1] == 0:
                opening_cell.append((r,c-1))
        if c != size-1:
            if grid[r][c+1] == 0:
                opening_cell.append((r,c+1))
        cell_to_open = opening_cell[(random.randint(0,len(opening_cell)-1))]
        grid[cell_to_open[0]][cell_to_open[1]] = 1

    #place button
    while True:
        r = random.randint(0,size-1)
        c = random.randint(0,size-1)
        if grid[r][c] == 1:
            grid[r][c] = 2
            break
    
    #place fire
    while True:
        r = random.randint(0,size-1)
        c = random.randint(0,size-1)
        if grid[r][c] == 1:
            grid[r][c] = -1
            break

    return grid

