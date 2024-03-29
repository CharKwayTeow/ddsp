# The Message class contains the data structure of the Message, and methods includes encapsulate, and decapsulate.

import sys
import struct
import netifaces
from socket import *
from Header import Header
from Record import Record

class Message:
    """docstring for Message"""
    def __init__(self, header = Header()):
        self.header = header
        self.records = []

    def addRecord(self, fid):
        self.records.append(fid)
        self.header.length += 1

    def removeRecord(self, fid):
        self.records.remove(fid)
        self.header.length -= 1

    def initializeRecord(self):
        self.records = []

    def encapsulate(self):
        data = self.header.encapsulate()
        for fid in self.records:
            data += struct.pack("!32s", fid)
        return data

    def decapsulate(self, data):
        self.header.decapsulate(data[0:6])
        self.initializeRecord()
        # decapsulate each fid
        recordsData = data[6:]
        for i in range(0, self.header.length):
            self.records.append(struct.unpack("!32s", recordsData[64*i:64*(i+1)])[0])

    def send(self, dst_ip = None, port = 8192, interface = 'eth0'):
        ifconfig = netifaces.ifaddresses(interface)

        # If the ip address is not specified, broadcast the message.
        if dst_ip == None:
            self.port = port
            dst_ip = (ifconfig[netifaces.AF_INET][0]['broadcast'], self.port)
        else:
            self.port = dst_ip[1]

        # Get the ip address of the interface
        src_ip = ifconfig[netifaces.AF_INET][0]['addr']

        data = self.encapsulate()

        s = socket(AF_INET, SOCK_DGRAM)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        s.bind(('', self.port))
        s.settimeout(3)
        s.sendto(data, dst_ip)


"""Write the test code here"""
if __name__ == '__main__':
    message = Message()
    print (message.header.length)
    message.addRecord(b'123456789012345678901234567890123456789012345678901234567890abcd')
    print (message.header.length)
    message.addRecord(b'123456789012345678901234567890123456789012345678901234567890efgh')
    print (message.header.length)
    print (message.records)
    # message.removeRecord(b'123456789012345678901234567890123456789012345678901234567890efgh')
    # print (message.header.length)
    # print (message.records)

    message.decapsulate(message.encapsulate())
    print (message.header.version)
    print (message.header.length)
    print (message.records)
    message.send(('222.222.222.222', 8192), 8192)
    message.send(None, 8192)
    print ("Message class should work if you see this")