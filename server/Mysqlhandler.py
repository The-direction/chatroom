# coding=utf-8
# date : 2018-10-16
# e-mail : 565401702@qq.com
# description : 此模块为mysql数据库的调用模块,一些类和函数说明将会再以下说明
# class : AID1806-online
# python3.5 mysql pymysql
import pymysql
import re
import time


class mySqlHandler:
    # 数据库处理对象的初始化,连接到本地服务器
    def __init__(self):
        self.db = pymysql.connect(
            'localhost', 'root', '123456', charset='utf8')
    # 对象首次允许创建数据库和表,注意不要重复使用

    def firststartdb(self):
        self.cur = self.db.cursor()
        # self.cur.execute('create database if not exists projectdb;')
        self.cur.execute('use projectdb;')
        self.cur.execute('create table if not exists userinformation(\
                          username char(20) not null primary key,\
                          password char(20) not null,\
                          createtime char(30) not null);')
        self.cur.execute('create table if not exists friendlist(\
                          username char(20) not null,\
                          friendname char(20));')
        self.cur.execute('create table if not exists records(\
                          username char(20) not null,\
                          message char(10) not null,\
                          createtime char(30) not null);')
        # self.cur = self.db.cursor()
        # self.cur.execute('use projectdb;')
        self.cur.execute(
            'create table qunxiaoxi(username char(20),xiaoxi varchar(70),keeptime varchar(30));')
        self.cur.execute(
            'create table xiaoxi(username char(20),duixiang char(20),xiaoxi varchar(70),keeptime varchar(30));')
        self.cur.close()

        self.db.commit()
        self.cur.close()

    def qunxiaoxijilu(self, c):
        self.cur = self.db.cursor()
        print('读取群消息')
        self.cur.execute('use projectdb;')
        self.cur.execute("select * from qunxiaoxi;")
        L = self.cur.fetchall()
        for t in L:
            text = '#jilu#' + t[2]+' '+t[0] + ':'+t[1]
            c.send(text.encode())
            time.sleep(0.3)
        else:
            c.send(b"#over")
            print('发送完成')

    # 用于注册的操作
    def save_qunxiaoxi(self, username, data):
        self.cur = self.db.cursor()
        print('保存群消息')
        self.cur.execute('use projectdb;')
        self.cur.execute('insert into qunxiaoxi values("%s","%s","%s");' % (
            username, data, time.ctime()))
        print('保存成功')
        self.db.commit()
        self.cur.close()

    def save_xiaoxi(self, username, duixiang, data):
        self.cur = self.db.cursor()
        print('保存消息')
        print(username, duixiang, data)
        self.cur.execute('use projectdb;')
        self.cur.execute('insert into xiaoxi values("%s","%s","%s","%s");' % (
            username, duixiang, data, time.ctime()))
        print('保存成功')
        self.cur.close()

    def registertomysql(self, l, c):
        self.cur = self.db.cursor()
        print('用户注册到数据库')
        # self.registerlist = re.split(r'[ ]+', l)
        self.registerlist = l
        self.cur.execute('use projectdb;')
        self.cur.execute(
            'select username from userinformation where username = "%s";' % self.registerlist[1])
        if not self.cur.fetchall():
            # 此处查明没有重名,可以注册
            self.cur.execute('insert into userinformation values("%s","%s","%s");' % (
                self.registerlist[1], self.registerlist[2], time.ctime()))
            self.db.commit()
            c.send(b'register')
            print('正在注册')

        else:
            # 此处出现重名,发送无法注册消息
            c.send('用户已存在'.encode('utf-8'))
    # 这里由于涉及全局变量的问题我没有动userdict,请自行添加配合
        self.cur.close()

    def recordtomysql_login(self, username):
        self.cur = self.db.cursor()
        print('添加登录信息到数据库')
        self.cur.execute('use projectdb;')
        self.cur.execute('insert into records values("%s","login","%s");' % (
            username, time.ctime()))
        self.db.commit()
        self.cur.close()
        print('添加登录信息成功')

    def recordtomysql_exit(self, username):
        self.cur = self.db.cursor()
        print('添加退出信息到数据库')
        self.cur.execute('use projectdb;')
        self.cur.execute('insert into records values("%s","exit","%s");' % (
            username, time.ctime()))
        self.db.commit()
        self.cur.close()
        print('添加退出信息成功')
    # 此处由于需要服务器判断是否为登录状态,所以需要传入事实记录登录状态的userdict,而且还需要传入MyException异常类,以便跳转

    def logintomysql(self, c, l, userdict, MyException):
        self.cur = self.db.cursor()
        print('用户登录验证数据库')
        # self.loginlist = re.split(r'[ ]+', l)
        self.loginlist = l
        self.cur.execute('use projectdb;')
        self.cur.execute(
            'select * from userinformation where username="%s";' % self.loginlist[1])
        logintuple = self.cur.fetchone()
        if not logintuple:
            c.send('用户不存在'.encode('utf-8'))
        else:
            if logintuple[1] == self.loginlist[2]:
                for name in userdict:
                    if name == self.loginlist[1]:
                        c.send('用户已登录'.encode('utf-8'))
                        return
                    else:
                        pass
                else:
                    c.send(b'login')
                    print('正在登录...')
                    # self.recordtomysql_login(self.loginlist[1])
                    raise MyException
            else:
                c.send('密码错误'.encode('utf-8'))
    # 循环从mysql发送好友信息,这是单人聊天的版本对应self.z
        self.cur.close()

    def showfriendformysql_one(self, z, username):
        self.cur = self.db.cursor()
        print('正在输出好友姓名信息')
        L = []
        self.cur.execute('use projectdb;')
        self.cur.execute(
            'select * from friendlist where username="%s";' % username)
        info = self.cur.fetchall()
        if info:
            for nametuple in info:
                L.append(nametuple[1])
                # z.send(nametuple[1].encode('utf-8'))
                # 防止粘包
                # time.sleep(0.1)
            # 由于客户端不知道有多少好友,所以发送完之后,发送'###'的标志字符串给客户端的while循环,示意停止输出
            # z.send('###'.encode('utf-8'))
            friend_data = ' '.join(L)
            print(username, '的好友', L, '或', friend_data)
            z.send(friend_data.encode() + b'###')
        else:
            z.send(b'###')
        self.cur.close()

    # 循环从mysql发送好友信息,这是多人聊天模式下的版本,对应self.c
    def showfriendformysql_mulit(self, t_object):
        self.cur = self.db.cursor()
        print('正在输出好友姓名信息')
        self.cur.execute('use projectdb;')
        self.cur.execute(
            'select * from friendlist where username="%s";' % t_object.username)
        if self.cur.fetchall():
            for nametuple in self.cur.fetchall():
                t_object.c.send(nametuple[1].encode('utf-8'))
                time.sleep(0.1)
            t_object.c.send('###'.encode('utf-8'))
        else:
            pass
        self.cur.close()

    # 添加好友的操作
    def addfriendtomysql(self, c, username, data):
        self.cur = self.db.cursor()
        print('添加好友')
        addfriendname = data[17:].decode('utf-8')
        if username == addfriendname:
            c.send('不能添加自己为好友'.encode('utf-8'))
        else:
            self.cur.execute('use projectdb;')
            self.cur.execute('select friendname from friendlist where username="%s" and friendname="%s";' % (
                username, addfriendname))
            checktuple = self.cur.fetchall()
            if not checktuple:
                self.cur.execute(
                    'select * from userinformation where username="%s";' % addfriendname)
                checktuple = self.cur.fetchall()
                if checktuple:
                    self.cur.execute('insert into friendlist values("%s","%s");' % (
                        username, addfriendname))
                    self.db.commit()
                    print('添加好友成功')
                    c.send('添加好友成功'.encode('utf-8'))
                else:
                    c.send('用户名不存在'.encode('utf-8'))
            else:
                c.send('好友已存在'.encode('utf-8'))
        self.cur.close()

    def removefriendtomysql(self, c, username, data):
        self.cur = self.db.cursor()
        print('删除好友')
        removefriendname = data[20:].decode('utf-8')
        # if username == removefriendname:
        #     c.send('不能删除自己'.encode('utf-8'))
        # else:
        self.cur.execute('use projectdb;')
        self.cur.execute('select friendname from friendlist where username="%s" and friendname="%s";' % (
            username, removefriendname))
        # if self.cur.fetchone():
        self.cur.execute('delete from friendlist where username="%s" and friendname="%s";' % (
            username, removefriendname))
        self.db.commit()
        print('删除好友成功')
        self.cur.close()
        #     c.send('删除好友成功'.encode('utf-8'))
        # else:
        #     c.send('无法删除好友'.encode('utf-8'))

    # 循环从mysql发送登录,登出信息
    def getoperation(self, t_object):
        self.cur = self.db.cursor()
        print('输出历史记录信息')
        self.cur.execute('use projectdb;')
        self.cur.execute(
            'select * from records where username="%s"' % t_object.username)
        if self.cur.fetchall():
            for history in self.cur.fetchall():
                historystring = '用户' + \
                    history[0] + '在' + history[2] + history[1]
                t_object.c.send(historystring.encode('utf-8'))
                time.sleep(0.1)
            t_object.c.send('###'.encode('utf-8'))
        else:
            pass
    # 测试用,删除数据库
        self.cur.close()

    def __killthedb(self):
        self.cur = self.db.cursor()
        print('警告,正在删除数据库')
        time.sleep(3)
        self.cur.execute('use projectdb;')
        self.cur.execute('drop database projectdb;')
        self.cur.close()

    def truekillthedb(self):
        self.__killthedb()

    # # 记得在一个客户端断开后，删除对象
    # def __del__(self):
    #     print('服务器处理对象已经被删除')
    #     self.cur.close()
    #     self.db.close()


if __name__ == "__main__":
    m = mySqlHandler()
    m.firststartdb()