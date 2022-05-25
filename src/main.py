from pymavlink import mavutil
import commands
import sys
import time

# Start a connection listening to a UDP port
drone = mavutil.mavlink_connection('/dev/tty.usbserial-0001', baud=57600)

def main():
    # Wait for a heartbeat
    drone.wait_heartbeat()
    print(
        "Heartbeat from system (system %u component %u)" 
        % (drone.target_system, drone.target_component)
    )
    start_time = time.time()
    # Arm the drone
    commands.arm_drone(drone)
    # Takeoff
    commands.takeoff(drone)
    # Go to a position
    commands.goto(drone, 0, 0, -10, start_time)
    #loiter while hand signal is not equal to loiter signal
    while :
        commands.loiter(drone)

main()