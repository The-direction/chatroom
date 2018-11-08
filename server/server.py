#!/usr/bin/env python3
# coding=utf-8

'''
name : Zhou
data : 2018-9-28
email : 18871778583@163.com
modules : python3.5 pymysql re
This is a chatroom server for AID1807
'''
from socket import *
from pymysql import *
from threading import Thread
from select import select
from Mysqlhandler import mySqlHandler
# from audioS import Audio_Server
import sys
import re
import time


# 设置本地服务器监听端口
HOST = '0.0.0.0'
PORT1 = 8080
PORT2 = 8081
PORT3 = 8082
ADDR1 = (HOST, PORT1)
ADDR2 = (HOST, PORT2)
ADDR3 = (HOST, PORT3)
# 客户端套接字列表
# rlist = []
# 客户端套接字－－－用户名:套接字
userdict = {}
userchatdict = {}

# 创建Server类


class Server:
    def __init__(self, ADDR1, ADDR2, ADDR3):
        self.ADDR1 = ADDR1
        self.ADDR2 = ADDR2
        self.ADDR3 = ADDR3
        # 设置监听套接字
        # 登录，注册，多人聊天
        self.sockfd = socket()
        # 单人聊天
        self.zockfd = socket()
        # 设置端口立即释放
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.zockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # 绑定本地地址和端口
        self.sockfd.bind(self.ADDR1)
        self.zockfd.bind(self.ADDR2)
        # 设置监听
        self.sockfd.listen(5)
        self.zockfd.listen(5)
        self.mysql_h = mySqlHandler()
        self.run()

    def run(self):
        print('启动服务端....')
        # self.mysql_h.firststartdb()
        while 1:
            try:
                # 等待连接
                c, addr = self.sockfd.accept()
                print('服务端等待连接...=====')
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('服务端退出')
            except Exception:
                print('连接错误')
                continue
            # 调用连接请求处理函数
            self.accept_handler(c)

    def accept_handler(self, c):
        # rlist.append(c)
        mth = Mythread_handler(c, self.zockfd, self.mysql_h, self.ADDR3)
        t = Mythread(target=mth.handler, args=(c,))
        t.start()


# 重写线程类,重写__init__和run函数
class Mythread(Thread):
    def __init__(self, target, args=(), kwargs={}):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        # 继承Thread的__init__函数
        super().__init__()
        # 分支线程随主线程退出而退出
        self.setDaemon(True)

    def __del__(self):
        print('退出--->> ', self.name)
        self.args[0].close()

    def run(self):
        print('这是分支线程:', self.name)
        # 调用Mythread_handler类中handler函数
        self.target()


# 封装,创建线程处理类
class Mythread_handler:
    def __init__(self, c, zockfd, mysql_h, ADDR3):
        self.c = c
        self.zockfd = zockfd
        self.username = ''
        self.mysql_h = mysql_h
        self.ADDR3 = ADDR3

    def __del__(self):
        print('客户端退出')
        # 从客户端套接字列表中去掉已退出的套接字
        # rlist.remove(self.c)
        self.exit_record()

    # 单人聊天等待链接
    def one_chat_connet(self):
        print("等待连接")
        time.sleep(1)
        try:
            # 等待连接
            c_for_one, addr = self.zockfd.accept()
            print('单人聊天等待连接...=====')
        except KeyboardInterrupt:
            print("按键错误")
        except Exception:
            print('连接错误')
        print('单人聊天套接字已经连接')
        uname = c_for_one.recv(2014).decode()
        userchatdict[uname] = c_for_one
        # self.chatone(c_for_one)
        return c_for_one
        # 调用连接请求处理函数

    # 单人聊天
    def chatone(self):
        data = self.xiaoxi
        try:
            print('-----', data, '-------')
            # if re.findall(r'^\w+$', data) == ['exit']:
            #     break
            name = re.findall(r'^\w+\:', data.decode())[0]
            # n = len(name)
            # data = data[n:]
            objname = name[:-1]
            self.mysql_h.save_xiaoxi(self.username, objname, data.decode())
            userchatdict[objname].send(data)
        except Exception as e:
            print(e)

    def handler(self):
        print('服务端处理函数')
        print('========Connect from', self.c.getpeername(), '========')
        while 1:
            data = self.c.recv(1024).decode()
            print(data)
            # 正则判定
            L = re.split(r'[ ]+', data)
            option = L[0]
            # 根据请求的首字母选择功能函数
            try:
                if option == 'L':
                    self.login(L)
                elif option == 'R':
                    self.register(L)
                elif option == 'E':
                    print('exit--->> ', self.c.getpeername())
                    # 结束线程
                    return
                else:
                    self.c.send(b'===error===')
            except MyException:
                # 捕获代表操作成功的异常,结束请求处理循环
                print('开始聊天')
                break
            except BrokenPipeError:
                # 结束线程
                break

        # IO多路复用
        self.z = self.one_chat_connet()
        rlist = [self.c, self.z]
        wlist = []
        xlist = [self.c, self.z]
        print("等候选择聊天对象")
        while 1:
            # 提交监控对象
            rs, ws, xs = select(rlist, wlist, xlist)
            for r in rs:
                if r is self.c:
                    print("self.c收到消息")
                    data = self.c.recv(2014)
                    if not data:
                        continue
                    if data == b'OK all':
                        self.guanliyaun()
                    # elif re.findall(r'^##add_my_friend##', data.decode()) is not None:
                    elif '##add_my_friend##' in data.decode():
                        self.add_friend(data)

                    elif data == b'E':
                        # 结束线程
                        rlist = []
                        self.z.close()
                        self.c.close()
                        break
                    elif data == b"##xiaoxijilu##":
                        self.mysql_h.qunxiaoxijilu(self.c)       
                    else:
                        # 储存消息
                        self.qunxiaoxi = data
                        # self.chucun1(data)
                        wlist.append(self.c)
                if r is self.z:
                    print("self.z收到消息")
                    text = self.z.recv(1024)
                    if not text:
                        continue
                    print(text)
                    if text == b'friendlist':
                        print('好友列表')
                        self.find_friend()
                    # elif re.findall(r'^##remove_my_friend##', text.decode()) is not None:
                    elif '##remove_my_friend##' in text.decode():
                        self.remove(text)
                    elif text == b'#exit#':
                        self.z.send(text)
                    
                    else:
                        print(text)
                        self.xiaoxi = text
                        # self.chucun2(data)
                        wlist.append(self.z)
            for w in ws:
                if w is self.c:
                    self.chatroom()
                    wlist.remove(w)
                if w is self.z:
                    self.chatone()
                    wlist.remove(w)
            if not rlist:
                break

        # # 发送聊天确认信息
        # while 1:
        #     time.sleep(1)
        #     print("等候选择聊天对象")
        #     data = self.c.recv(1024)
        #     if data == b'OK all':
        #         self.chatroom()
        #     if data == b'OK one':
        #         # 连接套接字
        #         self.one_chat_connet()
        #     elif data == b'friendlist':
        #         print('好友列表')
        #         self.find_friend()
        #     if data == b'E' or data == b'exit':
        #         # 结束线程
        #         break

    def remove(self, text):
        self.mysql_h.removefriendtomysql(self.c, self.username, text)
        # print('---------删除好友----------')
        # friendname = text[20:].decode()
        # print(friendname)
        # text = ''
        # with open('../friendlist.txt', 'r+') as f:
        #     print('==============================')
        #     for line in f:
        #         print(line)
        #         L = re.split(r'\s', line)
        #         print(L)
        #         if self.username == L[0]:
        #             # 删除好友名单
        #             L.remove(friendname)
        #             L.pop(-1)
        #             print("成功删除")
        #             line = ' '.join(L) + '\n'
        #             # self.c.send('添加成功'.encode())
        #         text += line
        #     print('=================================')
        # with open('../friendlist.txt', 'wt') as f:
        #     print(text)
        #     f.writelines(text)

    def add_friend(self, data):
        self.mysql_h.addfriendtomysql(self.c, self.username, data)
        # print('---------添加好友----------')
        # friendname = data[17:].decode()
        # text = ''
        # with open('../friendlist.txt', 'r+') as f:
        #     for line in f.readlines():

        #         if self.username in re.findall(r'^\w+', line):
        #             if friendname in line:
        #                 if friendname == self.username:
        #                     self.c.send("不能添加自己为好友".encode())
        #                 else:
        #                     print(friendname, self.username)
        #                     self.c.send("好友已存在".encode())
        #             else:
        #                 line = line[:-1] + ' ' + friendname + '\n'
        #                 self.c.send('添加成功'.encode())
        #         text += line
        # with open('../friendlist.txt', 'r+') as f:
        #     f.writelines(text)
        #     print(text)

    def save(self, data):
        line = self.username + ' ' + data[17:].decode() + '\n'
        with open('../friendlist.txt', 'r+') as f:
            f.writelines(line)
            print('添加好友，没有已存好友')
            print(line)

    # def show_friend(self):
    #     with open('../friendlist.txt', 'rt') as f:
    #         for line in f:
    #             print(line)
    #             if self.username in re.findall(r'^\w+', line):
    #                 #　发送好友列表
    #                 self.c.send(line.encode())
    #                 break

    def guanliyaun(self):
        s = "管理员消息：%s已登录" % self.username
        s += '#&&#'
        for conndf in userdict.values():
            conndf.send(s.encode())

    # 显示好友列表
    def find_friend(self):
        self.mysql_h.showfriendformysql_one(self.z, self.username)
        # with open('../friendlist.txt', 'rt') as f:
        #     for line in f:
        #         print(line)
        #         if self.username in re.findall(r'^\w+', line):
        #             #　发送好友列表
        #             self.z.send(line.encode())

    # 多人聊天室
    def chatroom(self):
        try:
            # data = self.c.recv(1024)
            # if re.findall(r'^\w+$', data.decode()) == ['exit']:
            #     print("退出聊天室")
            #     break
            if self.qunxiaoxi == b'##friendlist##':
                onlinelist = ''
                for name in userdict:
                    name = name + ' '
                    onlinelist += name
                onlinelist = b'##friendlist##' + onlinelist.encode()
                print('在线用户 ====== ', onlinelist)
                self.c.send(onlinelist)
            else:
                if self.qunxiaoxi == b"##audiochat##":
                    self.yuyinchat()
                if self.qunxiaoxi == b'#exit#':
                    self.c.send(b'#exit#')
                else:
                    self.mysql_h.save_qunxiaoxi(self.username, self.qunxiaoxi.decode())
                    data = self.username.encode() + b' : ' + self.qunxiaoxi
                    data += b'#&&#'
                    print(data.decode())
                    for conndf in userdict.values():
                        conndf.send(data)
        except Exception as e:
            print(e)

    def yuyinchat(self):
        print('语音客户端')
        # self.au_s = Audio_Server(self.ADDR3)

    def register(self, L):
        try:
            self.mysql_h.registertomysql(L, self.c)
        #     with open('../userinformation.txt', 'rt') as f:
        #         for line in f:
        #             l = re.split(r'[ ]+', line)
        #             # 查看用户名是否已存在
        #             if l[0] == L[1]:
        #                 self.c.send('用户已存在'.encode())
        #                 break
        #         else:
        #             self.c.send(b'register')
        #             print('正在注册')
        #             raise MyException
        # except MyException:
        #     # 保存信息记录
        #     with open('../userinformation.txt', 'at') as f:
        #         s = ' '.join(L[1:])
        #         s += ' ' + time.ctime()
        #         f.write(s + '\n')
        except Exception as e:
            print('注册数据库处理错误', e)

    def login(self, L):
        try:
            self.mysql_h.logintomysql(self.c, L, self.username, MyException)
        #     with open('../userinformation.txt', 'rt') as f:
        #         for line in f:
        #             l = re.split(r'[ ]+', line)
        #             if L[1] == l[0]:  # 匹配姓名
        #                 if L[2] == l[1]:  # 匹配密码
        #                     # 判断用户是否已登录
        #                     for name in userdict:
        #                         if name == L[1]:
        #                             self.c.send('用户已登录'.encode())
        #                             break
        #                     else:
        #                         self.c.send(b'login')
        #                         print('正在登录...')
        #                         # 登录成功，抛出自定义异常
        #                         self.login_record(L[1])
        #                         raise MyException
        #                     break
        #                 else:
        #                     self.c.send('密码错误'.encode())
        #                     break
        #         else:
        #             print('==================================')
        #             self.c.send('用户不存在'.encode())
        except MyException:
            self.login_record(L[1])
            raise MyException
        except Exception as e:
            print('登录数据库处理错误', e)

    def login_record(self, username):
        self.username = username
        # 在已登录字典中添加username和套接字
        userdict[self.username] = self.c
        self.mysql_h.recordtomysql_login(self.username)
        # with open('../records.txt', 'at') as f:
        #     s = username + ' login ' + time.ctime()
        #     f.write(s + '\n')

    def exit_record(self):
        if self.username:
            # 在登录字典中去掉username和它的套接字
            del userdict[self.username]
            self.mysql_h.recordtomysql_exit(self.username)
            # with open('../records.txt', 'at') as f:
            #     s = self.username + ' exit ' + time.ctime()
            #     f.write(s + '\n')


# 定义一个异常类，用来传递操作成功的消息
class MyException(Exception):
    def __init__(self):
        Exception.__init__(self)

        # 创建IO多路复用


if __name__ == '__main__':
    server = Server(ADDR1, ADDR2, ADDR3)
