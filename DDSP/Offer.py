# The Offer class contains the data structure of the Offer.

import sys
import struct
from MessageType import MessageType
from Header import Header
from Record import Record
from Message import Message

class Offer(Message):
    """docstring for Offer"""
    def __init__(self):
        super(Offer, self).__init__(Header(MessageType.offer))


"""Write the test code here"""
if __name__ == '__main__':
    print ("Offer class should work if you see this")