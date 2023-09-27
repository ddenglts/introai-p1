from bot import Bot
import random
class Ship():
    
    def __init__(self, ship_grid_D):
        self.ship_grid_D = ship_grid_D
        self.q = random.random(0,1)
        self.ship_grid = [] #D*D int array
        # self.ship_grid = self.build()
        self.bot = Bot(self, 1, (0,0))
                
        
       
        
    def build(self):
       #ship_grid creation
        for i in range(self.ship_grid_D):
            self.ship_grid.append([])
            for j in range(self.ship_grid_D):
                self.ship_grid[i].append(0)

        #randomly open 1 interior cell
        self.ship_grid[random.randint(1,self.ship_grid_D-2)][random.randint(1,self.ship_grid_D-2)] = 1

        while True:
            print("Ship Grid:")
            for i in range(self.ship_grid_D):
                print(self.ship_grid[i])
            #find all cells with one open neighbor
            one_open_neighbor_cells = []
            
                #identify all closed cells that have a single open neighbor in the 4 cardinal directions
            for i in range(self.ship_grid_D):
                for j in range(self.ship_grid_D):
                    num_open_neighbors = 0
                    if self.ship_grid[i][j] == 1:
                        continue
                    if i != 0:
                        if self.ship_grid[i-1][j] == 1:
                            num_open_neighbors += 1
                    if i != self.ship_grid_D-1:
                        if self.ship_grid[i+1][j] == 1:
                            num_open_neighbors += 1
                    if j != 0:
                        if self.ship_grid[i][j-1] == 1:
                            num_open_neighbors += 1
                    if j != self.ship_grid_D-1:
                        if self.ship_grid[i][j+1] == 1:
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
                self.ship_grid[chosen_cell[0]][chosen_cell[1]] = 1

        #output
        print("Ship Grid:")
        for i in range(self.ship_grid_D):
            print(self.ship_grid[i])

        dead_ends = []
            
        for i in range(self.ship_grid_D):
            for j in range(self.ship_grid_D):
                #check to see if cell is open
                num_open_neighbors = 0
                if self.ship_grid[i][j] == 1:
                    if i != 0:
                        if self.ship_grid[i-1][j] == 1:
                            num_open_neighbors += 1
                    if i != self.ship_grid_D-1:
                        if self.ship_grid[i+1][j] == 1:
                            num_open_neighbors += 1
                    if j != 0:
                        if self.ship_grid[i][j-1] == 1:
                            num_open_neighbors += 1
                    if j != self.ship_grid_D-1:
                        if self.ship_grid[i][j+1] == 1:
                            num_open_neighbors += 1
                    if num_open_neighbors == 1:
                        dead_ends.append((i,j))
        
        print("Dead ends unedited:")   
        print(dead_ends)           
        num_dead_ends = len(dead_ends)/2
        c = 0

        while c < num_dead_ends:
            dead_ends.pop(random.randint(0,len(dead_ends)-1))
            c += 1
        print("Dead ends:")   
        print(dead_ends)

        opening_cell = []
        for i in range(len(dead_ends)):
            r = dead_ends[i][0]
            c = dead_ends[i][1]
            if r != 0:
                if self.ship_grid[r-1][c] == 0:
                    opening_cell.append((r-1,c))
            if r != self.ship_grid_D-1:
                if self.ship_grid[r+1][c] == 0:
                    opening_cell.append((r+1,c))
            if c != 0:
                if self.ship_grid[r][c-1] == 0:
                    opening_cell.append((r,c-1))
            if c != self.ship_grid_D-1:
                if self.ship_grid[r][c+1] == 0:
                    opening_cell.append((r,c+1))
            cell_to_open = opening_cell[(random.randint(0,len(opening_cell)-1))]
            self.ship_grid[cell_to_open[0]][cell_to_open[1]] = 1



        for j in range(self.ship_grid_D):
            print(self.ship_grid[j])
            

        #Spawn fire
        fire = {}
        # Will keep track of neighbors that are on fire
        fire.location = (random.randint(0,self.ship_grid_D-1),random.randint(0,self.ship_grid_D-1))
        #redo generation if fire spawns on ship
        while self.ship_grid[fire.location[0]][fire.location[1]] == 0:
            fire.location = (random.randint(0,self.ship_grid_D-1),random.randint(0,self.ship_grid_D-1))

        self.ship_grid[fire.location[0]][fire.location[1]] == -1


        #timestep loop







        print("HELLO WORLD")


                        
                    
                    
                    
    

