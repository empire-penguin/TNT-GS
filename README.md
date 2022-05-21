# TNT-GS 

[![Releases](https://img.shields.io/endpoint?url=https%3A%2F%2Fempire-penguin.github.io%2Fempire-penguin%2Fdata%2FTNT-GS%2Fshields%2Fversion.json)](https://github.com/empire-penguin/TNT-GS)


Ground Station for Triton Neurotech Drone Project
-----------------------------------
-----------------------------------

Important Links
---------------
* [MAVlink Messages Protocol](https://mavlink.io/en/messages/common.html#COMMAND_LONG)
* [MAVlink Command Protocol](https://mavlink.io/en/services/command.html#MAV_CMD)
* [Ardupilot Guided Mode](https://ardupilot.org/copter/docs/ac2_guidedmode.html)
* [Ardupilot Movement Commands in Guided Mode](https://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html)


TODO
----
* Create main DFA for state handling
* Act on the current state to command drone


Opening a Simulator
------------------

If no ardupilot hardware is available try running the Java simulator which is included in the PX4-Ardupilot source code found [here](https://github.com/PX4/PX4-Autopilot) after downloading navigate to the root directory and run the command `make px4_sitl jmavsim`. Wait for the source to build and eventually you will see a drone sitting in the middle of a field.


Connecting to a Drone
-------------------

You must specify the port to send and receive MAVlink commands to and from. 
On an **UNIX environment** the following ports are used in the `mavutil` module of `pymavlink` called `mavlink_connection(<port>)` which returns a connection to the target drone

* Drone Simulator - `udpin:localhost:14550`
* USB to Pixhawk - `/dev/cu.usbmodem01`
* Over Telemetry - `/dev/tty.usbserial-0001` & `baud=57600`

