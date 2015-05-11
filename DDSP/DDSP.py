# This is the interface of the protocol.

import sys
import struct
from Header import Header
from Record import Record

class DDSP:
    """docstring for DDSP"""
    def __init__(self, data_directory = 'data', port = 8192):
        # initialization
        self.data_directory = data_directory
        self.port = port
        
        run()

    def run(self):
        pass

    def addContent(self, fid):
        pass

    def removeContent(self, fid):
        pass

    def requestContent(self, fid):
        pass