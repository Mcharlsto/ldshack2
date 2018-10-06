# Hello, this is the main file
from advent import *
import time

game = Game()

#Needs implementing
def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n = n -1
        if n == 0:
           print("Times up!")
           os.execl(sys.executable, sys.executable, * sys.argv)


def listen(self, actor, noun, words):
    print "What is the worst vegetable to have on a ship?"
    print "Enter answer"
    global input
    input = raw_input()
    if "leek" in input.lower():
        print "You Win. The frog drops a key. You can use \"take key\" to collect it."
        side4key = side4.new_object("key", "Key to the Elevator")
        floor3.make_requirement(side4key)
    else:
        print "Try Again"
        listen(0,0,0,0)


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
As soon as you reach the bottom of the stairs, a laptop on a table explodes into a sea of flames. There is a wooden door to the west. There is a staircase to floor 3, but it is locked. You don't have long before the fire spreads.
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

floor3 = game.new_location(
"Floor 3",
"""
Welcome to floor 3. You only have 100 seconds before you will die due to the extreme heat."
"""
)

stairs = game.new_connection("Stairs", floor5, floor4, [IN, DOWN], [UP, OUT])
fire_escape = game.new_connection("Side Room", floor4, side4, [IN, WEST], [EAST, OUT])
floor3stairs = game.new_connection("Stairs", floor4, floor3, [IN, DOWN], [UP, OUT])
user = game.new_player(floor5)
user.add_verb(Verb(listen, "listen"))


game.run()

