#Implementing FSM
from ctypes import sizeof
from signal import signal
import keyboard
import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)

import time
from os.path import exists
import queue

from macros import *
from movement import (buffer, left, right, up, down, land)


async def fsm2(connection):

    CurrLoc = PositionNedYaw(0,0,-5,0)

    flag = 1
    lander = 0
    
    #signals = [UP,UP,BUFFER,RIGHT,BUFFER,LEFT,BUFFER,DOWN]
    signals = []

    while not lander:

        #get user input from keyboard
        val = input("Enter wasd input ")
        signals.append(keybinds.get(val))
        print(len(signals))
        
        # signal = get signal number 0-6 from LSL function
        if flag == 1:
            if (signals[0] == BUFFER):
                await buffer(connection, CurrLoc)
            elif (signals[0] == LEFT):
                await left(connection, CurrLoc)
            elif (signals[0] == RIGHT):
                await right(connection, CurrLoc)
            elif (signals[0] == UP):
                await up(connection, CurrLoc)
            elif (signals[0] == DOWN):
                if CurrLoc.down_m < -5:
                    await down(connection, CurrLoc)
                else:
                    print("Cannot go down anymore")
            elif (signals[0] == LAND):
                await land(connection, CurrLoc)
                lander = 1
                break
            flag = 0
            signals.pop(0)
        else:
            await buffer(connection, CurrLoc)
        if len(signals) > 0:
            if signals[0] == BUFFER:
                flag = 1 
            if signals[0] == LAND:
                await land(connection, CurrLoc)
                lander = 1
                break
            signals.pop(0)
        
        

    #await land(connection, CurrLoc)