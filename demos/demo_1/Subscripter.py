import curses
import time
import os
import sys
import random
import hashlib
import _thread
sys.path.append('../../DDSP/')
from DDSP import DDSP

def query(stdscr):
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
                    i += 1
                    stdscr.addstr(i, 0, " ")
                    stdscr.refresh()
                    time.sleep(3)
                    break


if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1], sys.argv[2])
    stdscr = curses.initscr()
    stdscr.addstr(0, 10, "A Subscripter Using the APIs of DDSP")
    stdscr.addstr(1, 0, "Press 'q' to quit.")
    stdscr.addstr(3, 0, " ")
    _thread.start_new_thread(query, (stdscr, ))

    while True:
        key = stdscr.getch() 
        if key == ord('q'):
            curses.endwin()
            break

    os._exit(1)