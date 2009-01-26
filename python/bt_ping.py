
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

from bt_device import *

class ping:
    __device = None
    __username = ""
    __location = ""    
    
    def __init__(self, device, username, location):
        self.__device = device
        self.__username = username
        self.__location = location
        
    def getDevice(self):
        return self.__device
    
    def getUsername(self):
        return self.__username
    
    def getLocation(self):
        return self.__location
    
