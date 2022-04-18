# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2022/4/8 10:55
# # @Author  : 章
# # @File    : pra_01.py
# # @Software: PyCharm
# import socket,threading
# import tkinter as tk
# #创建套接字
# a = 1
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(("127.0.0.1",5678))#此处端口看服务端的端口，127.0.0.1要改成服务端主机的ipv4地址
# print('已链接服务端,通讯加密中')
# def shou(s,msg_text):
#     recv_data = s.recv(1024).decode('utf-8')
#     msg_text.insert(tk.END, recv_data)
#     while 1:
#         recv_data = s.recv(1024).decode('utf-8')
#         msg_text.insert(tk.END,recv_data)
# def fa():
#     global a
#     if a == 0:
#         msg = input_text.get('0.0',tk.END)
#         s.send(msg.encode('utf-8'))
#         input_text.delete('0.0',tk.END)
#     else:
#         msg = input_text.get('0.0', tk.END)
#         s.send(msg.encode('utf-8'))
#         input_text.delete('0.0', tk.END)
#         msg_text.delete('0.0', tk.END)
#         a = 0
#
# app = tk.Tk()
# app.title('聊天室')
# #显示消息框
# msg_frame = tk.Frame(app,width=480,height=300)
# msg_frame.grid(row=0,column=0,padx=6,pady=6)
# msg_frame.grid_propagate(0)#固定Frame的大小
# msg_text = tk.Text(msg_frame,bg='white')
# msg_text.grid()
# # msg_text.insert('0.0','hhh')
# #输入
# input_frame = tk.Frame(app,width=480,height=100)
# input_frame.grid(row=1,column=0)
# input_frame.grid_propagate(0)
# input_text = tk.Text(input_frame,bg='white')
# input_text.grid()
# #发送按钮
# btn_frame = tk.Frame(app,width=480,height=20)
# btn_frame.grid(row=2,column=0,sticky='E')
# button = tk.Button(btn_frame,text='发送',command=fa)
# button.grid()
# #线程
# t1 = threading.Thread(target=shou,args=(s,msg_text))
# t1.daemon = True
# t1.start()
# app.mainloop()
# #s.close()
#
a= "公告"+input()
print(a)