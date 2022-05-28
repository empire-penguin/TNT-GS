from pymavlink import mavutil
import time

def arm(connection):
    print("---ARMED")
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
        0, 1, 0, 0, 0, 0, 0, 0
    )

def disarm(connection):
    print("---DISARMED")
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
        0, 0, 0, 0, 0, 0, 0, 0
    )

def takeoff(connection):
    print("---TAKING OFF") 
    connection.mav.command_long_send(
        connection.target_system, 
        connection.target_component, 
        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 
        0, 0, 0, 0, 0, 0, 0, 10
    )

def goto(connection, x, y, z, start_time):
    print("---GOING UP")
    connection.mav.send(
        mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
            int(time.time() - start_time), # time_boot_ms
            connection.target_system,
            connection.target_component,
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,
            int(0b110111111000),
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
        )
    )

def set_offboard_mode(connection):
    print("---SETTING OFFBOARD MODE")
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE,
        0, # confirmation
        209, # param1
        6, # param2
        0, # param3
        0, # param4
        0, # param5
        0, # param6
        0  # param7
    )
def set_home(connection):
    print("---SETTING HOME")
    connection.mav.command_int_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_FRAME_GLOBAL,
        mavutil.mavlink.MAV_CMD_DO_SET_HOME,
        0, # current (not used)
        0, # autocontinue (not used)
        0, # param1 (use current location)
        0, # param2 (not used)
        0, # param3 (not used)
        0, # param4 (not used)
        328813570, # param5 (x latitude)
        -1172332020, # param6 (y longitude)
        0  # param7 (z alt)
    )

def rtn_to_launch(connection):
    print("---GOING HOME")
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE,
        0, # confirmation
        1, # param1
        6, # param2
        0, # param3
        0, # param4
        0, # param5
        0, # param6
        0  # param7
    )

def land(connection):
    print("---LANDING")
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE,
        0, # confirmation
        1, # param1
        6, # param2
        0, # param3
        0, # param4
        0, # param5
        0, # param6
        0  # param7
    )

<<<<<<< HEAD
=======
def loiter(connection, time):
    print("LOITERING")
    connection.mav.command_long_send(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_NAV_LOITER_TIME,
        0, time, 0, 0, 0, 0, 0, 0
    )

>>>>>>> c387720df624b5eaaa0c00283498d5a0c1652410
def get_all_params(connection):
    connection.mav.send(
        mavutil.mavlink.MAVLink_param_request_list_message(
            connection.target_system,
            connection.target_component,
        )
    )

def get_param(connection, id):
    connection.mav.send(
        mavutil.mavlink.MAVLink_param_request_read_message(
            connection.target_system,
            connection.target_component,
            id,
            -1
        )
    )
    print(connection.recv_match(type="PARAM_VALUE", blocking=True))

def set_param(connection, id, value):
    connection.mav.send(
        mavutil.mavlink.MAVLink_param_set_message(
            connection.target_system,
            connection.target_component,
            id,
            value,
            mavutil.mavlink.MAV_PARAM_TYPE_INT16
        )
    )