#Implementing FSM
import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)

import time
from os.path import exists

if (exists('/dev/tty.usbserial-0001')):
    port = '/dev/tty.usbserial-0001'
    baud = 57600
else:
    port = 'udp://'
    baud = 14550

BUFFER = 0
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
INTERRUPT = #SPACE KEYINPUT TODO

async def run():

    origin = [0,0,0] #for land command
    curLoc = [0,0,0]

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

    # Make drone hover above origin AKA Home
    print("-- Taking off")
    await drone.action.takeoff()
    await asyncio.sleep(10)

    # Commander the drone to move to a new position
    print("-- Setting initial setpoint")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, 0.0, 0.0))

    # Start the remote control loop
    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

while(! INTERRUPT):
  def buffer():
    return #TODO
    #waypoint function with current location running infinitely in loop
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

