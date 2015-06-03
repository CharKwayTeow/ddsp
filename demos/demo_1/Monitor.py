import curses
import time
import os
import sys
import random
import hashlib
import _thread
sys.path.append('../../DDSP/')
from DDSP import DDSP

def updateScreen(stdscr):
    fid_pos = 0
    ip_pos = 68
    ttl_pos = 88
    status_pos = 96
    while True:
        stdscr.clear()
        stdscr.addstr(0, 10, "A Monitor Using the APIs of DDSP")
        stdscr.addstr(1, 0, "Press 'q' to quit.")
        stdscr.addstr(3, fid_pos, "FID")
        stdscr.addstr(3, ip_pos, "IP Address")
        stdscr.addstr(3, ttl_pos, "TTL")
        stdscr.addstr(3, status_pos, "Status" + "\n")
        i = 4
        for record_dict in ddsp.getResourceTable():
            stdscr.addstr(i, fid_pos, record_dict['fid'])
            stdscr.addstr(i, ip_pos, record_dict['ip_addr'])
            stdscr.addstr(i, ttl_pos, record_dict['ttl'])
            stdscr.addstr(i, status_pos, record_dict['status'] + "\n")
            i += 1
        stdscr.refresh()


if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1])
    stdscr = curses.initscr()
    _thread.start_new_thread(updateScreen, (stdscr, ))

    while True:
        key = stdscr.getch() 
        if key == ord('q'):
            curses.endwin()
            break

    os._exit(1)