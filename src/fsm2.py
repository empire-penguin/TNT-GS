#Implementing FSM
import keyboard
import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)

import time
from os.path import exists

async def fsm2(connection):

    CurrLoc = (0,0,0,0)
    #Intialize CurrLoc as a tuple instead of a list to preserve parameter order
    #Initalize Curr Loc earlier
    #Read documentation to understand 4th 4-tuple orientation angle 
    XOffset = 5
    YOffset = 5
    ZOffset = -5

    #State Assignemnts
    BUFFER = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    INTERRUPT = false #TODO implement spacebar input

    async def buffer():
        # TODO this function may require a rework
        print("-- Maintain current position")
        await connection.offboard.set_position_ned(PositionNedYaw(CurrLoc))
        await asyncio.sleep(10)
    async def left():
        print("-- Move five meters to the left")
        CurrLoc[1] -= YOffset
        await connection.offboard.set_position_ned(PositionNedYaw(CurrLoc))
        await asyncio.sleep(10)
    async def right():
        print("-- Move five meters to the right")
        CurrLoc[1] += YOffset
        await connection.offboard.set_position_ned(PositionNedYaw(CurrLoc))
        await asyncio.sleep(10)
    async def up():
        print("-- Move five meters up")
        CurrLoc[2] += ZOffset
        await connection.offboard.set_position_ned(PositionNedYaw(CurrLoc))
        await asyncio.sleep(10)
    async def down():
        print("-- Move five meters down")
        CurrLoc[2] -= ZOffset
        await connection.offboard.set_position_ned(PositionNedYaw(CurrLoc))
        await asyncio.sleep(10)
    async def land():
        print("-- Land")
        CurrLoc = (0,0,0,0)
        await connection.offboard.set_position_ned(PositionNedYaw(CurrLoc))
        await connection.action.land()
        # look for the function that checks if youve gotten where you need to be
        await asyncio.sleep(60)

    #TODO, change Rotation

    switcher = {
    BUFFER: buffer(),
    LEFT: left(),
    RIGHT: right(),
    UP: up(),
    DOWN: down(),
    }

    def switch(input_num):
        return switcher.get(input_num)

    flag = 1

    i = 0
    signals = [3,3,0,2,0,1,0,4,0]

    while not INTERRUPT:
        # signal = get signal number 0-6 from LSL function
        if flag == 1:
            switch(signals[i])
            flag = 0
        else:
            switch(0)
        if signals[i] == 0:
            flag = 1 
        i += 1

        if i == 9:
            break
    
    land()