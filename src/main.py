from pymavlink import mavutil
import commands

# Start a connection listening to a UDP port
drone_connection = mavutil.mavlink_connection('udpin:localhost:14550')

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
drone_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (drone_connection.target_system, drone_connection.target_component))

while ( True ):
    msg = drone_connection.recv_match(type="LOCAL_POSITION_NED", blocking=True)
    print(msg)



