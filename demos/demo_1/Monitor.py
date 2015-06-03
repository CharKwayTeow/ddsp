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
    while True:
        stdscr.clear()
        stdscr.addstr(0, 10, "A Monitor Using the APIs of DDSP")
        stdscr.addstr(1, 0, "Press 'q' to quit.")
        stdscr.addstr(3, 0, "FID \t IP Address \t TTL \t Status \n")
        i = 4
        for record_dict in ddsp.getResourceTable():
            stdscr.addstr(i, 0, record_dict['fid'] + "\t" + record_dict['ip_addr'] + "\t" + record_dict['ttl'] + "\t" + record_dict['status'] + "\n")
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