# file: bt.py
# auth: Philippe Chretien <philippe.chretien@gmail.com>
# desc: This small program scan for bluetooth devices and add it to a 
# centralized database
#

import time
import MySQLdb
import bluetooth

print "connecting to the database ..."
conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "basbrun2", db = "bluetooth")

for i in range(1, 1000000):
	nearby_devices = ()
	print "performing inquiry..."

	try:
	    nearby_devices = bluetooth.discover_devices(lookup_names = True)
	    print "found %d devices" % len(nearby_devices)
	except:
	    print "bluetooth network not found"

	for addr, name in nearby_devices:
	    print "  %s - %s" % (addr, name)

	    try:
		cursor = conn.cursor ()
		cursor.execute ("insert into bt_device(address, createdby, created) values (%s,%s,NOW())", (addr, "pchretien@gcesoft.com") )
		cursor.close ()
	    except:
		print "    bluetooth device address %s already published" % (addr)

	    if len(name) > 0:
		    try:
			cursor = conn.cursor ()
			cursor.execute ("insert into bt_device_name(address, name, createdby, created, updated) values (%s,%s,%s,NOW(),NOW())", (addr, name, "pchretien@gcesoft.com") )
			cursor.close ()
		    except:
			try:
			    cursor = conn.cursor ()
			    cursor.execute ("select count(*) from bt_device_name where address=%s and name=%s", (addr, name))
			    exist = int(cursor.fetchone ()[0])
			    cursor.close ()

			    if exist == 0:
			    	print "    bluetooth device name changed to %s" % (name)
			        cursor = conn.cursor ()
			        cursor.execute ("update bt_device_name set name=%s, createdby=%s, updated=NOW() where address=%s", (name, "pchretien@gcesoft.com", addr) )
			        cursor.close ()
			    
			except:
			    print "    bluetooth device name %s update failed" % (name)

	conn.commit()
	time.sleep(10)
conn.close ()

