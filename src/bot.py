from typing import Tuple, List, Dict
import Algo
class Bot():
    def __init__(self, bot_type: int, pos: Tuple[int, int]) -> None:
        self.pos = pos
        self.path = []
        if bot_type == 1:
            self.move = self._move_1
        elif bot_type == 2:
            self.move = self._move_2
        elif bot_type == 3:
            self.move = self._move_3
        elif bot_type == 4:
            self.move = self._move_4
    
    def _move_1(self, grid: List[List[int]]) -> bool:
        """
        Moves the bot one step closer to the goal, using the BFS algorithm.
        Returns True if the bot moved once successfully, False if no path was found.
        """
        button_pos = Algo.find(grid, 2)
        if (button_pos == None):
            ###p.rint("!!! No button found")
            return False

        # get the path to the goal
        if not self.path:
            self.path = Algo.bfs(grid, self.pos, button_pos)
            if self.path == None:
                ###p.rint("Sorry you have been burned to a crisp")
                ###p.rint("No path found")
                return False
            #pop starting position so [0] is next move
            self.path.pop(0)
            
        
        
        # move the bot
        self.pos = self.path.pop(0)
        return True
    def _move_2(self, grid: List[List[int]]) -> bool:
        """
        Moves the bot one step closer to the goal, using the BFS algorithm.
        Returns True if the bot moved once successfully, False if no path was found.
        """
        button_pos = Algo.find(grid, 2)
        if (button_pos == None):
            ###p.rint("!!! No button found")
            return False

        # get the path to the goal

        self.path = Algo.bfs(grid, self.pos, button_pos)
        if self.path == None:
            ###p.rint("Sorry you have been burned to a crisp")
            ###p.rint("No path found")
            return False
        #pop starting position so [0] is next move
        self.path.pop(0)
        # move the bot
        self.pos = self.path.pop(0)
        return True
        
    def _move_3(self, grid: List[List[int]]) -> bool:
        button_pos = Algo.find(grid, 2)
        cautious_grid = Algo.cautious(grid)
        if (button_pos == None):
            ###p.rint("!!! No button found")
            return False

        # get the path to the goal

        self.path = Algo.bfs(cautious_grid, self.pos, button_pos)
        
        if self.path == None:
            self.path = Algo.bfs(grid, self.pos, button_pos)
            if self.path == None:
                ###p.rint("Sorry you have been burned to a crisp")
                ###p.rint("No path found")
                return False
        #pop starting position so [0] is next move
        self.path.pop(0)

        self.pos = self.path.pop(0)
        return True
    
    
    def _move_4(self, grid: List[List[int]]) -> bool:
        """
        Moves the bot one step closer to the goal, using the A* algorithm and also integrates the behavior of Bot 3.
        Returns True if the bot moved once successfully, False if no path was found.
        """
        button_pos = Algo.find(grid, 2)
        if (button_pos == None):
            # print("!!! No button found")
            return False

        # Step 1: Use A* on the cautious_grid
        cautious_grid = Algo.cautious(grid)
        self.path = Algo.a_star(cautious_grid, self.pos, button_pos)

        # Step 2: If no path is found in cautious_grid, use A* on the actual grid
        if self.path == None:
            self.path = Algo.a_star(grid, self.pos, button_pos)
            
        # Step 3: If still no path is found, bot has failed.
        if self.path == None:
            # print("Sorry you have been burned to a crisp")
            # print("No path found")
            return False

        # If path is found, pop starting position so [0] is the next move
        self.path.pop(0)
        # move the bot
        self.pos = self.path.pop(0)
        return True