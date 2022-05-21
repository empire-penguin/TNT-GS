def arm_drone():
    print("ARMED")
    drone_connection.mav.command_long_send(
        drone_connection.target_system,
        drone_connection.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
        0, 1, 0, 0, 0, 0, 0, 0
    )