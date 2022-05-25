from pymavlink import mavutil
import time

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

def takeoff(connection):
    print("TAKING OFF") 
    connection.mav.command_long_send(
        connection.target_system, 
        connection.target_component, 
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 
        0, 1, 0, 0, 0, 0, 0, 5
    )

def goto(connection, x, y, z, start_time):
    print("GOING TO")
    connection.mav.send(mavutil.mavlink.MAVLINK_set_position_target_local_ned_message(
        (time.time() - start_time), # time_boot_ms
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b110111111000,
        x, # x position
        y, # y position
        z, # z position
        0, # x velocity
        0, # y velocity
        0, # z velocity
        0, # x acceleration
        0, # y acceleration
        0, # z acceleration
        0, # yaw
        0, # yaw rate
    ))

def loiter(connection):
    print("LOITERING")
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_NAV_LOITER_TIME,
        0, 5, 0, 0, 0, 0, 0, 0
    )
