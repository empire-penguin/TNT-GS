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


#Intialize CurrLoc as a tuple instead of a list to preserve parameter order
#Initalize Curr Loc earlier
#Read documentation to understand 4th 4-tuple orientation angle 
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