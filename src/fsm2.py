#Implementing FSM
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

    #signals = [UP,UP,BUFFER,RIGHT,BUFFER,LEFT,BUFFER,DOWN]
    signals = queue.Queue(maxsize=20)

    while not INTERRUPT and i < len(signals):

        #get user input from keyboard
        input("Enter an integer 0-5: ")
        try: 
            val = int(input)
            if not signals.full() :
                queue.append(val)
            else:
                print("Queue is full")
        except ValueError:
            print("Enter an integer")
        
        # signal = get signal number 0-6 from LSL function
        if flag == 1:
            if (signals[0] == BUFFER):
                await buffer(connection, CurrLoc)
                signals.pop(0)
            elif (signals[0] == LEFT):
                await left(connection, CurrLoc)
                signals.pop(0)
            elif (signals[0] == RIGHT):
                await right(connection, CurrLoc)
                signals.pop(0)
            elif (signals[0] == UP):
                await up(connection, CurrLoc)
                signals.pop(0)
            elif (signals[0] == DOWN):
                await down(connection, CurrLoc)
                signals.pop(0)
            elif (signals[0] == LAND):
                await land(connection, CurrLoc)
                signals.pop(0)
            flag = 0
        else:
            await buffer(connection, CurrLoc)
        if signals[i] == BUFFER:
            flag = 1 
        

    await land(connection, CurrLoc)