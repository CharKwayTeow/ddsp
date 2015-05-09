# The Message class contains the data structure of the Message, and methods includes encapsulation, and decapsulation.

import sys
import struct
# import socket
# import fcntl
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

    def removeRecord(self, fid):
        records.remove(fid)

    def initializeRecord(self):
        records = []

    def encapsulation(self):
        pass

    def decapsulation(self, data):
        pass

    def send(self, dst_ip = None):
        interface = netifaces.ifaddresses('eth0')

        # If the ip address is not specified, broadcast the message.
        if dst_ip == None:
            dst_ip = interface[netifaces.AF_INET][0]['broadcast']

        src_ip = interface[netifaces.AF_INET][0]['addr']
        port = 8096

        data = self.encapsulation()

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(3)
        s.sendto(data,(dst_ip, port))


"""Write the test code here"""
if __name__ == '__main__':
    print "Message class should work if you see this"