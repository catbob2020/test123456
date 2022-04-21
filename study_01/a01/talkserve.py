#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 11:49
# @Author  : 章
# @File    : talkserve.py
# @Software: PyCharm

import socket
import threading
import time

import pymysql

def recv_message(conn,socket_list):#创建一个收消息的函数
    try:
        nikename = conn.recv(1024).decode('utf-8').strip()
    except:
        conn.close()#关闭当前建立的客户端的套接字
        socket_list.remove(conn)
        for i in socket_list:
            i.send('\n公告:轻轻的我走了，正如我轻轻的来，名字不留下'.encode('utf-8'))
        return None
    for i in socket_list:
        i.send(f'\n公告:欢迎{nikename}进入了聊天室........\n'.encode('utf-8'))
    while True:
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='nba2')
        cursor = db.cursor()
        try:
            recv_data = conn.recv(1024).decode('utf-8')
            print(recv_data)
            for i in socket_list:
                i.send(time.strftime('%X').encode('utf-8'))
                i.send(f'{nikename}:{recv_data}'.encode('utf-8'))
                t_1=time.strftime('%X')
                print(t_1,nikename,recv_data)
                sql1="insert into tb_te1(class4,class,cla_3) values ('%s','%s','%s')"%(nikename,t_1,recv_data)
                cursor.execute(sql1)
                db.commit()
        except:
            conn.close()#关闭当前客户端的套接字
            socket_list.remove(conn)
            for i in socket_list:
                i.send(f'公告:{nikename}离开了聊天室......'.encode('utf-8'))
            break
# db.close()
def send_message(conn):  #发送消息到公屏上
    while True:
        # msg = input('发送公告：').strip()
        msg = input('发送公告：')
        if not msg.strip():   #若消息全为空格和回车则为空消息
            print("消息不能为空.")
            continue
        # conn.sendall(msg.encode('utf-8'))
        conn.sendall(f'公告:{msg}'.encode('utf-8'))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("0.0.0.0",8888))

s.listen(5)
print('服务端处于监听状态，等待客户端接入..........')
socket_list = []
while True:

    conn,addr = s.accept()
    print('客户端已接入')
    socket_list.append(conn)
    conn.send('请输入昵称:'.encode('utf-8'))
    # recv_message(conn, socket_list)
    t1 = threading.Thread(target=recv_message,args=(conn,socket_list))
    t2 = threading.Thread(target=send_message,args=(conn,))
    t1.start()
    t2.start()
    # db.close()






# con = threading.Condition()
# host =input('input the serve ip')
# port = 8888
# data=''
# s=socket.socket()
# print('socket creat')
# s.bind((host,port))
# s.listen(5)
# print('监听')
#
# def NotifyAll(sss):
#     global data
#     if con.acquire():  #获取锁
#         data = sss
#         con.notifyAll()  #表示当前线程放弃对资源的占用，通知其它线程
#         con.release()  #释放锁
#
# def threadout(conn,nick):
#     global data
#     while True:
#         if con.acquire():
#             con.wait()
#             if data:
#                 try:
#                     conn.send(data)
#                     con.release()
#                 except:
#                     con.release()
#                     return
#
# def threadin(conn,nick):
#     while True:
#         try:
#             temp = conn.recv(1024)
#             if not temp:
#                 conn.close()
#             NotifyAll(temp)
#             print(data)
#         except:
#             NotifyAll(nick+'error')
#             print(data)
#             return
#
#
#
#
# while True:
#     conn,addr = s.accept()
#     # print('connected with {} : {}'.format(addr[0],addr[1]))
#     print('connected with'+addr[0]+':'+str(addr[1]))
#     nick = conn.recv(1024)
#     NotifyAll('welcome'+nick.enocde('utf-8')+'加入聊天')
#     print(data)
#     conn.send(data)
#     threading.Thread(target=threadout,args=(conn,nick.enocde('utf-8'))).start()
#     threading.Thread(target=threadin,agrs = (conn,nick.enocde('utf-8'))).start()







# server = socket.socket()
# server.bind(('0.0.0.0',9999))
# server.listen(5)
#
# while True:
#     print('等待连接...')
#     con,addr = server.accept()
#     while True:
#         try:
#             data = con.recv(1024)  # 接收数据
#             print('IP为:' + addr[0] + '向您发来消息：',data.decode())
#             con.send('done'.encode('utf-8'))
#         except ConnectionResetError as e:
#             print('客户端：%s 已经断开！'%addr[0])
#             break
#     con.close()
# server.close()