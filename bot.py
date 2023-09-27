# from ship import Ship
class Bot():
    def __init__(self, ship, bot_type, bot_pos):
        self.ship = ship
        self.bot_type = bot_type
        self.bot_pos = bot_pos
        if self.bot_type == 1:
            self.move = self.move_type_1
        elif self.bot_type == 2:
            self.move = self.move_type_2
        elif self.bot_type == 3:
            self.move = self.move_type_3
        elif self.bot_type == 4:
            self.move = self.move_type_4

    
    
    def move_type_1(self):
        print("move1")
        
        path = []
        visited = []
        fringe = []
        parent = self.bot_pos
        fringe.append(self.bot_pos)
        while fringe:
            curr = fringe.pop(0)
            if self.ship.ship_grid[curr[0]][curr[1]] == 3:
                print("Congrats! You found the button! The fire is out!")
                return 1
            elif self.ship.ship_grid[curr[0]][curr[1]] == -1:
                print("Sorry, you lost the game. The fire got you.")
                return -1
            for child in self.get_children(curr, parent):
                fringe.append(child)
                parent = curr
                visited.append(child)
            
                
        
    def move_type_2(self):
        pass
    def move_type_3(self):
        pass
    def move_type_4(self):
        pass

    def get_children(self, curr, parent):
        x = curr[0]
        y = curr[1]
        children = []
        
        if x != 0 and self.ship.ship_grid[x-1][y] == 1:
            children.append((x-1,y))
        if x != self.ship.ship_grid_D-1 and self.ship.ship_grid[x+1][y] == 1:
            children.append((x+1,y))
        if y != 0 and self.ship.ship_grid[x][y-1] == 1:
            children.append((x,y-1))
        if y != self.ship.ship_grid_D-1 and self.ship.ship_grid[x][y+1] == 1:
            children.append((x,y+1))
        if parent in children:
            children.remove(parent)
            
        