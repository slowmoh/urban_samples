# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:36:03 2016
Python documentary
- Simple example of client and server

@author: Ben
"""

# Echo server program
import socket

HOST = ''
PORT = 50007
# create a new socket using the given address family
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))         # bind the socket to address
    s.listen(1)                 # enable a server to accept connections
    conn, addr = s.accept()     # accept a connection. socket must be bound to an address and listening for connection: return the pair (conn,address)
    # conn is a new socket object usable to send and receive data on the connection
    # address is the address bound to the socket on the other end of the connection
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)  # receive data from the socket (power of 2, eg 4096)
            if not data: break
            conn.sendall(data)  # send data to the socket

