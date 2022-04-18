#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 18:24
# @Author  : 章
# @File    : server.py
# @Software: PyCharm
import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.102',8001))
sock.listen(5)
while True:
    conn,addr = sock.accept()  #等等客户端来连接

    print('有人来连接了')
    print(conn)
    conn.sendall('有人来找聊天了'.encode('utf-8'))
    while True:
        msg = input('》》').encode('utf-8')
        length = struct.pack('i',len(msg))
        conn.send(length)
        conn.send(msg)
        # data = conn.recv(1024)
        # if not data:
        #     break
        # data_string =data.decode('utf-8')
        # print('对方消息为:',data_string)
        # huihua=input('')
        # conn.sendall(huihua.encode('utf-8'))
    print('断开连接了')
    conn.close()


    # client_data = conn.recv(1024) # 等等客户端发来数据
    # print(client_data.decode('utf-8'))
    # conn.sendall('hello world'.encode('utf-8'))
#     conn.close()
#
# sock.close()

