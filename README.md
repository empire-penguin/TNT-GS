# TNT-GS 

[![Releases](https://img.shields.io/endpoint?url=https%3A%2F%2Fempire-penguin.github.io%2Fempire-penguin%2Fdata%2FTNT-GS%2Fshields%2Fversion.json)](https://github.com/empire-penguin/TNT-GS)


Ground Station for Triton Neurotech
-----------------------------------
-----------------------------------


Opening a Simulator
------------------

If no ardupilot hardware is available try running the Java simulator which is included in the PX4-Ardupilot source code found [here](https://github.com/PX4/PX4-Autopilot) after downloading navigate tp the root directory and run the command `make px4_sitl jmavsim`. Wait for the source to build and eventually you will see a drone sitting in the middle of a field.


Connecting to a Drone
-------------------

You must specify the port to send and receive commands to and from. 
On an **UNIX environment** the following ports are used in the `pymavlink` command
`mavutil.mavlink_connection(<port>)`
* Drone Simulator - `udpin:localhost:14550`
* USB to Pixhawk - `/dev/cu.usbmodem01`
* Over Telemetry - `/dev/tty.usbserial-0001`

