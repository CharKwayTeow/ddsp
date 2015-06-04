import curses
import time
import os
import sys
import random
import hashlib
sys.path.append('../../DDSP/')
from DDSP import DDSP
sys.path.append('../')
from DemoUtil import generateFile

if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1], sys.argv[2])
    stdscr = curses.initscr()
    stdscr.addstr(0, 10, "A Publisher Using the APIs of DDSP")
    stdscr.addstr(1, 0, "Press 'a' to generate a file and broadcast a advertisement.")
    stdscr.addstr(2, 0, "Press 'r' to withdraw a file and broadcast the message.")
    stdscr.addstr(3, 0, "Press 'q' to quit.")
    stdscr.addstr(5, 0, " ")

    i = 5
    while True:
        key = stdscr.getch() 
        if key == ord('a'):
            fid = generateFile(sys.argv[2])
            ddsp.addContent(fid)
            stdscr.addstr(i, 0, "Published a File: " + fid.decode('utf-8'))
            stdscr.refresh()
            i += 1
            stdscr.addstr(i, 0, " ")
        elif key == ord('r'):
            for record_dict in ddsp.getResourceTable():
                if record_dict['ip_addr'] == '127.0.0.1':
                    ddsp.removeContent(record_dict['fid'].encode('utf-8'))
                    stdscr.addstr(i, 0, "withdrew a File: " + record_dict['fid'])
                    stdscr.refresh()
                    i += 1
                    break
            stdscr.addstr(i, 0, " ")
        elif key == ord('q'):
            stdscr.clear()
            curses.endwin()
            break

    os._exit(1)