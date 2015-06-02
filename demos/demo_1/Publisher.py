import curses
import time
import os
import sys
import random
import hashlib
sys.path.append('../../DDSP/')
from DDSP import DDSP

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

if __name__ == '__main__':
    ddsp = DDSP(sys.argv[1], sys.argv[2])
    stdscr = curses.initscr()
    stdscr.addstr(0, 10, "A Publisher Using the APIs of DDSP")
    stdscr.addstr(1, 0, "Press 'a' to generate a file and broadcast a advertisement.")
    stdscr.addstr(2, 0, "Press 'q' to quit.")
    stdscr.addstr(4, 0, " ")

    i = 4
    while True:
        key = stdscr.getch() 
        if key == ord('a'):
            fid = generateFile(sys.argv[2])
            ddsp.addContent(fid);
            stdscr.addstr(i, 0, "Published a File: " + fid.decode('utf-8'))
            stdscr.refresh()
            i += 1
            stdscr.addstr(i, 0, " ")
        elif key == ord('q'):
            curses.endwin()
            break

    os._exit(1)