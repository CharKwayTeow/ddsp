import curses
import time
import os
import sys
import random
import hashlib
import _thread
sys.path.append('../../DDSP/')
from DDSP import DDSP

def updateScreen(stdscr, ddsp, table_top):
    fid_pos = 0
    ip_pos = 68
    ttl_pos = 88
    status_pos = 96
    while True:
        stdscr.clear()
        stdscr.addstr(0, 10, "A Monitor Using the APIs of DDSP")
        stdscr.addstr(1, 0, "Press 'q' to quit.")
        stdscr.addstr(table_top, fid_pos, "FID")
        stdscr.addstr(table_top, ip_pos, "IP Address")
        stdscr.addstr(table_top, ttl_pos, "TTL")
        stdscr.addstr(table_top, status_pos, "Status" + "\n")
        i = table_top + 1
        for record_dict in ddsp.getResourceTable():
            stdscr.addstr(i, fid_pos, record_dict['fid'])
            stdscr.addstr(i, ip_pos, record_dict['ip_addr'])
            stdscr.addstr(i, ttl_pos, record_dict['ttl'])
            stdscr.addstr(i, status_pos, record_dict['status'] + "\n")
            i += 1
        stdscr.refresh()

def generateFid():
    return (hashlib.md5((''.join(chr(random.randint(32,126)) for _ in range(64))).encode('utf-8')).hexdigest() + hashlib.md5((''.join(chr(random.randint(32,126)) for _ in range(64))).encode('utf-8')).hexdigest()).encode('utf-8')

def generateFile(data_directory):
    fid = generateFid();
    f = open(data_directory + '/' + fid.decode('utf-8'), 'wb')
    data_size = random.randint(50000, 100000);
    data = (''.join(chr(random.randint(32,126)) for _ in range(data_size))).encode('utf-8')
    f.write(data)
    f.close();
    return fid

def query(stdscr, ddsp, fixed_pos = False):
    fid_pos = 0
    ip_pos = 68
    ttl_pos = 88
    status_pos = 96
    i = 3
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
                    stdscr.addstr(i, 0, "Requested for a File: " + record_dict['fid'])
                    if not fixed_pos:
                        i += 1
                        stdscr.addstr(i, 0, " ")
                    else:
                        stdscr.addstr(i+1, 0, " ")
                    stdscr.refresh()
                    time.sleep(3)
                    break