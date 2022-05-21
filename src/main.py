from pymavlink import mavutil
import commands

# Start a connection listening to a UDP port
drone = mavutil.mavlink_connection('udpin:localhost:14550')


def main():
    # Wait for a heartbeat
    drone.wait_heartbeat()
    print(
        "Heartbeat from system (system %u component %u)" 
        % (drone.target_system, drone.target_component)
    )

    while(True):
        # Get the current drone state
        msg = drone.recv_match(type='SYS_STATUS', blocking=True)
        # Print the current msg
        print("Drone state: %s" % msg)

        if not msg:
            return
        if msg.get_type() == "BAD_DATA":
            if mavutil.all_printable(msg.data):
                sys.stdout.write(msg.data)
                sys.stdout.flush()
        else:
            

        # Send the command to arm the drone
        if drone_state == False:
            commands.arm_drone()
            
        # Send the command to disarm the drone
        if drone_state == True:
            commands.disarm_drone()