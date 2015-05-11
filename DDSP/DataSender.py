import os
import socket

class DataSender:
    """docstring for DataSender"""
    def __init__(self, ip_addr, port):
        self.port = port
        self.ip_addr = ip_addr

    def send(path):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip_addr, self.port))
        f = open(path, 'rb')
        while True:
            data = f.read(4096)
            if data:
                s.send(data)
                f.seek(4096, 1)
            else:
                f.close()
                break
        s.close()


"""Write the test code here"""
if __name__ == '__main__':
    print "DataSender class should work if you see this"