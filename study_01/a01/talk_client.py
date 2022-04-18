#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 13:19
# @Author  : 章
# @File    : talk_client.py
# @Software: PyCharm
import socket
sock = socket.socket(type=socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8081))
# 实现通信循环
while True:
    messages = input("Please input your messages to be sent:").strip().encode('utf-8')
    if not messages:
        print("Can't be empty...")
        continue
    # elif messages == b'q':
    # elif messages == 'q'.encode('utf-8'):
    elif messages == 'q'.encode(encoding='utf-8'):
        break
    else:
        sock.sendto(messages, ('127.0.0.1',8085))
        data, addr = sock.recvfrom(1024)
        print("Receive a message from {}:{}".format(addr, data.decode('utf-8')))
sock.close()