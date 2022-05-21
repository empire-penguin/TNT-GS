from pymavlink import mavutil

def arm_drone(connection):
    print("ARMED")
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
        0, 1, 0, 0, 0, 0, 0, 0
    )

def disarm_drone(connection):
    print("DISARMED")
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
        0, 0, 0, 0, 0, 0, 0, 0
    )