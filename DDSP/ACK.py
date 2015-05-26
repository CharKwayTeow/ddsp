# The ACK class contains the data structure of the ACK.

import sys
import struct
from MessageType import MessageType
from Header import Header
from Record import Record
from Message import Message

class ACK(Message):
    """docstring for ACK"""
    def __init__(self, port):
        super(ACK, self).__init__(Header(MessageType.ack))
        self.header.port = port


"""Write the test code here"""
if __name__ == '__main__':
    print ("ACK class should work if you see this")