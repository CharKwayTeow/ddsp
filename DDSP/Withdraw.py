# The Withdraw class contains the data structure of the Withdraw.

import sys
import struct
from MessageType import MessageType
from Header import Header
from Record import Record
from Message import Message

class Withdraw(Message):
    """docstring for Withdraw"""
    def __init__(self):
        super(Withdraw, self).__init__(Header(MessageType.withdraw))


"""Write the test code here"""
if __name__ == '__main__':
    print ("Withdraw class should work if you see this")