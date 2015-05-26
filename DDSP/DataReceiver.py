import os
import socket

class DataReceiver:
    """docstring for DataReceiver"""
    def __init__(self):
        selectPort()
        receive()

    def selectPort(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        while True:
            self.port = random.randint(8192, 65535)
            try:
                # Detect whether the port has been occupied.
                s.connect(('127.0.0.1', self.port))
                s.shutdown(2)
                break
            except:
                # Do nothing here to repick another port
                pass

    def receive(path):
        rc = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        s.bind((host, self.port))
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
    print ("DataReceiver class should work if you see this")