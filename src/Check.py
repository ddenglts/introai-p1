from typing import List, Tuple, Dict

def bot_on_fire(grid: List[List[int]], bot_pos: Tuple[int, int]) -> bool:
    """
    Returns True if the bot is on fire, False otherwise.
    """
    if grid[bot_pos[0]][bot_pos[1]] == -1:
        print("Sorry, you have been burned to a crisp.")
        print("bot on fire:", bot_pos)
        return True
    return False
def bot_on_button(grid: List[List[int]], bot_pos: Tuple[int, int]) -> bool:
    """
    Returns True if the bot is on a button, False otherwise.
    """
    if grid[bot_pos[0]][bot_pos[1]] == 2:
        print("Congratulations! You have reached the goal!")
        print("bot on button:", bot_pos)
        return True
    return False