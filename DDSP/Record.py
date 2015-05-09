# The Record class contains the data structure of a record encapsulation, and decapsulation.

import sys
import struct

class Record:
    """docstring for Record"""
    def __init__(self, fid = 0, ip_addr = '127.0.0.1'):
        self.fid = fid
        self.ip_addr = ip_addr
        self.ttl = 60

    def encapsulation(self):
        pass

    def decapsulation(self, data):
        pass


"""Write the test code here"""
if __name__ == '__main__':
    print "Record class should work if you see this"