# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2022/4/13 0:24
# # @Author  : 章
# # @File    : test_s1.py
# # @Software: PyCharm
# import socket
# sk = socket.socket()
# sk.bind(("127.0.0.1", 6666))
# sk.listen(5)
# conn, address = sk.accept()
# def my_send(msg):
#     bs = msg.encode("utf-8")
#     len_str = format(len(bs), "04d") # 定长4位
#     conn.send(len_str.encode("utf-8"))
#     conn.send(bs)
#     print(bs.decode('utf-8'))
# # my_send(input(">>>:").strip())
# # my_send(input(">>>:").strip())
# msg1 = 'hello'
# msg2 = 'world'
# my_send(msg1)
# my_send(msg2)
# # a= 'hello'
# # b=a.encode('utf-8')
# # # print(b,type(b))
# #
# # c=format(len(b),"04d")
# # # c=b.decode('utf-8')
# # print(c)
# # d=c.encode('utf-8')
# # print(d,type(d))
# # d2=d.decode('utf-8')
# # print(d2)

def longestArithSeqLength(A):
    n = len(A)
    if 0 == n:
        return 0
    res = 0
    tmp = [{} for i in range(n)]
    # tmp = [set() for i in range(n)]
    for i in range(n):
        for j in range(0, i):
            diff = A[i] - A[j]
            if diff in tmp[j]:
                tmp[i][diff] = tmp[j][diff] + 1
            else:
                tmp[i][diff] = 2
            res = max(res, tmp[i][diff])
    return res
A =[9,4,7,2,10]
print(longestArithSeqLength(A))