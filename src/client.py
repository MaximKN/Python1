#!/usr/bin/python

# Echo client program
import socket
import sys
import getopt


def main(argv):
    inputfile  = ''
    outputfile = ''
    host = 'localhost'
    port = 50007
    try:
        opts, args = getopt.getopt(argv,"hi:o:a:p",["ifile=","ofile=", "host=", "port="])
    except getopt.GetoptError:
        print 'client.py -i <inputfile> -o <outputfile> [-p <port>] [-h <host>]'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'client.py -i <inputfile> -o <outputfile> [-p <port>] [-h <host>]'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-p", "--port"):
            if (arg != ''):
                port = int(arg)
       	elif opt in ("-a", "--host"):
       		host = arg
    send(inputfile, outputfile, host, port)

"""
Send OpenMath doc to server and
get response
"""
def send(inputfile, outputfile):
    # get contents of file
    with open(inputfile, "r") as f:
        data = f.read();

    HOST = 'localhost'  # The remote host
    PORT = 50007  # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print "Connected to server"
    print "Sending data..."
    s.sendall(data)
    print "Data sent"
    data = s.recv(1024)
    s.close()
    with open(outputfile, "w") as f:
        f.write(data)
    print "Outputted server response to ", outputfile

if __name__ == "__main__":
    main(sys.argv[1:])
