#!/usr/bin/env python3
# coding=utf-8


from demo import *
from clientMain import Client
from clientHandler import Client_handler
import sys
import signal
import os

HOST = '127.0.0.1'
PORT1 = 8080
PORT2 = 8081
PORT3 = 8082
ADDR1 = (HOST, PORT1)
ADDR2 = (HOST, PORT2)
ADDR3 = (HOST, PORT3)
path = os.path.split(os.path.realpath(__file__))[0]
print(path)

try:
    # 创建客户端
    client = Client(ADDR1)
    # 处理客户端
    c_handler = Client_handler(client.sockfd, ADDR2, ADDR3, path)
except Exception as e:
    print('error', e)


# def func(sig, frame):
#     if sig == signal.SIGINT:
#         c_handler.exit()


# signal.signal(signal.SIGINT, func)

app = QApplication(sys.argv)
demo = Demo(c_handler)
demo.show()
sys.exit(app.exec_())