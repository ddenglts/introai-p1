import random
class Fire:
    # @param ship ship object
    # @param fire_pos (i, j) in ship_grid
    def __init__(self, ship, init_fire_pos):
        self.grid = ship.ship_grid
        self.q = ship.q
        self.on_fire_cells = []
        self.on_fire_cells.append(init_fire_pos)
        
    def spread(self):
        future_on_fire_cells = []
        for cell in self.on_fire_cells:
            adj = []
            k = 0
            x = cell[0]
            y = cell[1]
            
            if self.grid[x][y] == 1:
                #right neighbor
                if self.grid[x+1][y] and self.grid[x+1][y] == 1:
                    adj.append((x+1,y))
                elif self.grid[x+1][y] and self.grid[x+1][y] == -1:
                    k += 1
                #left neighbor
                if self.grid[x-1][y] and self.grid[x-1][y] == 1:
                    adj.append((x-1,y))
                elif self.grid[x-1][y] and self.grid[x-1][y] == -1:
                    k += 1
                #up neighbor
                if self.grid[x][y+1] and self.grid[x][y+1] == 1:
                    adj.append((x,y+1))
                elif self.grid[x][y+1] and self.grid[x][y+1] == -1:
                    k += 1
                #down neighbor
                if self.grid[x+1][y] and self.grid[x][y-1] == 1:
                    adj.append((x,y-1))
                elif self.grid[x][y-1] and self.grid[x][y-1] == -1:
                    k += 1
            rand = 1 - (1 - self.q)**k
            if random.random() <= rand:
                
                future_on_fire_cells.append((x,y))
        
        #update ship grid to spread calculations
        for i in future_on_fire_cells:
            self.grid[i[0]][i[1]] = -1
            self.on_fire_cells.append((x,y))

            
            
            