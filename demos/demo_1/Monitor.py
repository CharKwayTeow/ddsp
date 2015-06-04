import curses
import time
import os
import sys
import random
import hashlib
import _thread
sys.path.append('../../DDSP/')
from DDSP import DDSP
sys.path.append('../')
from DemoUtil import updateScreen

if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1])
    stdscr = curses.initscr()
    _thread.start_new_thread(updateScreen, (stdscr, ddsp, True))

    while True:
        key = stdscr.getch() 
        if key == ord('q'):
            stdscr.clear()
            curses.endwin()
            break

    os._exit(1)