# The Header class contains the data structure of the Header class, and methods includes encapsulate, and decapsulate.

import struct
import random
from MessageType import MessageType

class Header:
    """docstring for Header"""
    def __init__(self, type = MessageType.undefined):
        self.version = 1
        self.type = type
        self.length = 0
        self.port = 0

    def encapsulate(self):
        return struct.pack("!BBHH", self.version, self.type, self.length, self.port)

    def decapsulate(self, data):
        header = struct.unpack("!BBHH", data)
        self.version = header[0]
        self.type = header[1]
        self.length = header[2]
        self.port = header[3]

"""Write the test code here"""
if __name__ == '__main__':
    header = Header(MessageType.query)
    print (header.port)
    header.length = 1
    header.decapsulate(header.encapsulate())
    print (header.version)
    print (header.type)
    print (header.length)
    print (header.port)
    print ("Header class should work if you see this")