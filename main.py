"""
Questions to ask TA: 
Is it required to worry about cases where we fix multiple dead ends at once? This causes as us to have to 
constantly recheck the amount of dead ends we have closed during one iteration of the loop

Can the fire and button be in the same cell?
"""
from ship import Ship


# Create initial state (ship, bot, button, fire)

# create ship with size 5, bot type 1
ship = Ship(100, 3)
# build ship
ship.build()
# place bot
ship.place_bot()
# place button
ship.place_button()
# place fire
ship.place_fire()

# time loop
while True:
    print("before timestep")
    print()
    if not ship.bot.move():
        print("Bot is stuck. GAME OVER!!!!!")
        break
    if ship.is_bot_on_fire():
        print("Bot is on fire. YOU LOSE!!!!!")
        break
    if ship.is_bot_on_button():
        print("Bot is on button. YOU WIN!!!!!")
        break
    # spread fire
    ship.spread()
    if ship.is_bot_on_fire():
        print("Bot is on fire. YOU LOSE!!!!!")
        break
    input("Press Enter to continue...")
    


print("CODE WENT THROUGH MAIN")