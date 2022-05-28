def buffer():
    # TODO this function may require a rework
    print("-- Maintain current position")
    await drone.offboard.set_position_ned(PositionNedYaw(CurrLoc))
    await asyncio.sleep(10)
def left():
    print("-- Move five meters to the left")
    CurrLoc[1] -= YOffset
    await drone.offboard.set_position_ned(PositionNedYaw(CurrLoc))
    await asyncio.sleep(10)
def right():
    print("-- Move five meters to the right")
    CurrLoc[1] += YOffset
    await drone.offboard.set_position_ned(PositionNedYaw(CurrLoc))
    await asyncio.sleep(10)
def up():
    print("-- Move five meters up")
    CurrLoc[2] += ZOffset
    await drone.offboard.set_position_ned(PositionNedYaw(CurrLoc))
    await asyncio.sleep(10)
def down():
    print("-- Move five meters down")
    CurrLoc[2] -= ZOffset
    await drone.offboard.set_position_ned(PositionNedYaw(CurrLoc))
    await asyncio.sleep(10)
def land();
    print("-- Land")
    await drone.action.land()
    await asyncio.sleep(60)