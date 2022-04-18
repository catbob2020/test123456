#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 0:25
# @Author  : 章
# @File    : test_c1.py
# @Software: PyCharm
# import socket
# import time
# sk = socket.socket()
# sk.connect(("127.0.0.1", 6666))
# # time.sleep(10)
# def my_recv():
#     len_str = int(sk.recv(4).decode("utf-8"))
#     msg = sk.recv(len_str)
#     print(len_str)
#     print(f"来自服务端的消息：{msg.decode('utf-8')}")
# my_recv()
# my_recv()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 17:39
# @Author  : 章
# @File    : client_struct.py
# @Software: PyCharm
# -*- coding: UTF-8 -*-
# import threading
# import socket
# import time
# import struct

#
#
# class Client:
#     SERVER_IP = 'localhost'
#     PORT = 8888
#
#     def __init__(self, serve_ip=SERVER_IP, port=PORT):
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
#         self.client.connect((serve_ip, port))  # 建立一个链接，连接到服务器端口
#
#     def __del__(self):
#         self.client.close()
#
#     def close(self):
#         self.client.close()
#
#     def sender(self):
#         while True:
#             time.sleep(0.1)
#             # msg = input("发送的信息：").strip()   #防止空格和回车发送空消息
#             ms = input("发送的信息：")
#             msg = ms.encode('utf-8')
#             length_ms = struct.pack('i',len(msg))
#             if not ms.strip():
#                 print("消息不能为空.")
#                 continue
#             self.client.send(length_ms)
#             self.client.send(msg)
#
#     def receiver(self):
#         while True:
#             # time.sleep(1)
#             length_msg = self.client.recv(4)
#             length = struct.unpack('i',length_msg)[0]
#             msg = self.client.recv(length).decode('utf-8')
#             print(msg)

# len_str = int(self.client.recv(4).decode("utf-8"))
# len_str = int(self.client.recv(4).decode("utf-8"))
# len_str = int(len_str)
# print(len_str)
# msg = self.client.recv(len_str)
# print(msg.decode('utf-8'))


# data = self.client.recv(1024)
# if not data:
#     print("\n没有消息。")
#     break
# msg = data.decode('utf-8')
# # print("\n收到的信息：", msg)
# print("\n", msg)
#
#     def loop(self):
#         receiver = threading.Thread(target=self.receiver)
#         receiver.start()
#         sender = threading.Thread(target=self.sender)
#         sender.start()
# if __name__ == '__main__':
#     c = Client()
#     c.loop()
# list = [1,2,3,'4',5]
# sum = 0
# for i in list:
#        try:
#               sum += i
#        except:
#               print('非法操作')
#               # break
# print(sum)  #即使有错 还是有计算结果
# age = input('输入年龄').strip()
# if age.isdigit():
#        age = int(age)
#        if age >18:
#               print('猜 对了')
#        else:
#               print('错了')
# else:
#        print('请输入数字')  #if else 过滤报错

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# num1 = max(nums[0:3])
# num2=max(nums[1:4])
# num3= max(nums[2:5])
# num4 =max(nums[3:6])
# num5 = max(nums[4:7])
# num6 =max(nums[5:8])
# new_num = [num1,num2,num3,num4,num5,num6]
# print(new_num)



def get_new_num(nums: list, k: int):

    new_num = []

    n = len(nums)
    i = n-k+1
    if k == 0 or k == n:
        new_num = [max(nums)]
        return new_num
    else:
        for j in range(i):
            new_num.append(max(nums[j:j+k]))
        return new_num



# def get_lst(k,lst1):#lst1为老列表，lst2为新列表，k为翻转数量
#     i = len(lst1)-k+1
#     for j in range(i):
#         lst2.appemd(max(lst1[j:j+k-1]))






# n1 = [1,3,-1,-3,5,3,6,7]
# k1 = 0
# print(get_new_num(n1,k1))


