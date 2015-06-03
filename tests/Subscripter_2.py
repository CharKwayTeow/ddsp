import os
import sys
import time
sys.path.append('../DDSP/')
from DDSP import DDSP

if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1], sys.argv[2])
    while True:
        for record_dict in ddsp.getResourceTable():
                ddsp.requestContent(record_dict['fid'].encode('utf-8'))
                print (record_dict['fid'] + "\t" + record_dict['ip_addr'] + "\t" + record_dict['ttl'] + "\t" + record_dict['status'])
    os._exit(1)