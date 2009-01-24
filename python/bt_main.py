# file: bt.py
# auth: Philippe Chretien <philippe.chretien@gmail.com>
# desc: This small program scan for bluetooth devices and add it to a 
# centralized database
#

import sys
import time
import MySQLdb
import bluetooth

if len(sys.argv) < 3:
	print "bt_main [username] [location name] [wait time in seconds]"
	quit()
	
# argv[0] is the module name
username = sys.argv[1]
location = sys.argv[2]
period = int(sys.argv[3])

# Connect to the database ... the connection is maintained opened until the 
# program exit
print "connecting to the database ..."
conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "basbrun2", db = "bluetooth")

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
		print "  %s - %s" % (addr, name)

		try:
			# First time insertion to the bt_device table. If the address 
			# already exist the database raise an exception 
			cursor = conn.cursor ()
			cursor.execute ("insert into bt_device(address, createdby, created) values (%s,%s,NOW())", (addr, username) )
			cursor.close ()
		except:
			None
		
		# If a name is defined with this device, it is added to the
		# bt_device_name table
		if len(name) > 0:
			try:
				# Try a first insertion. If the address already exist, a database
				# exception is throwed
				cursor = conn.cursor ()
				cursor.execute ("insert into bt_device_name(address, name, createdby, created, updated) values (%s,%s,%s,NOW(),NOW())", (addr, name, username) )
				cursor.close ()
			except:
				try:
					# The address already exist, We then check if the
					# name is the same
					cursor = conn.cursor ()
					cursor.execute ("select count(*) from bt_device_name where address=%s and name=%s", (addr, name))
					exist = int(cursor.fetchone ()[0])
					cursor.close ()

					# The name is different. We update the name of the
					# device to match the new one
					if exist == 0:
						print "    bluetooth device name changed to %s" % (name)
						cursor = conn.cursor ()
						cursor.execute ("update bt_device_name set name=%s, createdby=%s, updated=NOW() where address=%s", (name, username, addr) )
						cursor.close ()
				except:
					print "    bluetooth device name %s update failed" % (name)

		# Keep a timestamp of every time the address is recorded in a specific
		# location
		cursor = conn.cursor ()
		cursor.execute ("insert into bt_ping(address, location, created, createdby) values (%s,%s,NOW(),%s)", (addr, location, username) )
		cursor.close ()
		
	conn.commit()
	time.sleep(period)
	
conn.close ()

