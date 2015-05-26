# The Discovery class contains the data structure of the Discovery.

import sys
import struct
from MessageType import MessageType
from Header import Header
from Record import Record
from Message import Message

class Discovery(Message):
    """docstring for Discovery"""
    def __init__(self):
        super(Discovery, self).__init__(Header(MessageType.discovery))


"""Write the test code here"""
if __name__ == '__main__':
    print ("Discovery class should work if you see this")