#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 20:30
# @Author  : 章
# @File    : server_struct.py
# @Software: PyCharm
import socket
import threading
import time
import struct

def recv_message(conn,socket_list):#创建一个收消息的函数
    try:
        length2_niname = conn.recv(4)
        length2 = struct.unpack('i',length2_niname)[0]
        niname = conn.recv(length2).decode('utf-8').strip()
    except:
        conn.close()#关闭当前建立的客户端的套接字
        socket_list.remove(conn)
        for i in socket_list:
            ms2 = '\n公告:轻轻的我走了，正如我轻轻的来，名字不留下'.encode('utf-8')
            length_ms2 = struct.pack('i',len(ms2))
            i.send(length_ms2)
            i.send(ms2)
        return None
    for i in socket_list:
        ms3 = f'\n公告:欢迎{niname}进入了聊天室........\n'.encode('utf-8')
        length_ms3 = struct.pack('i',len(ms3))
        i.send(length_ms3)
        i.send(ms3)
    while True:
        try:
            leni_data = conn.recv(4)
            leni = struct.unpack('i',leni_data)[0]

            recv_data = conn.recv(leni).decode('utf-8')
            print(recv_data)
            for i in socket_list:
                mstime = time.strftime('%X').encode('utf-8')
                lentime = struct.pack('i',len(mstime))
                i.send(lentime)
                i.send(mstime)
                # i.send(time.strftime('%X').encode('utf-8'))
                ms4 = f'{niname}:{recv_data}'.encode('utf-8')
                print(f'{niname}:{recv_data}')
                len4_ms4 = struct.pack('i',len(ms4))
                i.send(len4_ms4)
                i.send(ms4)
        except:
            conn.close()#关闭当前客户端的套接字
            socket_list.remove(conn)
            for i in socket_list:
                ms5 = f'公告:{niname}离开了聊天室......'.encode('utf-8')
                len5= struct.pack('i',len(ms5))
                i.send(len5)
                i.send(ms5)
            break
def send_message(conn):  #发送消息到公屏上
    while True:
        # msg = input('发送公告：').strip()
        ms ='公告:'+ input()
        msg = ms.strip().encode('utf-8')
        length6 = struct.pack('i',len(msg))
        # length = format(len(msg),"04d")
        if not ms.strip():   #若消息全为空格和回车则为空消息
            print("消息不能为空.")
            continue
        # conn.sendall(msg.encode('utf-8'))
        conn.send(length6)
        conn.send(msg)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("0.0.0.0",8888))

s.listen(5)
print('服务端处于监听状态，等待客户端接入..........')
socket_list = []
while True:

    conn,addr = s.accept()
    print('客户端已接入')
    socket_list.append(conn)
    msg_1 = '请输入昵称:'.encode('utf-8')
    len_msg1 = struct.pack('i',len(msg_1))
    conn.send(len_msg1)
    conn.send(msg_1)
    t1 = threading.Thread(target=recv_message,args=(conn,socket_list))
    t2 = threading.Thread(target=send_message,args=(conn,))
    t1.start()
    t2.start()

