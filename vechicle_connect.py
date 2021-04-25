#!/usr/bin/env python2
import dronekit
import subprocess
import os
import time

START_ID=2
VEHICLE_COUNTER=0

HOMES = ["-35.363261,149.165230,584,353", "-35.364261,149.166230,584,353",  "-35.365261,149.167230,584,353","-35.366261,149.168230,584,353","-35.367261,149.169230,584,353"]

def set_simulation_source_system():
	global VEHICLE_COUNTER, START_ID
	print("mavproxy.py --master=tcp:127.0.0.1:57"+str(63+10*(START_ID+VEHICLE_COUNTER))+" --cmd=\"set source_system " +  str(START_ID+VEHICLE_COUNTER)+"\"")
	mav_proxy = subprocess.Popen(["mavproxy.py", 
		"--master=tcp:127.0.0.1:57"+str(63+10*(START_ID+VEHICLE_COUNTER)), 
		"--cmd=\"set source_system " +  str(START_ID+VEHICLE_COUNTER)+"\""])
	time.sleep(20)
	mav_proxy.kill()
	
def new_vehicle_simulation():
	global VEHICLE_COUNTER, START_ID
	print("===============Sumulation #"+ str(VEHICLE_COUNTER) + " starting...===============")
	simulation = subprocess.Popen(("python ./Tools/autotest/sim_vehicle.py -v ArduCopter -f quad --no-mavproxy --instance=" + str(START_ID+VEHICLE_COUNTER) ).split())
	print("===============Sumulation #"+ str(VEHICLE_COUNTER) + " started===============")
	set_simulation_source_system()
	return simulation

def new_vehicle_connection(wait=True):
	global VEHICLE_COUNTER, START_ID
	connection_str = "tcp:127.0.0.1:"+str(5760+(START_ID+VEHICLE_COUNTER)*10)
	print("===============Connection #" + str(VEHICLE_COUNTER) + " starting on " + connection_str+"===============")
	connection = dronekit.connect(connection_str, wait_ready=wait, source_system=VEHICLE_COUNTER+START_ID)
	print("===============Connection  #" + str(VEHICLE_COUNTER) + " started on " + connection_str+"===============")
	return connection

def new_vehicle(wait=True):
	global VEHICLE_COUNTER
	s = new_vehicle_simulation()
	v = new_vehicle_connection(wait)
	for i in v.parameters:
		print i
	while v.parameters["SYSID_THISMAV"] != VEHICLE_COUNTER+1:
            v.parameters["SYSID_THISMAV"] = VEHICLE_COUNTER+1
	VEHICLE_COUNTER+=1
	return [v, s]

def start_n_vehicles(n, wait=True):
	n_vehicles = []
	print("===============Starting "+str(n)+" vehicles===============")
	for i in range(n):
		n_vehicles.append(new_vehicle())
	print("===============Started "+str(n)+" vehicles===============")
	return n_vehicles

def main():
	vehicles = start_n_vehicles(2)
	while(str(raw_input("ENTER 'q' to quit: ")) != 'q'):
		print ""
	for vehicle in vehicles:
		vehicle[1].kill()
	os.system('killall -9 xterm')

main()

