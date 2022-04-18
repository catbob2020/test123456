#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 13:19
# @Author  : 章
# @File    : talk_serve.py
# @Software: PyCharm
import socket
sock = socket.socket(type=socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8085))
# sock.bind(('192.168.1.102', 8080))

# 实现通信循环
while True:
    data, addr = sock.recvfrom(1024)
    print("Receive a message from {}:{}".format(addr, data.decode('utf-8')))
    # if data == b'q':
    # # if data == 'q'.encode('utf-8'):
    #     break
    while True:
        messages = input("Please input the messages to be sent:").strip().encode('utf-8')
        if not messages:
            print("Can't be empty...")
            continue
        sock.sendto(messages, addr)
        break

sock.close()