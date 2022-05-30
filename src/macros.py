global CurrLoc

#State Assignemnts
BUFFER = 0
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
LAND = 5
INTERRUPT = False 

TIMEOUT = 3

XOffset = 5
YOffset = 5
ZOffset = -5

keybinds = {
    "w": UP,
    "a": LEFT,
    "s": DOWN,
    "d": RIGHT,
    "q": BUFFER,
    "e": LAND
}