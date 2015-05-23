# This is the interface of the protocol.

import sys
import struct
import socket
import thread
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

        # start a new thread to run the daemon function
        thread.start_new_thread(run)

    def run(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(('', port))
            data, ip_addr = udps.recvfrom(1024)
            incomeMessage = Message()
            incomeMessage.decapsulate()

            # start a new thread to handle message
            thread.start_new_thread(handleMessage, incomeMessage)
            

    def handleMessage(incomeMessage):
        if incomeMessage.header.type == MessageType.discovery or incomeMessage.header.type == MessageType.query:
            # check the resource table, if find the record, send an offer
            for record in self.resourceTable.records:
                if record.status == 0 and record.fid == incomeMessage.records[0]:
                    # send an offer
                    offer = Offer()
                    offer.addRecord(record.fid)
                    offer.send(ip_addr, self.port)
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
                    nack.send(ip_addr, self.port)
                    return
            # update the resource table
            resourceTable.updateStatus(fid, RecordStatus.on_the_wire)
            # setup a data receiver
            receiver = DataReceiver()
            # send an ack
            rc = -1
            while rc != 0:
                ack = ACK(receiver.port)
                ack.addRecord(incomeMessage.records[0])
                ack.send(ip_addr, self.port)
                # start the receiver
                rc = receiver.receive(self.data_directory + "/" + fid)
            # update resource table
            resourceTable.updateStatus(fid, RecordStatus.on_the_disk)
            
        elif incomeMessage.header.type == MessageType.ack:
            # transfer data
            for record in self.resourceTable.records:
                if record.fid == incomeMessage.records[0]:
                    # establish a connection
                    sender = DataSender(ip_addr, imcomeMessage.header.port)
                    sender.send(self.data_directory + "/" + fid)
                    break
            
        elif incomeMessage.header.type == MessageType.nack:
            pass
            
        else:
            pass


    def addContent(self, fid):
        record = Record(fid, '127.0.0.1', RecordStatus.on_the_disk)
        self.resourceTable.records.append(record)
        advertisement = Advertisement()
        advertisement.addRecord(fid)
        advertisement.send(None, self.port)

    def removeContent(self, fid):
        for record in self.resourceTable.records:
            if record.fid == fid:
                self.resourceTable.remove(record)
                withdraw = Withdraw()
                withdraw.addRecord(fid)
                withdraw.send(None, self.port)

    def requestContent(self, fid):
        for record in self.resourceTable.records:
            if record.fid == fid:
                query = Query()
                query.addRecord(fid)
                query.send(record.ip_addr, self.port)
                break
        discovery = Discovery()
        discovery.addRecord(fid)
        discovery.send(None, self.port)

"""Write the test code here"""
if __name__ == '__main__':
    print "DDSP class should work if you see this"