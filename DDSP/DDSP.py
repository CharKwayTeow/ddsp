# This is the interface of the protocol.

import sys
import struct
import socket
import _thread
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
    def __init__(self, interface = 'eth0', data_directory = 'data', port = 8192):
        # initialization
        self.interface = interface
        self.data_directory = data_directory
        self.port = port
        self.resourceTable = ResourceTable()

        # start a new thread to run the daemon function
        self.daemon = _thread.start_new_thread(self.run, ())

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', self.port))
        while True:
            data, ip_addr = s.recvfrom(1024)
            incomeMessage = Message()
            incomeMessage.decapsulate(data)
            # print (incomeMessage.header.type)
            # print (incomeMessage.header.length)

            # start a new thread to handle message
            _thread.start_new_thread(self.handleMessage, (incomeMessage, ip_addr))

    def handleMessage(self, incomeMessage, ip_addr):
        def handleDiscoveryAndQueryMessage(incomeMessage, ip_addr):
            # check the resource table, if find the record, send an offer
            for record in self.resourceTable.records:
                if record.status == 0 and record.fid == incomeMessage.records[0]:
                    # send an offer
                    offer = Offer()
                    offer.addRecord(record.fid)
                    offer.send(ip_addr, self.port, self.interface)
                    break

        def handleAdvertisementMessage(incomeMessage, ip_addr):
            # add a record to resource table
            record = Record(incomeMessage.records[0], ip_addr[0], RecordStatus.on_remote)
            self.resourceTable.records.append(record)

        def handleWithdrawMessage(incomeMessage, ip_addr):
            # delete a record in resource table
            for record in self.resourceTable.records:
                if record.fid == incomeMessage.records[0] and record.ip_addr == ip_addr:
                    # delete the record
                    self.resourceTable.remove(record)
                    break

        def handleOfferMessage(incomeMessage, ip_addr):
            # check the resource table, if not found, send a ack, else, send a nack
            for record in self.resourceTable.records:
                if record.fid == incomeMessage.records[0] and record.status != RecordStatus.on_remote:
                    # send a nack
                    nack = NACK()
                    nack.addRecord(incomeMessage.records[0])
                    nack.send(ip_addr, self.port, self.interface)
                    break
            # update the resource table
            self.resourceTable.updateStatus(incomeMessage.records[0], RecordStatus.on_the_wire)
            rc = -1
            while rc != 0:
                # setup a data receiver
                receiver = DataReceiver()
                # send an ack
                ack = ACK(receiver.port)
                ack.addRecord(incomeMessage.records[0])
                ack.send(ip_addr, self.port, self.interface)
                # start the receiver
                rc = receiver.receive(self.data_directory + "/" + incomeMessage.records[0].decode(encoding='UTF-8'))
            # update resource table
            self.resourceTable.updateStatus(incomeMessage.records[0], RecordStatus.on_the_disk)

        def handleAckMessage(incomeMessage, ip_addr):
            # transfer data
            for record in self.resourceTable.records:
                if record.fid == incomeMessage.records[0]:
                    # establish a connection
                    sender = DataSender(ip_addr, incomeMessage.header.port)
                    sender.send(self.data_directory + "/" + record.fid.decode(encoding='UTF-8'))
                    break
            
        
        if incomeMessage.header.version != 1:
            return    
        
        if incomeMessage.header.type == MessageType.discovery or incomeMessage.header.type == MessageType.query:
            handleDiscoveryAndQueryMessage(incomeMessage, ip_addr)

        elif incomeMessage.header.type == MessageType.advertisement:
            handleAdvertisementMessage(incomeMessage, ip_addr)
            
        elif incomeMessage.header.type == MessageType.withdraw:
            handleWithdrawMessage(incomeMessage, ip_addr)
            
        elif incomeMessage.header.type == MessageType.offer:
            handleOfferMessage(incomeMessage, ip_addr)

        elif incomeMessage.header.type == MessageType.ack:
            handleAckMessage(incomeMessage, ip_addr)
            
        elif incomeMessage.header.type == MessageType.nack:
            pass
            
        else:
            pass


    def addContent(self, fid):
        record = Record(fid, '127.0.0.1', RecordStatus.on_the_disk)
        self.resourceTable.records.append(record)
        advertisement = Advertisement()
        advertisement.addRecord(fid)
        advertisement.send(None, self.port, self.interface)

    def removeContent(self, fid):
        for record in self.resourceTable.records:
            if record.fid == fid:
                self.resourceTable.remove(record)
                withdraw = Withdraw()
                withdraw.addRecord(fid)
                withdraw.send(None, self.port, self.interface)

    def requestContent(self, fid):
        for record in self.resourceTable.records:
            if record.fid == fid:
                query = Query()
                query.addRecord(fid)
                query.send((record.ip_addr, self.port), self.port, self.interface)
                return
        discovery = Discovery()
        discovery.addRecord(fid)
        discovery.send(None, self.port, self.interface)

    def getResourceTable(self):
        result = []
        for record in self.resourceTable.records:
            record_dict = {}
            record_dict['fid'] = record.fid
            record_dict['ip_addr'] = record.ip_addr
            record_dict['ttl'] = record.ttl
            record_dict['status'] = record.status
            result.append(record_dict)
        return result

"""Write the test code here"""
if __name__ == '__main__':
    ddsp = DDSP()
    print ("DDSP class should work if you see this")