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
from DemoUtil import query


if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1], sys.argv[2])
    stdscr = curses.initscr()
    stdscr.addstr(0, 10, "A Subscripter Using the APIs of DDSP")
    stdscr.addstr(1, 0, "Press 'q' to quit.")
    stdscr.addstr(3, 0, " ")
    _thread.start_new_thread(query, (stdscr, ddsp, False))

    while True:
        key = stdscr.getch() 
        if key == ord('q'):
            stdscr.clear()
            curses.endwin()
            break

    os._exit(1)