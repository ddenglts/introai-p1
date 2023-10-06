# from ship import Ship
class Bot():
    def __init__(self, ship, bot_type, bot_pos):
        self.ship = ship
        self.bot_type = bot_type
        self.bot_pos = bot_pos
        self.path = []
        if self.bot_type == 1:
            self.move = self.move_type_1
        elif self.bot_type == 2:
            self.move = self.move_type_2
        elif self.bot_type == 3:
            self.move = self.move_type_3
        elif self.bot_type == 4:
            self.move = self.move_type_4
        

    def get_bot_pos(self):
        return self.bot_pos
    

    def move_type_1(self):
        
        print("move1")

        if not self.path:
            parents = {}  # Create the parents dictionary
            fringe = [self.bot_pos]

            while fringe:
                curr = fringe.pop(0)
                
                if self.ship.ship_grid[curr[0]][curr[1]] == 3:
                    
                    # Backtracking
                    self.path = []
                    while curr in parents:
                        self.path.append(curr)
                        curr = parents[curr]
                    self.path.append(self.bot_pos)
                    self.path.reverse()  # From start to goal
                    print("Path:", self.path)
                    break
                

                children_array = self.get_children(curr)
                for child in children_array:
                    if child not in parents:  # Check if we haven't visited this child before, VERY POOR COMPLEXITY(TRY TO FIX LATER)
                        fringe.append(child)
                        parents[child] = curr  # Set the parent of this child

            return False
        
        #move based on path

        self.bot_pos = self.path.pop(0)
        #ship will check fire collision

        return True


    def move_type_2(self):
        print("move2")

        parents = {}  # Create the parents dictionary
        fringe = [self.bot_pos]

        while fringe:
            curr = fringe.pop(0)
            
            if self.ship.ship_grid[curr[0]][curr[1]] == 3:
                print("Congrats! You found the button! The fire is out!")
                return True
                
                # Backtracking
                self.path = []
                while curr in parents:
                    self.path.append(curr)
                    curr = parents[curr]
                self.path.append(self.bot_pos)
                self.path.reverse()  # From start to goal
                print("Path:", self.path)
                break
            

            children_array = self.get_children(curr)
            for child in children_array:
                if child not in parents:  # Check if we haven't visited this child before, VERY POOR COMPLEXITY(TRY TO FIX LATER)
                    fringe.append(child)
                    parents[child] = curr  # Set the parent of this child
        
        if not fringe: return False #no path found

        #move based on path

        self.bot_pos = self.path.pop(0)
        #ship will check fire collision

        return True
    

    def move_type_3(self):
        parents = {}  # Create the parents dictionary
        fringe = [self.bot_pos]

        while fringe:
            curr = fringe.pop(0)
            
            if self.ship.ship_grid[curr[0]][curr[1]] == 3:
                print("Congrats! You found the button! The fire is out!")
                
                # Backtracking
                self.path = []
                while curr in parents:
                    self.path.append(curr)
                    curr = parents[curr]
                self.path.append(self.bot_pos)
                self.path.reverse()  # From start to goal
                print("Path:", self.path)
                break
            

            children_array = self.get_safe_children(curr)
            for child in children_array:
                if child not in parents:  # Check if we haven't visited this child before, VERY POOR COMPLEXITY(TRY TO FIX LATER)
                    fringe.append(child)
                    parents[child] = curr  # Set the parent of this child
        
        if not fringe: return self.move_type_2() #no path found

        #move based on path

        self.bot_pos = self.path.pop(0)
        #ship will check fire collision

        return True




    # like get_children except it only returns children that are not next to a fire cell
    def get_safe_children(self, curr):
        children = self.get_children(curr)
        safe_children = []
        for child in children:
            x, y = child
            if x != 0 and self.ship.ship_grid[x-1][y] == 0:
                safe_children.append((x-1, y))
            if x != self.ship.ship_grid_D-1 and self.ship.ship_grid[x+1][y] == 0:
                safe_children.append((x+1, y))
            if y != 0 and self.ship.ship_grid[x][y-1] == 0:
                safe_children.append((x, y-1))
            if y != self.ship.ship_grid_D-1 and self.ship.ship_grid[x][y+1] == 0:
                safe_children.append((x, y+1))
        if not safe_children:
            return False
        return safe_children
            

    def get_children(self, curr):
        x, y = curr
        children = []
        # Check surrounding positions in grid
        if x != 0 and self.ship.ship_grid[x-1][y] == 1:
            children.append((x-1, y))
        if x != self.ship.ship_grid_D-1 and self.ship.ship_grid[x+1][y] == 1:
            children.append((x+1, y))
        if y != 0 and self.ship.ship_grid[x][y-1] == 1:
            children.append((x, y-1))
        if y != self.ship.ship_grid_D-1 and self.ship.ship_grid[x][y+1] == 1:
            children.append((x, y+1))
        return children