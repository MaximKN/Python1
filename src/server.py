#!/usr/bin/python

# Echo server program
from openmath import *
import socket
import sys, getopt


# Reference:https://docs.python.org/2/library/socket.html
def start(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    while True:
        s.listen(1)
        conn, addr = s.accept()
        while 1:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(str(ParseOMstring(data)))
        conn.close()


def main(argv):
    host = 'localhost'
    port = 50007
    try:
        opts, args = getopt.getopt(argv[1:], "h:a:p", ["host=", "port="])
    except getopt.GetoptError:
        print 'server.py [-p <port>] [-h <host>]'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'server.py [-p <port>] [-h <host>]'
            sys.exit()
        elif opt in ("-p", "--port"):
            if arg != '':
                port = int(arg)
        elif opt in ("-a", "--host"):
            host = arg
    start(host, port)

if __name__ == "__main__":
    main(sys.argv)
