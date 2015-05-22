# This is the interface of the protocol.

import sys
import struct
import socket
# from Header import Header
from MessageType import MessageType
from RecordStatus import RecordStatus
from Record import Record
from Message import Message
from Discovery import Discovery
from Advertisement import Advertisement
from Withdraw import Withdraw
from Query import Query
from Offer import Offer
from ACK import ACK
from NACK import NACK
from ResourceTable import ResourceTable
from DataReceiver import DataReceiver
from DataSender import DataSender

class DDSP:
    """docstring for DDSP"""
    def __init__(self, data_directory = 'data', port = 8192):
        # initialization
        self.data_directory = data_directory
        self.port = port
        self.resourceTable = ResourceTable()

        run()   # a new thread is expected to call this method

    def run(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(('', port))
            data, ip_addr = udps.recvfrom(1024)
            incomeMessage = Message()
            incomeMessage.decapsulate()

            if incomeMessage.header.type == MessageType.discovery or incomeMessage.header.type == MessageType.query:
                # check the resource table, if find the record, send an offer
                for record in self.resourceTable.records:
                    if record.status == 0 and record.fid == incomeMessage.records[0]:
                        # send an offer
                        offer = Offer()
                        offer.addRecord(record.fid)
                        offer.send(ip_addr)
                        break

            elif incomeMessage.header.type == MessageType.advertisement:
                # add a record to resource table
                record = Record(incomeMessage.records[0], ip_addr, RecordStatus.on_remote)
                self.resourceTable.records.append(record)
                
            elif incomeMessage.header.type == MessageType.withdraw:
                # delete a record in resource table
                for record in self.resourceTable.records:
                    if record.fid == incomeMessage.records[0]:
                        # delete the record
                        resourceTable.remove(record)
                        break
                
            elif incomeMessage.header.type == MessageType.offer:
                # check the resource table, if not found, send a ack, else, send a nack
                for record in self.resourceTable.records:
                    if record.fid == incomeMessage.records[0]:
                        # send a nack
                        nack = NACK()
                        nack.addRecord(incomeMessage.records[0])
                        nack.send(ip_addr)
                        return
                # add to resource table
                resourceTable.add(Record(incomeMessage.records[0], ip_addr, RecordStatus.on_the_wire))
                # setup a data receiver
                receiver = DataReceiver()
                # send an ack
                rc = -1
                while rc != 0:
                    ack = ACK(receiver.port)
                    ack.addRecord(incomeMessage.records[0])
                    ack.send(ip_addr)
                    # start the receiver
                    rc = receiver.receive(data_directory + "/" + fid)    # a new thread is   expected to call this method

                
            elif incomeMessage.header.type == MessageType.ack:
                # transfer data
                for record in self.resourceTable.records:
                    if record.fid == incomeMessage.records[0]:
                        # establish a connection
                        sender = DataSender(ip_addr, imcomeMessage.header.port)
                        sender.send(data_directory + "/" + fid) # a new thread is expected to call this method
                        break
                
            elif incomeMessage.header.type == MessageType.nack:
                pass
                
            else:
                pass

    def addContent(self, fid):
        pass

    def removeContent(self, fid):
        pass

    def requestContent(self, fid):
        pass

"""Write the test code here"""
if __name__ == '__main__':
    print "DDSP class should work if you see this"