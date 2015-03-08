#!/usr/bin/python

# Echo server program
from openmath import *
import socket

HOST = 'localhost'        # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while(True):
	s.listen(1)
	conn, addr = s.accept()
	print 'Connected by', addr
	while 1:
		data = conn.recv(1024)
		if not data: break
		conn.sendall(str(ParseOMstring(data)))
	conn.close()
