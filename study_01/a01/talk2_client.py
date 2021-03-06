#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 13:38
# @Author  : 章
# @File    : talk2_client.py
# @Software: PyCharm
import socket
sock = socket.socket(type=socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8082))
while True:
    messages = input("Please input your messages to be sent:").strip().encode('utf-8')
    if not messages:
        print("Can't be empty...")
        continue
    elif messages == b'q':
        break
    else:
        sock.sendto(messages, ('127.0.0.1',8080))
        data, addr = sock.recvfrom(1024)
        print("Receive a message from {}:{}".format(addr, data.decode('utf-8')))
sock.close()