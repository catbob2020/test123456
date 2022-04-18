#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 18:24
# @Author  : 章
# @File    : client.py
# @Software: PyCharm
import socket
import struct

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.bind(('192.168.1.102',8002))
client.connect(('192.168.1.102',8001))
message = client.recv(1024)
print(message.decode('utf-8'))
while True:
    length_msg=client.recv(4)
    length = struct.unpack('i',length_msg)[0]
    msg = client.recv(length).decode('utf-8')
    print(msg)
    # content = input('请输入，Q可以退出')
    # if content.upper() == 'Q':
    # # if content == b'Q':
    #     break
    # client.sendall(content.encode('utf-8'))
    # reply = client.recv(1024)
    # print(reply.decode('utf-8'))
client.close()
# client.sendall('hello'.encode('utf-8'))
# reply = client.recv(1024)
# print(reply)
# client.close()

