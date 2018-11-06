from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import signal
import os
import re
import time
from clientChat import F_thread
from Ui_1v1 import *
from Ui_qunliao import *
# from lanse import MyMainWindow


class loginPage(QDialog):
    def __init__(self, c_handler):
        self.c_handler = c_handler
        #print(self.c_handler.username)
        #多人聊天室
        self.s = self.c_handler.s
        # 好友列表/单人聊天
        self.z = self.c_handler.z
        super().__init__()
        self.setStyleSheet(
            'QPushButton{background-color:#F5F3ED;border:none;font-size:16px;}')
        # Qthread中创建的信号
        self.rlist = []
        # 好友列表 {好友名称:窗口}
        self.add_friend_button = []
        self.setWindowTitle(self.c_handler.userlist[0])
        self.setGeometry(900, 100, 270, 480)
        user_button = QPushButton('>我的好友', self)
        users_button = QPushButton('>我的群聊', self)
        self.user_list = QListWidget()
        self.user_list.setFont(QFont('黑体', 14))
        self.layout = QGridLayout()
        self.layout.addWidget(users_button, 1, 0)
        self.layout.addWidget(user_button, 2, 0)
        self.layout.addWidget(self.user_list, 3, 0)
        self.setLayout(self.layout)

        user_button.clicked.connect(self.find_friend)
        users_button.clicked.connect(self.createchat)
        # user_button.setFont(QFont('黑体', 15))
        # user_button.resize(80, 30)
        # user_button.move(50, 60)
        # user_button.setStyleSheet(
        # 'QPushButton{background-color:#FFE3E5;border:none;}')
        # self.listfile = QListWidget()
        # self.listfile.resize(80,50)
        # self.listfile.move(100,100)

        # users_button.setFont(QFont('黑体', 15))
        # users_button.resize(80, 30)
        # users_button.move(50, 10)
        # users_button.setStyleSheet(
        # 'QPushButton{background-color:#FFE3E5;border:none;}')
        # self.find_friend()

    # def check_func(self):
    #     self.chat_in_room = Chatthread(
    #         target=self.createchat, args=(self.c_handler.s,))
    #     self.chat_in_room.start()
    #     self.chat_in_room.join()

    def find_friend(self):
        print('创建线程收取消息')
        self.f_th = F_thread(self.z)
        self.f_th.friendlist_recv.connect(self.show_list)
        self.add_signal(self.f_th.friendlist_recv)
        self.f_th.start()

    def add_signal(self, SIG):
        self.rlist.append(SIG)

    def show_list(self, f_info):
        print(f_info, "-----show_list----")
        f_info = f_info.decode()
        # if f_info == '###':
        #     print('没有好友')
        #     pass
        # else:
        L = re.findall(r'.+###',f_info)
        if L:
            friend_l = re.split(r'\W', L[0])
            l = friend_l[:-3]
            print(l)
            if l:
                self.user_list.clear()
                for friend_n in l:
                    #把好友信息都添加到列表里
                    self.user_list.addItem(friend_n)
        else:
            print('没有好友')
            # self.user_list.addItem
            self.user_list.clear()

        self.user_list.itemClicked.connect(self.createchat_1)
                #每循环一次，就刷新一次
        QApplication.processEvents()
        time.sleep(0.1)
        self.user_list.setContextMenuPolicy(3)
        self.user_list.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)

        # print(friend_n) 

        # 点击创建新窗口
        # self.user_list.itemClicked.connect(self.test)

    # def test(self,item):
    #     print('============================')
    #     print(item.text())
    #     print('============================')
    def rightMenuShow(self, point):
        print('--point:--',point)
        rightMenu = QMenu(self.user_list)
        addAction = QAction(u"删除好友", self, triggered=self.remove_Item)       # 也可以指定自定义对象事件
        rightMenu.addAction(addAction)
        rightMenu.exec_(QtGui.QCursor.pos())

    def remove_Item(self):
        print('-----删除------')
        name = self.user_list.currentItem().text()
        print(name)
        data = b'##remove_my_friend##' + name.encode()
        self.z.send(data)
        self.user_list.removeItemWidget(self.user_list.takeItem(self.user_list.row(item)))

    def createchat_1(self, item):
        friend_n = item.text()
        classname = friend_n + "page"

        class classname(Mychatwindow):
            def __init__(self, s, obj, parent=None):
                super().__init__(s, obj)
                
        self.chat_page1 = classname(self.z, friend_n)
        self.chat_page1.show()

    def createchat(self, s):
        # Ui_qunliao
        self.chat_page = MyMainWindow(self.s, self.c_handler.ADDR3)
        self.chat_page.show()

    def closeEvent(self, event):
        print('退出客户端')
        self.c_handler.exit()
        # os.kill(os.getpid(), signal.SIGINT)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("bgpic/bgpic5.jpg")
        painter.drawPixmap(self.rect(), pixmap)
