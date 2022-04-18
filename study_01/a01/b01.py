# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2022/4/1 0:48
# # @Author  : 章
# # @File    : b01.py
# # @Software: PyCharm
# import turtle
#
# turtle.setup(500,500,100,100)
# turtle.bgcolor('yellow')
# turtle.showturtle()
#
#
#
# turtle.done()
#
# a='123000900'


# def fun(a):
#     li = []
#     for i in a:
#         li.append(int(i))
#     return li


# c='000700100'
# def get_list():
#     m = []
#     for c in range(3):
#         ac = input()
#         m.append(fun(ac))
#     return m


# print(get_list())
# print(np.matrix(get_list()))
# print(get_list())
# from functools import reduce
# lst=[1,2,3,4]
# print(reduce(lambda x,y: x*y, lst))
# a= 0
# while a <5:
#     print(a+1)
#     a+=1
# def sum_demo(x, y):
#     for _ in range(2):
#         x += 1
#         y += 1
#         result = x + y
#     return result
#
# if __name__ == '__main__':
#     result = sum_demo(1, 1)
#     print(result)
# import time
# result = 0
# for i in range(100000):
#     result+=i
# print(result)
# import threading  #多线程
# def fun(a1,a2,a3):
#     pass
# t= threading(target=fun,args=(11,12,13))
# t.start()
# import multiprocessing #多进程
# import threading
# import time
# st=time.time()
# def tstart(arg):
#     time.sleep(0.5)
#     print("%s running...." % arg)
# tstart('hello')
# et=time.time()
# tt=et-st
# print(tt)
# if __name__ == '__main__':
#     st=time.time()
#     t1 = threading.Thread(target=tstart, args=('This is thread 1',))
#     t2 = threading.Thread(target=tstart, args=('This is thread 2',))
#     t1.start()
#     t2.start()
#     et = time.time()
#     tt = et - st
#     print(tt)
#     print("This is main function")
# import socket
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('192.168.1.102',8001))
# sock.listen(5)
# while True:
#     conn,addr = sock.accept()
#     print('有人来聊天了')
#     conn.sendall('你是来找我聊天的吗'.encode('utf-8'))
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             break
#         data_string = data.decode('utf-8')
#         print('对方的消息为：',data_string)
#         huihua = input('')
#         conn.sendall(huihua.encode('utf-8'))
#     print('断开连接了')
#     conn.close()
import mysql.connector
# import mysql.connector.errorcode

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'iteast',
    passwd = '123456'
)
print(mydb)


#
# if __name__ == '__main__':
#     conn = mysql.connector.connect()
