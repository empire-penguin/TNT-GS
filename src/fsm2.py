#Implementing FSM
from signal import signal
import keyboard
import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)

import time
from os.path import exists

from macros import *
from movement import (buffer, left, right, up, down, land)


async def fsm2(connection):

    CurrLoc = PositionNedYaw(0,0,-5,0)

    flag = 1

    i = 0
    signals = [UP,UP,BUFFER,RIGHT,BUFFER,LEFT,BUFFER,DOWN]

    while not INTERRUPT and i < len(signals):
        # signal = get signal number 0-6 from LSL function
        if flag == 1:
            if (signals[i] == BUFFER):
                await buffer(connection, CurrLoc)
            elif (signals[i] == LEFT):
                await left(connection, CurrLoc)
            elif (signals[i] == RIGHT):
                await right(connection, CurrLoc)
            elif (signals[i] == UP):
                await up(connection, CurrLoc)
            elif (signals[i] == DOWN):
                await down(connection, CurrLoc)
            elif (signals[i] == LAND):
                await land(connection, CurrLoc)
            flag = 0
        else:
            await buffer(connection, CurrLoc)
        if signals[i] == BUFFER:
            flag = 1 
        i += 1

    await land(connection, CurrLoc)