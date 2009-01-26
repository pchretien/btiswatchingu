## BTisWatchingU ##
#
# This program scans for bluetooth devices and add their address and name to a 
# centralized database. This database have some simple facilities to determine
# where and when the device have been spotted.
# Copyright (C) 2008,2009  Philippe Chretien
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# You will find the latest version of this code at the following address:
# http://github.com/pchretien
#
# You can contact me at the following email address:
# philippe.chretien@gmail.com

import sys
import time
import threading
import bluetooth

from bt_db import *
from bt_device import *
from bt_ping import *

# Initialize application parameters
if len(sys.argv) < 3:
	print "bt_main [username] [location name] [period in seconds]"
	quit()
	
# argv[0] is the module name
username = sys.argv[1]
location = sys.argv[2]
period = int(sys.argv[3])

def timerEvent():
    # Prepare the timer for the next run ...
    global t, lock, database
    t = threading.Timer(period, timerEvent)
    t.start()
    if lock == True:
        return
    try:
        lock = True
        print "timer", time.localtime()        
        
        print "performing inquiry ..."
        nearby_devices = ()
        try:
            # Search for bluetooth devices ...        
            nearby_devices = bluetooth.discover_devices(lookup_names = True)
        except:
            print "bluetooth network not found"
    
        # For each device found, add the address and the name to the database 
        for addr, name in nearby_devices:
            print "  processing %s - %s" % (addr, name)
            
            newPing = ping(device(name, addr), username, location)        
            database.saveDevice(newPing)
            database.savePing(newPing)
        
    except:
        None
    finally:
        lock = False


# To avoid parallel execution of the thread
lock = False

# Connect to the database ... the connection is maintained opened until the 
# program exit
database = db("mysql")

# Start the timer thread ...
t = threading.Timer(1, timerEvent)
t.start()


