import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)

import time
from os.path import exists

from fsm2 import fsm2

if (exists('/dev/tty.usbserial-0001')):
    port = '/dev/tty.usbserial-0001'
    baud = 57600
else:
    port = 'udp://'
    baud = 14550

async def run():

    # Initialize the drone
    drone = System()
    # Connect to the drone
    await drone.connect(system_address=port+':'+str(baud))

    # Wait for the drone to acknowledge connection
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    # Make sure the GPS and origin is accurate
    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    # Arm the drone
    print("-- Arming")
    await drone.action.arm()

    # Commander the drone to move to a new position
    print("-- Setting initial setpoint")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, 0.0, 0.0))

    fsm2(drone)

    # Start the remote control loop
    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    await fsm2(drone)

# # command the drone to move to a new position
# print("-- Go 0m North, 0m East, -5m Down within local coordinate system")
# await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -5.0, 0.0))
# await asyncio.sleep(10)

# print("-- Go 5m North, 0m East, -5m Down within local coordinate system, turn to face East")
# await drone.offboard.set_position_ned(PositionNedYaw(5.0, 0.0, -5.0, 90.0))
# await asyncio.sleep(10)

# print("-- Go 5m North, 10m East, -5m Down within local coordinate system")
# await drone.offboard.set_position_ned(PositionNedYaw(5.0, 10.0, -5.0, 90.0))
# await asyncio.sleep(10)

# print("-- Go 0m North, 10m East, 0m Down within local coordinate system, turn to face South")
# await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -25.0, 180.0))
# await asyncio.sleep(10)

# # Land the drone
# print("-- Land")
# await drone.action.land()
# await asyncio.sleep(60)

# # Stop offboard mode
# print("-- Stopping offboard")
# try:
#     await drone.offboard.stop()
# except OffboardError as error:
#     print(f"Stopping offboard mode failed with error code: {error._result.result}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())