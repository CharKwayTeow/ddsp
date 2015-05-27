import os
import socket
import random

class DataReceiver:
    """docstring for DataReceiver"""
    def __init__(self):
        self.selectPort()

    def selectPort(self):
        while True:
            self.port = random.randint(8192, 65535)
            try:
                print (self.port)
                # Detect whether the port has been occupied.
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(('', self.port))
                s.close()
                print ('success.')
                return
            except:
                # Do nothing here to repick another port
                print("Unexpected error:", sys.exc_info()[0])
                pass

    def receive(self, path):
        rc = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', self.port))
        s.settimeout(10)
        try:
            s.listen(1)

            conn, addr = s.accept()
            f = open(path, 'wb')
            while True:
                data = conn.recv(4096)
                if data:
                    f.write(data)
                else:
                    f.close()
                    break
        except:
            rc = -1
        finally:
            s.close()
            return rc

"""Write the test code here"""
if __name__ == '__main__':
    receiver = DataReceiver()
    receiver.port = 11111
    print (receiver.receive('../../received/missfont.log'))
    print ("DataReceiver class should work if you see this")