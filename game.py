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
Placeholder
"""
)

stairs = game.new_connection("Stairs", floor5, floor4, [IN, DOWN], [UP, OUT])

user = game.new_player(floor5)

game.run()
