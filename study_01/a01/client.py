#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 18:24
# @Author  : 章
# @File    : client.py
# @Software: PyCharm
import socket
import struct
import pymysql
import time

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='nba2',
                     )
cursor = db.cursor()

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.bind(('192.168.1.102',8002))
client.connect(('192.168.1.102',8001))
message = client.recv(1024)
print(message.decode('utf-8'))
while True:
    length_msg=client.recv(4)
    length = struct.unpack('i',length_msg)[0]
    msg = client.recv(length).decode('utf-8')
    print(time.strftime('%X')+msg)
    time2=time.strftime('%X')
    # msg=time.strftime('%X')+msg
    # sql2 = "insert into tb_te1(class) values('%s')" % time2
    sql="insert into tb_te1(cla_3,class) values('%s','%s')" % (msg,time2)
    # cursor.execute(sql2)
    cursor.execute(sql)
    db.commit()


    # content = input('请输入，Q可以退出')
    # if content.upper() == 'Q':
    # # if content == b'Q':
    #     break
    # client.sendall(content.encode('utf-8'))
    # reply = client.recv(1024)
    # print(reply.decode('utf-8'))
client.close()
db.close()
# client.sendall('hello'.encode('utf-8'))
# reply = client.recv(1024)
# print(reply)
# client.close()

