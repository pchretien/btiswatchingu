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
    
