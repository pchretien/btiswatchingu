# file: bt.py
# auth: Philippe Chretien <philippe.chretien@gmail.com>
# desc: This small program scan for bluetooth devices and add it to a 
# centralized database
#

import sys
import time
import bluetooth

from bt_db import *
from bt_device import *
from bt_ping import *

# Initialize application parameters
if len(sys.argv) < 3:
	print "bt_main [username] [location name] [wait time in seconds]"
	quit()
	
# argv[0] is the module name
username = sys.argv[1]
location = sys.argv[2]
period = int(sys.argv[3])

# Connect to the database ... the connection is maintained opened until the 
# program exit
database = db("mysql")

while 1==1:
	nearby_devices = ()
	print "performing inquiry..."

	try:
		# Search for bluetooth devices ...	    
		nearby_devices = bluetooth.discover_devices(lookup_names = True)
		print "found %d devices" % len(nearby_devices)
	except:
		print "bluetooth network not found"

	# For each device found, add the address and the name to the database 
	for addr, name in nearby_devices:
		print "  processing %s - %s" % (addr, name)
		
		newPing = ping(device(name, addr), username, location)		
		database.saveDevice(newPing)
		database.savePing(newPing)
		
	time.sleep(period)
	
database.dispose()

