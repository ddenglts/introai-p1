# from ship import Ship
class Bot():
    def __init__(self, ship, bot_type, bot_pos):
        self.ship = ship
        self.bot_type = bot_type
        self.bost_pos = bot_pos
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
    def move_type_2(self):
        pass
    def move_type_3(self):
        pass
    def move_type_4(self):
        pass