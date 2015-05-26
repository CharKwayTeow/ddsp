# The Query class contains the data structure of the Query.

import sys
import struct
from MessageType import MessageType
from Header import Header
from Record import Record
from Message import Message

class Query(Message):
    """docstring for Query"""
    def __init__(self):
        super(Query, self).__init__(Header(MessageType.query))


"""Write the test code here"""
if __name__ == '__main__':
    print ("Query class should work if you see this")