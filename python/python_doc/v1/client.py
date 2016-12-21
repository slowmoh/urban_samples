# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:36:02 2016

@author: Ben
"""

import socket

name = input('please write your name: ')
age = input('please type your age: ')
matnr = input('please type your matrikel number: ')

HOST = 'localhost'  # remote host
PORT = 50007            # the same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('received', repr(data))