PREREQUISITES:
	1. Update...
		$ sudo apt update
	2. Install python2...
		$ sudo apt install python-minimal
	3. Install pip for python 2 and 3...
		$ sudo apt install python-pip python3-pip
	4. Install dronekit python2 api
		$ sudo pip2 install dronekit
	5. Install dronekit-sitl
		$ sudo pip install dronekit-sitl
	6. Install mavproxy
		$ sudo pip install mavproxy.py
	7. Update
		$ sudo apt update
	8. Clone final project Repo
		$ git clone https://github.com/jburns11/ardupilot
	9. Enter Directory
		$ cd arducopter
	10. Get submodules
		$ git submodule update --init --recursive
	11. Install ardupilot prereqs
		$ Tools/environment_install/install-prereqs-ubuntu.sh -y
	12. Configure build system
		$ ./waf configure
	13. Clean build system
		$ ./waf clean
	14. Make target
		$ ./waf build --board=sitl
	15. Now you can start the multi vehicle simulation
		$ python vehicle_connect.py
	

FILES:
	vehicle_connect.py - This file will start multiple vehicle simulations and provide connections to them with a dronkit connection object. These vehicle connections can be used to control the goal of the UAV.

	clean_proc.bash -  Use this script to kill all simulations that did not properly terminate. This might happen if vehicle_connect.py does not close properly


