#latest version
import random
#Hello this is Sarthak
#consts
ship_grid_D = 5


ship_grid = [] #D*D int array
#ship_grid creation
for i in range(ship_grid_D):
    ship_grid.append([])
    for j in range(ship_grid_D):
        ship_grid[i].append(0)

#randomly open 1 interior cell
ship_grid[random.randint(1,ship_grid_D-2)][random.randint(1,ship_grid_D-2)] = 1

while True:
    print("Ship Grid:")
    for i in range(ship_grid_D):
        print(ship_grid[i])
    #find all cells with one open neighbor
    one_open_neighbor_cells = []
    
        #identify all closed cells that have a single open neighbor in the 4 cardinal directions
    for i in range(ship_grid_D):
        for j in range(ship_grid_D):
            num_open_neighbors = 0
            if ship_grid[i][j] == 1:
                continue
            if i != 0:
                if ship_grid[i-1][j] == 1:
                    num_open_neighbors += 1
            if i != ship_grid_D-1:
                if ship_grid[i+1][j] == 1:
                    num_open_neighbors += 1
            if j != 0:
                if ship_grid[i][j-1] == 1:
                    num_open_neighbors += 1
            if j != ship_grid_D-1:
                if ship_grid[i][j+1] == 1:
                    num_open_neighbors += 1
            if num_open_neighbors == 1:
                one_open_neighbor_cells.append((i,j))

    print("One open neighbor cells:")
    print(one_open_neighbor_cells)
    
    #break if no open cells
    if len(one_open_neighbor_cells) == 0:
        break

    #open one of thse cells at random
    if len(one_open_neighbor_cells) > 0:
        chosen_cell = one_open_neighbor_cells[random.randint(0,len(one_open_neighbor_cells)-1)]
        ship_grid[chosen_cell[0]][chosen_cell[1]] = 1

#output
print("Ship Grid:")
for i in range(ship_grid_D):
    print(ship_grid[i])


