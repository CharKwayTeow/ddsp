# The NACK class contains the data structure of the NACK.

import sys
import struct
from MessageType import MessageType
from Header import Header
from Record import Record
from Message import Message

class NACK(Message):
    """docstring for NACK"""
    def __init__(self):
        super(NACK, self).__init__(Header(MessageType.nack))


"""Write the test code here"""
if __name__ == '__main__':
    print "NACK class should work if you see this"