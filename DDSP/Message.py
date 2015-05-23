# The Message class contains the data structure of the Message, and methods includes encapsulate, and decapsulate.

import sys
import struct
import netifaces
from Header import Header
from Record import Record

class Message:
    """docstring for Message"""
    def __init__(self, header = Header()):
        self.header = header
        self.records = []

    def addRecord(self, fid):
        records.append(fid)
        self.header.length += 1

    def removeRecord(self, fid):
        records.remove(fid)
        self.header.length -= 1

    def initializeRecord(self):
        records = []

    def encapsulate(self):
        data = self.header.encapsulate
        for fid in self.records:
            data += struct.pack("!I", fid)
        return data

    def decapsulate(self, data):
        self.header.decapsulate(data[0:8])
        initializeRecord()
        # decapsulate each fid
        recordsData = data[9:]
        for i in range(len(recordsData)/4):
            self.records.append(struct.unpack("!I", recordsData[4*i:4*i+3])[0])

    def send(self, dst_ip = None):
        interface = netifaces.ifaddresses('eth0')

        # If the ip address is not specified, broadcast the message.
        if dst_ip == None:
            dst_ip = interface[netifaces.AF_INET][0]['broadcast']

        # Get the ip address of the interface
        src_ip = interface[netifaces.AF_INET][0]['addr']
        port = 8096

        data = self.encapsulate()

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(3)
        s.sendto(data,(dst_ip, port))


"""Write the test code here"""
if __name__ == '__main__':
    print "Message class should work if you see this"