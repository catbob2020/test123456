# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2022/4/8 19:40
# # @Author  : 章
# # @File    : talk_clientv2.py
# # @Software: PyCharm
# import threading
# # loop = 1000000
# # number = 0
# # def add(count):
# #     global number
# #     for i in range(count):
# #         number+=1
#
# # t = threading.Thread(target=add,args=(loop,))
# # t.start()
# # # t.join()
# # print(number)
# # def sub(count):
# #     global number
# #     for i in range(count):
# #         number -=1
# #
# # t1 = threading.Thread(target=add,args=(loop,))
# # t2 = threading.Thread(target=sub,args=(loop,))
# # t1.start()
# # t1.join()
# # t2.start()
# # t2.join()
# # print(number)
#
# #主线程与子线程
# # import threading
# # import time
# #
# # def thread():
# #     time.sleep(2)
# #     print('---子线程结束---')
# #
# # def main():
# #     t1 = threading.Thread(target=thread)
# #     t1.setDaemon(True)  #开启True  强行终止所有子线程
# #     t1.start()
# #     print('---主线程---结束')
# #
# # if __name__ == '__main__':
# #     main()
# import asyncio
# import time
# async def say_after(delay,what):
#     await asyncio.sleep(delay)
#     print(what)
# # async def main():
# #     # print('hello')
# #     print(f"start at {time.strftime('%X')}")
# #     # await asyncio.sleep(1)
# #     await say_after(1,'hello')
# #     await say_after(2,'world')
# #     # print('world')
# #     print(f"finished at {time.strftime('%X')}")
#
# async def main():
#     task1 = asyncio.create_task(say_after(1,'hello'))
#     task2 = asyncio.create_task(say_after(2,'world'))
#     print(f"start at {time.strftime('%X')}")
#     await task1
#     await task2
#     print(f"finished at {time.strftime('%X')}")
#
# asyncio.run(main())
#
#
# x,y =input('请输入值').split()
# x,y =input().split()
# print(x,y)
# a= input('please input')
# print(a)
# print(type(a))

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

            msg = input("发送的信息：")
            if not msg.strip():
                print("消息不能为空.")
                continue
            self.client.send(msg.encode('utf-8'))

    def receiver(self):
        while True:
            data = self.client.recv(1024)
            # if not data:
            #     print("\n没有消息。")
            #     break
            msg = data.decode('utf-8')
            # print("\n收到的信息：", msg)
            print("\n", msg)

    def loop(self):
        receiver = threading.Thread(target=self.receiver)
        receiver.start()
        sender = threading.Thread(target=self.sender)
        sender.start()
if __name__ == '__main__':
    c = Client()
    c.loop()
