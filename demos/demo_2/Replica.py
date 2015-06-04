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
from DemoUtil import query
from DemoUtil import generateFile


if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1], sys.argv[2])
    stdscr = curses.initscr()
    _thread.start_new_thread(updateScreen, (stdscr, ddsp, 5))
    _thread.start_new_thread(query, (stdscr, ddsp, True))

    while True:
        key = stdscr.getch() 
        if key == ord('a'):
            fid = generateFile(sys.argv[2])
            ddsp.addContent(fid)
            stdscr.addstr(3, 0, "Published a File: " + fid.decode('utf-8'))
            stdscr.refresh()
            stdscr.addstr(4, 0, " ")
        elif key == ord('r'):
            for record_dict in ddsp.getResourceTable():
                if record_dict['ip_addr'] == '127.0.0.1':
                    ddsp.removeContent(record_dict['fid'].encode('utf-8'))
                    stdscr.addstr(3, 0, "withdrew a File: " + record_dict['fid'])
                    stdscr.refresh()
                    break
            stdscr.addstr(4, 0, " ")
        elif key == ord('q'):
            curses.endwin()
            break

    os._exit(1)