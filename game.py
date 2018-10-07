# Hello, this is the main file
from advent import *
import time
import os
import sys
import __future__
import threading
from playsound import playsound

game = Game()
def end(self, actor, noun, words):
    print "\n\n\nWell done! \nYou completed the Libary Escape Game!\n\n\n"
    time.sleep(2)
    print """|@@@@|     |####|
|@@@@|     |####|
|@@@@|     |####|
\@@@@|     |####/
 \@@@|     |###/
  `@@|_____|##'
       (O)
    .-'''''-.
  .'  * * *  `.
 :  *       *  :
: ~   Libary ~  :
: ~   Escape ~  :
 :  *       *  :
  `.  * * *  .'
    `-.....-'\n\n\n"""
    animation = "Thanks For Playing"

    for i in range(18):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(5)
        print "By James, Owen and Matthew"


def countdown():
    floor3Key = corridoor.new_object("key", "Key to Floor 3")
    floor3.make_requirement(floor3Key)
    print("A key to the main floor 3 is now available. Use \"take key\"")
    n = 30
    while n > 0:
        time.sleep(1)
        n = n -1
        if n == 0:
           print("""You died!


                                                 .#@#';'+@@;
                                               @; ```` ```` :@`
                                             @,```````````````,@
                                            @ ````````````````  @
                                          `@ ````````````````````@
                                          @ ````````````````````` @
                                         ::` ```````````````````` ;,
                                         @`````````````````````````@
                                        ,+```````````````````````:`#`
                                        @``.`````````````````````;`.#
                                        @  ;`````````````````````+` @
                                        @``.`````````````````````;``@
                                        @`:  ````````````````````. `@
                                        @`@````` ````````````````,`.@
                                        @ ,``` ` ` ````````````  @ '@
                                        @``@.`` '+````  ` .:'+@ #'@`@
                                        @ `@@` ,;;:+# ``@:`   ``.`+ @
                                        @, ' ` `.'. `#`` ;,+##'``';,@
                                        ##,``#@@@@@@,  `#@@@@@@@:`+##
                                        .@@`'@@@@@@@@ ``@@@@@@@@@ #@,
                                         @@.@@@@@ .@@```@@@@@ +@@ @@
                                         @@:+@@@@'#@@  `@@@@@@@@# @@@
                                        .@@.:@@@@@@@'`@` @@@@@@#+`:+@
                                        ,@.,`'+@@@+:`:@@  ;+++'+ `  @
                                        ,@;`` :''.#``@@@;``    ,:``,@
                                        `@#  ``.`````@+@@ ``.;'` ` @
                                         ,@ ,. ``.``:@#@@  ;``  , @
                                          .@@;+'````+@#@@  ```@+@@`
                                           @'@@@``` `'`..`````@`#@
                                           @,'@@ ` `  ``  `.`+@ @@
                                           @..@@#,`..,  `  .'@@`.@
                                           @.`@@;'@#+#'';#,.:@@`:@
                                           @`;;@#@ ,;;  .:`#@@@`;#
                                           @`+`'+,#@#+,#+@@+.@+`++
                                           @.:`@`#;  `;'#'.+, ` #'
                                           ++#` `.`'#`,:#+,` ,``@.
                                            @@ ````   `.,, ``   @
                                            :@ ``  ```` ``` `` @;
                                             '@ :  ``````` +` @+
                                              +@ ``  ````` `.@;
                                               @@ `````` #`.@:
                                                @@`@` ``# ;@.
                                                 ;@@@@@@@@@`
                                                     ````
           """)
           os.execl(sys.executable, sys.executable, * sys.argv)

def start(self, actor, noun, words):
        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.start()

def listen(self, actor, noun, words):
    print " The lion asks: What is the worst vegetable to have on a ship?"
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
"TOP MIDDLE MAZE ROOM",
"""

 `,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,,,,,,,,,,,,,,+@@@@@@@@@@@@',,,,,,,,,,,.+
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,`````````````,````````````;````````````'
 ,`````````````,````````````;````````````'
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
 You are in the first room of a large maze.
"""
)

tlmaze = game.new_location(
"TOP LEFT MAZE ROOM",
"""
 `,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@;:,,,,,,,,,,,.',,,,,,,,,,,.+
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,`````````````,````````````;````````````'
 ,`````````````,````````````;````````````'
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

"""
)


trmaze = game.new_location(
"TOP RIGHT MAZE ROOM",
"""

 `,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,,,,,,,,,,,,,,:,,,,,,,,,,,.@@@@@@@@@@@@@+
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,`````````````,````````````;````````````'
 ,`````````````,````````````;````````````'
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

"""
)


mlmaze = game.new_location(
"MIDDLE LEFT MAZE ROOM",
"""

 `,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,,,,,,,,,,,,,,:,,,,,,,,,,,.',,,,,,,,,,,.+
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,````````````;````````````'
 ,`````````````,````````````;````````````'
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'


"""
)

mmmaze = game.new_location(
"MIDDLE MIDDLE MAZE ROOM",
"""
:
: ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: :,,,,,,,,,,,,+,,,,,,,,,,,,#,,,,,,,,,,,,@
: ,            @@@@@@@@@@@@@#            @
: ,            @@@@@@@@@@@@@#            @
: ,            @@@@@@@@@@@@@#            @
: ,            @@@@@@@@@@@@@#            @
: ,            @@@@@@@@@@@@@#            @
: ,            @@@@@@@@@@@@@#            @
: ,            @@#@@@@@@@@@@#            @
: ,            @@.@@@#;@+;@@#            @
: ,            @@.@@#,@'`@'@#            @
: ,            @@.@@#.@+.@'@#            @
: ,            @@@  Lion  @@#            @
: ,            @@@@@@@@@@@@@#            @
: ,````````````@@@@@@@@@@@@@#````````````@
: ,````````````+````````````#````````````@
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: ,            '            #            @
: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
:


"""
)
mrmaze = game.new_location(
"MIDDLE RIGHT MAZE ROOM",
"""

 `,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,,,,,,,,,,,,,,:,,,,,,,,,,,.',,,,,,,,,,,.+
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,`````````````,````````````@@@@@@@@@@@@@'
 ,`````````````,````````````;````````````'
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

"""
)
brmaze = game.new_location(
"BOTTOM RIGHT MAZE ROOM",
"""

 `,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,,,,,,,,,,,,,,:,,,,,,,,,,,.',,,,,,,,,,,.+
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,`````````````,````````````;````````````'
 ,`````````````,````````````@@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@@@@@@@@@@@@'
 ,             ,            @@:;;@@@+@@@@'
 ,             ,            @@:'+#@+:##@@'
 ,             ,                 Exit    '
 ,             ,            @@;`.,@.;@.@@'
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

"""
)
blmaze = game.new_location(
"BOTTOM LEFT MAZE ROOM",
"""

 `,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,,,,,,,,,,,,,,:,,,,,,,,,,,.',,,,,,,,,,,.+
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,`````````````,````````````;````````````'
 ,@@@@@@@@@@@@@,````````````;````````````'
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@`;'@@@'+@@@,            ;            '
 ,@@`'#;#@`+#@@,            ;            '
 ,@@`@@@`@`+@@@,            ;            '
 ,@@.` EXIT  @@,            ;            '
 ,@@@@@@@@@@@@@,            ;            '
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
"""
)

bmmaze = game.new_location(
"BOTTOM MIDDLE MAZE ROOM",
"""

 `,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,,,,,,,,,,,,,,:,,,,,,,,,,,.',,,,,,,,,,,.+
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,             ,            ;            '
 ,`````````````,````````````;````````````'
 ,`````````````@@@@@@@@@@@@@;````````````'
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,             @@@@@@@@@@@@@;            '
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

"""
)
floor1 = game.new_location(
"Floor 1",
"""
Type END\
""")

stairs = game.new_connection("Stairs", floor5, floor4, [IN, DOWN], [UP, OUT])
fire_escape = game.new_connection("Side Room", floor4, side4, [IN, WEST], [EAST, OUT])
floor3stairs = game.new_connection("Stairs", floor4, corridoor, [IN, DOWN], [UP, OUT])
corridorrFloor3 = game.new_connection("Continue to Floor 3", corridoor, floor3, [IN, WEST], [EAST, OUT])
maze1 = game.new_connection("Maze 1", floor3, tlmaze, [IN, WEST], [EAST, OUT])
maze2 = game.new_connection("Maze 2", floor3, trmaze, [IN, EAST], [WEST, OUT])
maze3 = game.new_connection("Maze 3", mlmaze, tlmaze, [IN, NORTH], [SOUTH, OUT])
maze4 = game.new_connection("Maze 4", mmmaze, floor3, [IN, NORTH], [SOUTH, OUT])
maze5 = game.new_connection("Maze 5", mrmaze, trmaze, [IN, NORTH], [SOUTH, OUT])
maze6 = game.new_connection("Maze 6", mlmaze, mmmaze, [IN, EAST],  [WEST, OUT])
maze7 = game.new_connection("Maze 7", mrmaze, mmmaze, [IN, WEST], [EAST, OUT])
maze8 = game.new_connection("Maze 8", blmaze, mlmaze, [IN, NORTH], [SOUTH, OUT])
maze9 = game.new_connection("Maze 9", bmmaze, mmmaze, [IN, NORTH], [SOUTH, OUT])
maze10 = game.new_connection("Maze 10", brmaze, mrmaze, [IN, NORTH], [SOUTH, OUT])
maze11 = game.new_connection("Maze 11", blmaze, bmmaze, [IN, EAST], [WEST, OUT])
maze12 = game.new_connection("Maze 12", brmaze, bmmaze, [IN, WEST], [EAST, OUT])
maze13 = game.new_connection("Maze 13", blmaze, floor5, [IN, SOUTH], [NORTH, OUT])
maze14 = game.new_connection("Maze 14", brmaze, floor1, [IN, SOUTH], [NORTH, OUT])

user = game.new_player(floor5)
user.add_verb(Verb(listen, "listen"))
user.add_verb(Verb(start, "start"))
user.add_verb(Verb(end, "end"))
game.run()
