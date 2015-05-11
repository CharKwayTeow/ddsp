# The Header class contains the data structure of the Header class, and methods includes encapsulation, and decapsulation.

import struct
import random
from MessageType import MessageType

class Header:
    """docstring for Header"""
    def __init__(self, type = MessageType.undefined):
        self.type = type
        self.length = 0
        self.port = 0

    # """Only use for ACK message"""
    # def generatePortNum(self):
    #     self.port = random.randint(8192, 65535)

    def encapsulation(self):
        return struct.pack("!BHH", self.type, self.length, self.port)

    def decapsulation(self, data):
        header = struct.unpack("!BHH", data)
        self.type = header[0]
        self.length = header[1]
        self.port = header[2]

"""Write the test code here"""
if __name__ == '__main__':
    header = Header(MessageType.query)
    # header.generatePortNum()
    print str(header.port)
    header.length = 1
    header.decapsulation(header.encapsulation())
    print header.type
    print header.length
    print header.port
    print "Header class should work if you see this"