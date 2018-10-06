# Hello, this is the main file
from advent import *
game = Game()

floor5 = game.new_location(
"Floor 5",
"""
You are on floor five of a large library.
The place is deserted.
You cannot see the room.
Your laptop is on the floor below.
Commands - down
"""
)

floor4 = game.new_location(
"Floor 4",
"""
As soon as you reach the bottom of the stairs, a laptop on a table explodes into a sea of flames. There is a wooden door to the west. You don't have long before you will die.
Commands - west
"""
)

side4 = game.new_location(
"Side Room",
"""
You are in a side room, a lion is infront of you.
Commands - listen, east
"""
)

stairs = game.new_conne4ection("Stairs", floor5, floor4, [IN, DOWN], [UP, OUT])
fire_escape = game.new_connection("Escape", floor4, side4, [IN, WEST], [EAST, OUT])
user = game.new_player(floor5)
side4key = side4.new_object("Key", "Key to the Elevator")

game.run()
59
