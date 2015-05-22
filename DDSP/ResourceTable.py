# The ResourceTable class contains the data structure of the ResourceTable class, and methods includes add, remove, clear.

import sys
import struct
from Header import Header
from Record import Record
import time, threading

class ResourceTable:
    """docstring for ResourceTable"""
    def __init__(self):
        # initialization
        self.records = []
        run()

    def run():
        # excute once per second
        threading.Timer(1, run).start()

        for record in self.records:
            if record.ip_addr != '127.0.0.1':
                record.ttl -= 1
                if record.ttl == 0:
                    remove(record)

    def add(self, record):
        pass

    def remove(self, record):
        pass

    def clear(self):
        self.records = []

"""Write the test code here"""
if __name__ == '__main__':
    print "ResourceTable class should work if you see this"