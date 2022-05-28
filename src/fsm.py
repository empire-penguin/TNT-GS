#Implementing FSM

#MAVSDK imports for flying functions
import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)

BUFFER = 0
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
INTERRUPT = #SPACE KEYINPUT TODO

while(! INTERRUPT):
  def buffer():
    return #TODO
  def left():
    return #TODO
  def right():
    return #TODO
  def up():
    return #TODO
  def down():
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

