import curses
import time
import os
import sys
import random
import hashlib
sys.path.append('../../DDSP/')
from DDSP import DDSP

if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1], sys.argv[2])
    stdscr = curses.initscr()

    i = 4
    while True:
        stdscr.clear()
        stdscr.addstr(0, 10, "A Monitor Using the APIs of DDSP")
        stdscr.addstr(1, 0, "Press 'q' to quit.")
        stdscr.addstr(3, 0, "FID \t IP Address \t TTL \t Status")
        for record_dict in ddsp.getResourceTable():
            stdscr.addstr(i, 0, record_dict['fid'] + "\t" + record_dict['ip_addr'] + "\t" + record_dict['ttl'] + "\t" + record_dict['status'])
            i += 1
        stdscr.refresh()
        
        key = stdscr.getch() 
        if key == ord('q'):
            curses.endwin()
            break

    os._exit(1)