#!/usr/bin/python

# Echo server program
from openmath import *
import socket
import sys, getopt


'''
Sends result of parsing client's input back to the client.
Reference:https://docs.python.org/2/library/socket.html
'''
def start(host, port):
    
    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    # listen forever
    while True:
        s.listen(1)
        conn, addr = s.accept() # client connected
        while 1:
            data = conn.recv(1024)
            if not data:
                break
            # calculate and send the result to client
            conn.sendall(str(ParseOMstring(data)))
        conn.close()

'''
Extracts command line arguments, then calls send with arguments
'''
def main(argv):
    # default socket info
    host = 'localhost'
    port = 50007
    
    # extract arguments
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
    
