import os
import sys
import time
sys.path.append('../DDSP/')
from DDSP import DDSP

if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1], sys.argv[2])
    time.sleep(3)
    ddsp.requestContent(b'123456789012345678901234567890123456789012345678901234567890abcd')
    for record_dict in ddsp.getResourceTable():
            print (record_dict['fid'] + "\t" + record_dict['ip_addr'] + "\t" + record_dict['ttl'] + "\t" + record_dict['status'])
    time.sleep(10)
    print ("Reached the end of Subscriber.py")
    os._exit(1)