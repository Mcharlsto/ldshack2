# Hello, this is the main file
from advent import *
import time
import os
import sys
import __future__
game = Game()

def start(self, actor, noun, words):
    floor3Key = corridoor.new_object("key", "Key to Floor 3")
    floor3.make_requirement(floor3Key)
    print("A key to the main floor 3 is now available. Use \"take key\"")
    n = 100
    while n > 0:
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
    if "leek" or "leak" in input.lower():
        print "You Win. The frog drops a key. You can use \"take key\" to collect it."
        side4key = side4.new_object("key", "Key to the Elevator")
        corridoor.make_requirement(side4key)
    else:
        print "Try Again"
        listen(0,0,0,0)


floor5 = game.new_location(
"Floor 5",
"""
    __    _ __                             ______
   / /   (_) /_  _________ ________  __   / ____/_____________ _____  ___
  / /   / / __ \/ ___/ __ `/ ___/ / / /  / __/ / ___/ ___/ __ `/ __ \/ _ \
 / /___/ / /_/ / /  / /_/ / /  / /_/ /  / /___(__  ) /__/ /_/ / /_/ /  __/
/_____/_/_.___/_/   \__,_/_/   \__, /  /_____/____/\___/\__,_/ .___/\___(_)
                              /____/                        /_/
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
You are in a small side room, a lion is standing in its center.
Commands - listen, east
"""
)

corridoor = game.new_location(
"Corridoor",
"""
You have reached a corridoor at the bottom of the stairs. The room ahead is very hot and you can't survive in there for very long. Type start then get the key then advance to the next room.
Commands - start then west
"""
)

floor3 = game.new_location(
"Floor 3",
"""
Description goes here.
"""
)

stairs = game.new_connection("Stairs", floor5, floor4, [IN, DOWN], [UP, OUT])
fire_escape = game.new_connection("Side Room", floor4, side4, [IN, WEST], [EAST, OUT])
floor3stairs = game.new_connection("Stairs", floor4, corridoor, [IN, DOWN], [UP, OUT])
secret = game.new_connection("Secret", floor5, side4, [IN, WEST], [EAST, OUT])
corridorrFloor3 = game.new_connection("Continue to Floor 3", corridoor, floor3, [IN, WEST], [EAST, OUT])
user = game.new_player(floor5)
user.add_verb(Verb(listen, "listen"))
user.add_verb(Verb(start, "start"))
game.run()
