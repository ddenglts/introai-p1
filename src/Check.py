from typing import List, Tuple, Dict

def bot_on_fire(grid: List[List[int]], bot_pos: Tuple[int, int]) -> bool:
    """
    Returns True if the bot is on fire, False otherwise.
    """
    if grid[bot_pos[0]][bot_pos[1]] == -1:
        ###p.rint("Sorry, you have been burned to a crisp.")
        ###p.rint("bot on fire:", bot_pos)
        return True
    return False
def bot_on_button(grid: List[List[int]], bot_pos: Tuple[int, int]) -> bool:
    """
    Returns True if the bot is on a button, False otherwise.
    """
    if grid[bot_pos[0]][bot_pos[1]] == 2:
        ###p.rint("Congratulations! You have reached the goal!")
        ###p.rint("bot on button:", bot_pos)
        return True
    return False