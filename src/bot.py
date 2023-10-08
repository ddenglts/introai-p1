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
    
    def _move_1(self, grid: List[List[int]], button: Tuple[int, int]) -> bool:
        """
        Moves the bot one step closer to the goal, using the BFS algorithm.
        Returns True if the bot moved once successfully, False if no path was found.
        """
        # get the path to the goal
        if not self.path:
            self.path = Algo.bfs(grid, self.pos, button)
            print(self.path)
            if self.path == None:
                return False
            #pop starting position so [0] is next move
            self.path.pop(0)
            
        
        
        # move the bot
        self.pos = self.path.pop(0)
        return True