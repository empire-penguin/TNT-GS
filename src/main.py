from pymavlink import mavutil
import commands
import sys
import time
from os.path import exists

if (exists('/dev/tty.usbserial-0001')):
    port = '/dev/tty.usbserial-0001'
    baud = 57600
else:
    port = 'udpin:localhost:14550'
    baud = 115200

# connect to a drone over mavlink
drone = mavutil.mavlink_connection(port, baud=baud)

def main():
    # Wait for a heartbeat
    drone.wait_heartbeat()
    print(
        "Heartbeat from system (system %u component %u)" 
        % (drone.target_system, drone.target_component)
    )
    start_time = time.time()

    # arm the drone
    # takeoff 10

    # Set computer to control the drone
    # commands.set_param(drone,b'ARMING_CHECK',0)
    # commands.get_param(drone, b'ARMING_CHECK')

    commands.set_home(drone)
    msg = drone.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

    commands.set_guided_mode(drone)
    msg = drone.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

    # arm drone
    commands.arm(drone)
    msg = drone.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

    # takeoff
    commands.takeoff(drone)
    msg = drone.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)
    
    while(True):
        msg = drone.recv_match(type="HEARTBEAT", blocking=True)
        print(msg)
    
main()