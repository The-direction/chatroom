# -*- coding: utf-8 -*-

from PyQt5 import QtCore
import re


class myThread(QtCore.QThread):
    pressed = QtCore.pyqtSignal(str)
    answer = QtCore.pyqtSignal(str)
    jilu = QtCore.pyqtSignal(str)

    def __init__(self, s):
        super(myThread, self).__init__()
        print('+----------------Qthread开始--------------------------+')
        self.s = s
        self.message = ""

    def run(self):
        while 1:
            self.sleep(0.3)
            msg = self.s.recv(1024)
            self.message = msg.decode()           
            if msg:
                # print('-----Qthread----run()-----',msg.decode())
                if msg.decode() == "不能添加自己为好友":
                    self.answer.emit(self.message)
                elif msg.decode() == "好友已存在":
                    self.answer.emit(self.message)
                elif self.message == "#exit#":
                    break
                elif '#jilu#' in self.message:
                    self.jilu.emit(self.message)
                elif self.message == '#over':
                    self.jilu.emit(self.message)
                else:
                    print('有消息')
                    # self.message = msg.decode()
                    # print('-------',msg,'-----thread-run')
                    self.pressed.emit(self.message)
        self.sleep(1)
        print("+----------------Qthread结束-----------------+")


