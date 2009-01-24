from bt_ping import *
from bt_device import *
from bt_db_mysql import *

class db:
    dbInstance = None
    
    def __init__(self, dbName):
        if(dbName == "mysql"):
            self.dbInstance = db_mysql()
        if(dbName == "mssql"):
            self.dbInstance = None
        if(dbName == "oracle"):
            self.dbInstance = None
            
    def saveDevice(self, ping):
        self.dbInstance.saveDevice(ping.getDevice().getName(), ping.getDevice().getAddress(), ping.getUsername());
        
    def savePing(self, ping):
        self.dbInstance.savePing(ping.getDevice().getAddress(), ping.getLocation(), ping.getUsername())
        
    def dispose(self):
        self.dbInstance.dispose()