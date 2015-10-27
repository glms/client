#/usr/bin/python

# this is Grapich Linux Monitoring System client side
# kontam da ga preimenujem u nock nock ili samo nok, nock


# libs
import sys
import os
import commands
import json
import time
import httplib

def connect():
	print "bla"
	# ovde treba da se registruje ako nije i konektuje i time povuce informacija o intervalu i pickama materina

def register():
	# This function should register self on web system
	# generate node id
	nuid = commands.getstatusoutput("ifconfig | grep $(route | grep default | awk '{print $8}' | head -n 1) | awk '{print $NF}' | sed 's/://g'")
	nuid = nuid[1]
	# get CPU model
	cpu = commands.getstatusoutput("cat /proc/cpuinfo | grep 'model name' | head -n 1 | sed 's/model name//' | sed 's/://'")
	cpu = cpu[1]
	# get CPU cores
	cpucores = commands.getstatusoutput("grep processor /proc/cpuinfo | wc -l")
	cpucores = cpucores[1]
	# get sys arch
	arch = commands.getstatusoutput("uname -m")
	arch = arch[1]
	# get sys kernel
	kernel = commands.getstatusoutput("uname -r")
	kernel = kernel[1]
	# get hostame
	hostname = commands.getstatusoutput("cat /etc/hostname")
	hostname = hostname[1]
	# get total RAM
	ramtotal  = commands.getstatusoutput("cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'")
	ramtotal = str(int(ramtotal[1])/1000000)+"MB"
	# get total disk size
	st = os.statvfs("/")
	disktotal = str((st.f_blocks * st.f_frsize)/1000000000)+"GB"
	# generate json to send
	data = '{"nuid":"' + nuid + '", "cpu":"' + cpu + '", "cpucores":"' + cpucores + '", "arch":"' + arch + '", "kernel":"' + kernel + '", "hostname":"' + hostname + '", "ramtotal":"' + ramtotal + '", "disktotal":"' + disktotal + '" }'
	# send json
	httpServ = httplib.HTTPConnection("127.0.0.1", 5000)
  	httpServ.connect()
	httpServ.request('POST', '/push', data)
  	response = httpServ.getresponse()
  	print response.read() 
  	httpServ.close()

register()



def push():
	# get nuid 
	nuid = commands.getstatusoutput("ifconfig | grep $(route | grep default | awk '{print $8}' | head -n 1) | awk '{print $NF}' | sed 's/://g'")
	while 1:
		# get free RAM in MB
		ramfree = commands.getstatusoutput("cat /proc/meminfo | grep MemFree | awk '{ print $2 }'")
		ramfree = freemem[1]
		# get load
		load = commands.getstatusoutput("cat /proc/loadavg")
		load = load[1]
		# get CPU utilization
		cputil = commands.getstatusoutput("mpstat | awk '$12 ~ /[0-9.]+/ { print 100 - $12"%" }'")
		cputil = cputil[1]
		# get hdd free space in GB
		st = os.statvfs("/")
		diskfree = str((st.f_bavail * st.f_frsize)/1000000000)+"GB"
		# get recieved data
		ethrx = commands.getstatusoutput("cat /sys/class/net/$(route | grep default | awk '{print $8}' | head -n 1)/statistics/rx_bytes")
		ethrx = str(int(ethrx[1])/1000/1000)+"MB"
		# get sent data
		ethtx = commands.getstatusoutput("cat /sys/class/net/$(route | grep default | awk '{print $8}' | head -n 1)/statistics/tx_bytes")
		ethtx = str(int(ethtx[1])/1000/1000)+"MB"

		# ovde radi konekciju

		time.sleep(5)

