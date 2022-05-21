from pymavlink import mavutil
import keyboard

# Start a connection listening to a UDP port
drone_connection = mavutil.mavlink_connection('/dev/tty.usbserial-0001' ,baud=57600)

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
drone_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (drone_connection.target_system, drone_connection.target_component))


drone_connection.mav.command_long_send(
    drone_connection.target_system, 
    drone_connection.target_component, 
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
    0, 1, 0, 0, 0, 0, 0, 0
)

msg = drone_connection.recv_match(type="ATTITUDE",blocking=True)
print(msg)

drone_connection.mav.command_long_send(
    drone_connection.target_system, 
    drone_connection.target_component, 
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 
    0, 1, 0, 0, 0, 0, 0, 5
)

msg = drone_connection.recv_match(type="ATTITUDE",blocking=True)
print(msg)