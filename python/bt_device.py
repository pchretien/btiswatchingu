class device:
    __name = ""
    __address = ""
    
    def __init__(self, deviceName, deviceAddress):
        self.__name = deviceName
        self.__address = deviceAddress

    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address