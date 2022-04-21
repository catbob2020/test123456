#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import mysql.connector
#
# # 1、打开数据库连接
# mydatabase = mysql.connector.connect(
#     host = "localhost" , # 服务器地址
#     port = 3306, # 端口
#     user = "root" , # 用户名
#     passwd = "123456" , # 密码
#     buffered = True
#     #auth_plugin = 'mysql_native_password'
# )
#
# # 2、使用cursor()方法获取操作游标
# cursor = mydatabase.cursor()
#
# # 3.1、判断数据库是否存在，存着则删除
# cursor.execute('DROP DATABASE IF EXISTS nba')
#
# # 3.2、判断数据库是否存在，不存着则新建
# cursor.execute('CREATE DATABASE IF NOT EXISTS NBA')
# cursor.execute('CREATE DATABASE IF NOT EXISTS NBA2')
#
# # 4、查看所有数据库
# cursor.execute("SHOW DATABASES")
#
# # 5、使用 fetchall() 方法获取返回数据
# data = cursor.fetchall()
#
# # 6、输出所有数据库名称
# print(data)
#
# # 7、关闭数据库连接
# mydatabase.close()
# import pymysql

# import mysql.connector
# conn=mysql.connector.connect(
#     host = 'localhost',
#     user = 'root'
# )
# cur = conn.cursor() # 生成游标对象
# sql="select * from student " # SQL语句
# cur.execute(sql) # 执行SQL语句
# data = cur.fetchall() # 通过fetchall方法获得数据
# for i in data[:2]: # 打印输出前2条数据
# print (i)
# cur.close() # 关闭游标
# conn.close() # 关闭连接
# import sys
# # print('1')
# # exit('再见')
# # print(2)
#
# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='123456',
#                      database='nba2',
#                      # charset='utf-8'
#                      # autocommit=True
#                      )
# print('hello')
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # sq3='show tables'
# # sq1='select * from account'
# # sq2 ='insert into account(id,name,money,messsage) values (null,'li',5000,'hello')'
# # sq3 = 'insert into account(id) VALUES(3) '
# # sq4 = 'insert into account(name) VALUES('jack')'
# # sq4 = '''insert into account(name) VALUES('王五')'''
# # sq4 = '''insert into account(message) VALUES('你好')'''
# # sq4 = '''insert into account(id,message) VALUES(5,'你好好好是的好') '''
# sq5 ='''update account set message='不在' where id =5'''
#
# cursor.execute(sq5)
# db.commit()
#
# # # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchone()
# # data = cursor.fetchone()
# # data = cursor.fetchall()
#
# # print("show : %s " % data)
# # for i in data:
# #     print(i)
# # 关闭数据库连接
# db.close()
import os
print(os.getcwd())