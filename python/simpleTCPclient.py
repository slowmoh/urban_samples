# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:03:13 2016

@author: Ben
"""

import socket
import sys

#Further task - url input by user for download
HOST = 'coding.debuntu.org'
GET = '/rss.xml'
PORT = 80

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(1)
    
try:
    sock.connect((HOST, PORT))
except socket.error as msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(2)
    
sock.send(**b** "GET %s HTTP/1.0\r\nHost: %s\r\n\r\n" % (GET, HOST))

data = sock.recv(1024)
string = ""
while len(data):
    string = string + data
    data = sock.recv(1024)
sock.close()

print(string)

sys.exit(0)
    