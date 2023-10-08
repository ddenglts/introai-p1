from typing import List, Tuple, Dict

def bot_on_fire(grid: List[List[int]], bot_pos: Tuple[int, int]) -> bool:
    """
    Returns True if the bot is on fire, False otherwise.
    """
    return grid[bot_pos[0]][bot_pos[1]] == -1
def bot_on_button(grid: List[List[int]], bot_pos: Tuple[int, int]) -> bool:
    """
    Returns True if the bot is on a button, False otherwise.
    """
    return grid[bot_pos[0]][bot_pos[1]] == 3