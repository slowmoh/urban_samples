# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:59:25 2016
https://www.youtube.com/watch?v=wzrGwor2veQ&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=55
Socket intro
@author: Ben
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket information: ' +str(s))

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print('Server IP: ' +server_ip)

request ="GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)

#print(result)

while (len(result) > 0):
    print(result)
    result = s.recv(4096)
    
#fo = open("xxx.txt", "wb")
#fo.write(s)
#print("name of the file: ", fo.name)

#fo.close()