import os
import sys
import time
sys.path.append('../DDSP/')
from DDSP import DDSP

if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1], sys.argv[2])
    while True:
        for record_dict in ddsp.getResourceTable():
            if record_dict['ip_addr'] != '127.0.0.1':
                interested = True
                for duplicated in ddsp.getResourceTable():
                    if duplicated['fid'] == record_dict['fid'] and duplicated['ip_addr'] == '127.0.0.1':
                        interested = False
                        break
                if interested:
                    ddsp.requestContent(record_dict['fid'].encode('utf-8'))
                    print (record_dict['fid'] + "\t" + record_dict['ip_addr'] + "\t" + record_dict['ttl'] + "\t" + record_dict['status'])
                    time.sleep(3)
        
    os._exit(1)