"""
Questions to ask TA: 
Is it required to worry about cases where we fix multiple dead ends at once? This causes as us to have to 
constantly recheck the amount of dead ends we have closed during one iteration of the loop

Can the fire and button be in the same cell?
"""
from ship import Ship
import time


# Create initial state (ship, bot, button, fire)

# create ship with size 5, bot type 1
ship = Ship(7, 1)
# build ship
ship.build()
# place bot
ship.place_bot()
# place button
ship.place_button()
# place fire
#ship.place_fire()

ship.manual_set()

# time loop
while True:
    print("before timestep")
    for row in ship.ship_grid:
        print(row)
    print("bot position: ", ship.bot.get_bot_pos())

    if ship.bot.move():
        print("Bot is stuck. GAME OVER!!!!!")
        break
    #if ship.is_bot_on_fire():
        print("Bot is on fire. YOU LOSE!!!!!")
        break
    if ship.is_bot_on_button():
        print("Bot is on button. YOU WIN!!!!!")
        break
    # spread fire
    #ship.fire.spread()
    #if ship.is_bot_on_fire():
        print("Bot is on fire. YOU LOSE!!!!!")
        break
    print("before timestep")
    for row in ship.ship_grid:
        print(row)
    print("bot position: ", ship.bot.get_bot_pos())
    #input("Press Enter to continue...")
    


print("CODE WENT THROUGH MAIN")