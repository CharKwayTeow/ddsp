# The Record class contains the data structure of a record encapsulate, and decapsulate.

import sys
import struct

class Record:
    """docstring for Record"""
    def __init__(self, fid = 0, ip_addr = '127.0.0.1', status = 0):
        self.fid = fid
        self.ip_addr = ip_addr
        self.ttl = 60
        self.status = status    # status = 0: on the wire, = 1: on the disk

    def encapsulate(self):
        pass

    def decapsulate(self, data):
        pass


"""Write the test code here"""
if __name__ == '__main__':
    print "Record class should work if you see this"