#!/usr/bin/python

# Echo client program
import socket
import sys
import getopt

"""
Send OpenMath doc to server and get response.
Reference: https://docs.python.org/2/library/socket.html
"""
def send(inputfile, outputfile, host, port):
    try:
        # get contents of file
        with open(inputfile, "r") as f:
            data = f.read()
            
        # connect to server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        
        # send data
        s.sendall(data)
        data = s.recv(1024)
        s.close()
        
        # write response to file
        with open(outputfile, "w") as f:
            f.write(data)
        print "Outputted server response to ", outputfile
    except IOError:
        print "An error occurred while accessing files. Please try again."

"""
Gets command-line arguments and passes them
to send.
"""
def main(argv):
    host  = 'localhost'
    port  = 50007
    usage = 'client.py -i <inputfile> -o <outputfile> [-p <port>] [-h <host>]'
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:a:p", ["ifile=", "ofile=", "host=", "port="])
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print usage
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-p", "--port"):
            if arg != '':
                port = int(arg)
        elif opt in ("-a", "--host"):
            host = arg
            
    # check if user hasn't specified inputs
    if not 'inputfile' in locals()\
    or not 'outputfile' in locals():
        print usage
        sys.exit(2)
        
    send(inputfile, outputfile, host, port)

if __name__ == "__main__":
    main(sys.argv[1:])
