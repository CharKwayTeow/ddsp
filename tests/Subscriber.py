import os
import sys
import time
sys.path.append('../DDSP/')
from DDSP import DDSP

if __name__ == '__main__':
    ddsp = DDSP('../../sent', 12344)
    time.sleep(3)
    ddsp.requestContent('123456789012345678901234567890123456789012345678901234567890abcd')
    time.sleep(10)
    print ("Reached the end of Subscriber.py")