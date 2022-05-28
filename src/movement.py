import keyboard
import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)

from macros import *

async def buffer(connection, CurrLoc):
    # TODO this function may require a rework
    print("-- Maintain current position")
    await connection.offboard.set_position_ned(CurrLoc)
    await asyncio.sleep(TIMEOUT)
async def left(connection, CurrLoc):
    print("-- Move five meters to the left")
    CurrLoc.east_m -= YOffset
    await connection.offboard.set_position_ned(CurrLoc)
    await asyncio.sleep(TIMEOUT)
async def right(connection, CurrLoc):
    print("-- Move five meters to the right")
    CurrLoc.east_m += YOffset
    await connection.offboard.set_position_ned(CurrLoc)
    await asyncio.sleep(TIMEOUT)
async def up(connection, CurrLoc):
    print("-- Move five meters up")
    CurrLoc.down_m += ZOffset
    await connection.offboard.set_position_ned(CurrLoc)
    await asyncio.sleep(TIMEOUT)
async def down(connection, CurrLoc):
    print("-- Move five meters down")
    CurrLoc.down_m -= ZOffset
    await connection.offboard.set_position_ned(CurrLoc)
    await asyncio.sleep(TIMEOUT)
async def land(connection, CurrLoc):
    print("-- Land")
    CurrLoc = PositionNedYaw(0,0,-5,0)
    await connection.offboard.set_position_ned(CurrLoc)
    await connection.action.land()
    # look for the function that checks if youve gotten where you need to be
    await asyncio.sleep(60)