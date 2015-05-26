# The ResourceTable class contains the data structure of the ResourceTable class, and methods includes add, remove, clear.

import sys
import struct
import time, threading
from Record import Record
from RecordStatus import RecordStatus

class ResourceTable:
    """docstring for ResourceTable"""
    def __init__(self):
        # initialization
        self.records = []
        self.run()

    def run(self):
        # excute once per second
        threading.Timer(1, self.run).start()

        for record in self.records:
            if record.ip_addr != '127.0.0.1':
                record.ttl -= 1
                if record.ttl == 0:
                    self.remove(record)

    def add(self, record):
        self.records.append(record)

    def remove(self, record):
        self.records.remove(record)

    def clear(self):
        self.records = []

    def updateStatus(self, fid, status):
        for record in self.records:
            if record.fid == fid:
                record.status = status

"""Write the test code here"""
if __name__ == '__main__':
    resourceTable = ResourceTable()
    resourceTable.add(Record('123456789012345678901234567890123456789012345678901234567890efgh', '111.10.10.11', 0))
    print (resourceTable.records[0].ttl)
    while resourceTable.records[0].ttl != 30:
        pass
    print (resourceTable.records[0].ttl)
    
    resourceTable.add(Record('123456789012345678901234567890123456789012345678901234567890abcd', '127.0.0.1', 0))
    while len(resourceTable.records) != 1:
        pass
    print (len(resourceTable.records))
    print ("ResourceTable class should work if you see this")