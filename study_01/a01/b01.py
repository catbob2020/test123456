# conn.close() # 关闭连接
import sys
# print('1')
# exit('再见')
# print(2)
# -*- coding: utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='nba2',
                     # charset='utf-8'
                     # autocommit=True
                     )
# print('hello')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# sq3='show tables'
# sq1='select * from account'
# sq2 ='insert into account(id,name,money,messsage) values (null,'li',5000,'hello')'
# sq3 = 'insert into account(id) VALUES(3) '
# sq4 = 'insert into account(name) VALUES('jack')'
# sq4 = '''insert into account(name) VALUES('王五')'''
# sq4 = '''insert into account(message) VALUES('你好')'''
# sq4 = '''insert into account(id,message) VALUES(5,'你好好好是的好') '''
# sq5 ='''update account set message='不在' where id =5'''
# ab = input('请输入信息')
a ='你好呀ss'
# a='5678'
# a='hello'
# sq5 ="update tb_te1 set cla_3={} where id =3".format(a)
sq5 ="update tb_te1 set cla_3='%s' where id =3" % a
# sq5 ="update tb_te1 set cla_3='你好呀' where id =3"
cursor.execute(sq5)
db.commit()
db.close()