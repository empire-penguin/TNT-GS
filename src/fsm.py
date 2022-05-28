#Implementing FSM

#MAVSDK imports for flying functions
import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)

#State Assignemnts
BUFFER = 0
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
INTERRUPT = #SPACE KEYINPUT TODO

#TODO, change Rotation

#North, East, Down, Degrees toward East
CurrLoc = (0,0,0,0)
XOffset = 5;
YOffset = 5;
ZOffset = 5;

while(! INTERRUPT):
  def buffer():
    return #TODO
  def left():
    return #TODO
  def right():
    return #TODO
  def up():
    print("-- Go 0m North, 0m East, -5m Down within local coordinate system, turn to face East")
    CurrLoc[2] -= YOffset
    await drone.offboard.set_position_ned(PositionNedYaw(CurrLoc))
    await asyncio.sleep(10)
  def down():
    print("-- Go 0m North, 0m East, +5m Down within local coordinate system, turn to face East")
    CurrLoc[2] += YOffset
    await drone.offboard.set_position_ned(PositionNedYaw(CurrLoc))
    await asyncio.sleep(10)
    return #TODO

  switcher = {
      BUFFER: buffer,
      LEFT: left,
      RIGHT: right,
      UP: up,
      DOWN: down,
  }

  def switch(input_num):
      return switcher.get(input_num, default)()
else:
  
 #TODO: Landing Protocol

