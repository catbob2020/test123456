#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 11:42
# @Author  : 章
# @File    : talkclient.py
# @Software: PyCharm
import socket
import threading
import socket,threading
import tkinter as tk
#创建套接字
a = 1
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",5678))#此处端口看服务端的端口，127.0.0.1要改成服务端主机的ipv4地址
print('已链接服务端,通讯加密中')
def shou(s,msg_text):
    recv_data = s.recv(1024).decode('utf-8')
    msg_text.insert(tk.END, recv_data)
    while 1:
        recv_data = s.recv(1024).decode('utf-8')
        msg_text.insert(tk.END,recv_data)
def fa():
    global a
    if a == 0:
        msg = input_text.get('0.0',tk.END)
        s.send(msg.encode('utf-8'))
        input_text.delete('0.0',tk.END)
    else:
        msg = input_text.get('0.0', tk.END)
        s.send(msg.encode('utf-8'))
        input_text.delete('0.0', tk.END)
        msg_text.delete('0.0', tk.END)
        a = 0

app = tk.Tk()
app.title('聊天室')
#显示消息框
msg_frame = tk.Frame(app,width=480,height=300)
msg_frame.grid(row=0,column=0,padx=6,pady=6)
msg_frame.grid_propagate(0)#固定Frame的大小
msg_text = tk.Text(msg_frame,bg='white')
msg_text.grid()
# msg_text.insert('0.0','hhh')
#输入
input_frame = tk.Frame(app,width=480,height=100)
input_frame.grid(row=1,column=0)
input_frame.grid_propagate(0)
input_text = tk.Text(input_frame,bg='white')
input_text.grid()
#发送按钮
btn_frame = tk.Frame(app,width=480,height=20)
btn_frame.grid(row=2,column=0,sticky='E')
button = tk.Button(btn_frame,text='发送',command=fa)
button.grid()
#线程
t1 = threading.Thread(target=shou,args=(s,msg_text))
t1.daemon = True
t1.start()
app.mainloop()
#s.close()





# outstring=''
# nick=''
# instring=''
# def client_send(sock):
#     global outstring
#     while True:
#         outstring = input()
#         outstring = nick+":"+outstring
#         sock.send(outstring)
#
# def client_accept(sock):
#     global instring
#     while True:
#         try:
#             instring = sock.recv(1024)
#             if not instring:
#                 break
#             if outstring != instring:  #不显示自己发出的消息
#                 print(instring)
#         except:
#             break
#
#
#
# nick = input('input uour nicknmae').encode('utf-8')
# ip = input('input your ip')
# port = 8888
# sock = socket.socket()
# sock.connect((ip,port))  #连接
#
# sock.send(nick) #发送给服务㟨
# th_send = threading.Thread(target=client_send,args=(sock,))
# th_send.start()
# th_accept = threading.Thread(target=client_accept,args=(sock,))
# th_accept.start()









import socket
# ip_addr = input('请输入对方IP地址：').strip()
# client = socket.socket()
# client.connect((ip_addr,9999))
#
# while True:
#     msg = input('>>:').strip()
#     if len(msg) == 0: continue
#     client.send(msg.encode('utf-8'))
#     data_sure = client.recv(1024)
#     print(data_sure.decode())
# client.close()

