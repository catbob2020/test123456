#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 17:39
# @Author  : 章
# @File    : client_struct.py
# @Software: PyCharm
# -*- coding: UTF-8 -*-
import threading
import socket
import time
import struct



class Client:
    SERVER_IP = 'localhost'
    PORT = 8888

    def __init__(self, serve_ip=SERVER_IP, port=PORT):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
        self.client.connect((serve_ip, port))  # 建立一个链接，连接到服务器端口

    def __del__(self):
        self.client.close()

    def close(self):
        self.client.close()

    def sender(self):
        while True:
            time.sleep(0.1)
            # msg = input("发送的信息：").strip()   #防止空格和回车发送空消息
            ms = input("发送的信息：")
            if not ms.strip():
                print("消息不能为空.")
                continue
            msg = ms.encode('utf-8')
            length_ms = struct.pack('i',len(msg))

            self.client.send(length_ms)
            self.client.send(msg)

    def receiver(self):
        while True:
            # time.sleep(1)
            length_msg = self.client.recv(4)
            length = struct.unpack('i',length_msg)[0]
            msg = self.client.recv(length).decode('utf-8')
            print(msg)


    def loop(self):
        receiver = threading.Thread(target=self.receiver)
        receiver.start()
        sender = threading.Thread(target=self.sender)
        sender.start()
if __name__ == '__main__':
    c = Client()
    c.loop()
