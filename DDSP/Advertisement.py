# The Advertisement class contains the data structure of the Advertisement.

import sys
import struct
from MessageType import MessageType
from Header import Header
from Record import Record
from Message import Message

class Advertisement(Message):
    """docstring for Advertisement"""
    def __init__(self):
        super(Advertisement, self).__init__(Header(MessageType.advertisement))


"""Write the test code here"""
if __name__ == '__main__':
    print ("Advertisement class should work if you see this")