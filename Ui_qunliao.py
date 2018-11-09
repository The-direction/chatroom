# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_qun.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from recvThread import myThread
import re
import time
from weather import *
# from audioC import *
from PyQt5.QtGui import QIcon
import time
import os


class Ui_Form1(QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, Form):
        path = os.path.split(os.path.realpath(__file__))[0]
        print(path)
        Form.setObjectName("Form")
        Form.resize(675, 444)
        Form.setAutoFillBackground(False)
        path1 = path + '/shaizeiwang3333_看图王.jpg'
        Form.setStyleSheet("#Form\n"
            "{border-image: url(haizeiwang3333_看图王.jpg);}"
            "")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 21, 411, 180))
        self.textBrowser.setStyleSheet("\n"
                                       "background-color: rgb(221, 246, 255);")
        self.textBrowser.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 270, 411, 91))
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setStyleSheet("background-color: rgb(224, 244, 255);")
        self.textEdit.setObjectName("textEdit")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.luyinBtn = QtWidgets.QPushButton(Form)
        self.luyinBtn.setGeometry(QtCore.QRect(80, 230, 91, 27))
        self.luyinBtn.setStyleSheet("background-color: rgb(247, 255, 194);\n"
                                    "background-image: url(999.jpg);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("xiaoxi.jpg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.luyinBtn.setIcon(icon)
        self.luyinBtn.setFlat(True)
        self.luyinBtn.setObjectName("luyinBtn")
        self.tonghuaBtn = QtWidgets.QPushButton(Form)
        self.tonghuaBtn.setGeometry(QtCore.QRect(180, 230, 91, 27))
        self.tonghuaBtn.setStyleSheet("background-color: rgb(245, 255, 194);\n"
                                      "background-image: url(999.jpg);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("tonghu.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tonghuaBtn.setIcon(icon1)
        self.tonghuaBtn.setFlat(True)
        self.tonghuaBtn.setObjectName("tonghuaBtn")
        self.sendBtn = QtWidgets.QPushButton(Form)
        self.sendBtn.setGeometry(QtCore.QRect(370, 370, 61, 31))
        self.sendBtn.setAutoFillBackground(False)
        self.sendBtn.setStyleSheet("background-color: rgb(186, 186, 186);\n"
                                   "background-image: url(100.jpg);\n"
                                   "")
        self.sendBtn.setFlat(True)
        self.sendBtn.setObjectName("sendBtn")
        self.jiluBtn = QtWidgets.QPushButton(Form)
        self.jiluBtn.setGeometry(QtCore.QRect(350, 230, 81, 27))
        self.jiluBtn.setStyleSheet("background-color: rgb(205, 255, 215);\n"
                                   "background-image: url(beijing.jpg);")
        self.jiluBtn.setFlat(True)
        self.jiluBtn.setObjectName("jiluBtn")
        self.quitBtn = QtWidgets.QPushButton(Form)
        self.quitBtn.setGeometry(QtCore.QRect(590, 370, 61, 31))
        self.quitBtn.setStyleSheet("background-color: rgb(186, 186, 186);\n"
                                   "background-image: url(100.jpg);\n"
                                   "background-image: url(100.jpg);")
        self.quitBtn.setFlat(True)
        self.quitBtn.setObjectName("quitBtn")
        # 表情
        self.biaoqingBtn = QtWidgets.QPushButton(Form)
        self.biaoqingBtn.setGeometry(QtCore.QRect(30, 230, 31, 27))
        self.biaoqingBtn.setStyleSheet(
            "background-image: url(beijing.jpg);")
        self.biaoqingBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("p=0.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.biaoqingBtn.setIcon(icon2)
        self.biaoqingBtn.setFlat(True)
        self.biaoqingBtn.setObjectName("biaoqingBtn")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 200, 302, 32))#设置表格大小
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)#设置表格不可编辑
        self.tableWidget.setShowGrid(False)#隐藏表格网格线
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)#设置表格列数
        self.tableWidget.setColumnWidth(3,300)
        self.tableWidget.setRowHeight(1,200)
        self.tableWidget.setRowCount(1)#设置表格行数
        self.tableWidget.horizontalHeader().setVisible(False)#隐藏表格头
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.hide()#默认隐藏表情窗口
        self.value = 0
        self.biaoqingBtn.clicked.connect(self.show_hide)#自定义函数通过value值控制表情窗口的显示
        # 天气
        self.skyLabel = QtWidgets.QLabel(Form)
        self.skyLabel.setGeometry(QtCore.QRect(25, 366, 291, 61))
        self.skyLabel.setText("")
        self.skyLabel.setObjectName("skyLabel")
        # 列表框
        self.listwidget = QtWidgets.QListWidget(Form)
        self.listwidget.setGeometry(QtCore.QRect(450, 50, 211, 311))
        self.listwidget.setStyleSheet("background-color: rgb(213, 230, 255);")
        self.listwidget.setObjectName("listwidget")
        # 在线人数标签
        self.on_lineNlabel = QtWidgets.QLabel(Form)
        self.on_lineNlabel.setGeometry(QtCore.QRect(460, 360, 121, 21))
        self.on_lineNlabel.setObjectName("on_lineNlabel")
        # 在线人数按钮
        self.on_lineBtn = QtWidgets.QPushButton(Form)
        self.on_lineBtn.setGeometry(QtCore.QRect(450, 20, 211, 30))
        self.on_lineBtn.setStyleSheet("background-color: rgb(213, 230, 255);")
        self.on_lineBtn.setFlat(False)
        self.on_lineBtn.setObjectName("on_lineBtn")
        self.textEdit.raise_()
        self.formLayoutWidget.raise_()
        self.textBrowser.raise_()
        self.luyinBtn.raise_()
        self.tonghuaBtn.raise_()
        self.jiluBtn.raise_()
        self.quitBtn.raise_()
        self.biaoqingBtn.raise_()
        self.sendBtn.raise_()
        self.skyLabel.raise_()
        self.listwidget.raise_()
        self.on_lineNlabel.raise_()

        self.retranslateUi(Form)
        self.quitBtn.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "群聊"))
        self.luyinBtn.setText(_translate("Form", "语音消息"))
        self.tonghuaBtn.setText(_translate("Form", "语音通话"))
        self.sendBtn.setText(_translate("Form", "发送"))
        self.jiluBtn.setText(_translate("Form", "聊天记录"))
        self.quitBtn.setText(_translate("Form", "退出"))
        self.on_lineNlabel.setText(_translate("Form",
                                              "<html><head/><body><p><span style=\" \
        font-weight:600; font-style:italic; color:#dc4900;\">在线人数：</span></p></body></html>"))
        self.on_lineBtn.setText(_translate("Form", "在线用户"))
        self.skyLabel.setText(_translate("Form", now(nowtq_status)))
        QApplication.processEvents()
        time.sleep(0.1)

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.biaoqingBtn.setText(_translate("Form", "biaoqingBtn"))
        Item1 = QTableWidgetItem(QIcon("/home/tarena/my_first_project/chatroom/______/1.png"),"1")#通过Qicon插入
        self.tableWidget.setItem(0,0,Item1)
        Item2 = QTableWidgetItem(QIcon("/home/tarena/my_first_project/chatroom/______/2.png"),"2")
        self.tableWidget.setItem(0,1,Item2)
        Item3 = QTableWidgetItem(QIcon("/home/tarena/my_first_project/chatroom/______/3.png"),"3")
        self.tableWidget.setItem(0,2,Item3)
        item = QTableWidgetItem()
        print(item.text())

    def show_hide(self):#控制窗口隐藏信号函数
        print("显示表情")
        if self.value == 0:
            self.tableWidget.show()
            self.value += 1
        else:
            self.tableWidget.hide()
            self.value = 0


class MyMainWindow(Ui_Form1):
    # def __init__(self, s, parent=None):
    #     super(MyMainWindow,self).__init__(parent)
    def __init__(self, s, ADDR3):
        self.s = s
        self.ADDR3 = ADDR3
        print("欢迎来到群组聊天室")
        self.s.send(b'OK all')
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.num_L = []
        self.n_L = []
        self.msg = ''
        self.th = myThread(self.s)
        self.th.pressed.connect(self.display)
        self.th.answer.connect(self.message_box)
        self.th.jilu.connect(self.show_jilu)
        self.th.start()
        self.sendBtn.clicked.connect(self.chat)
        self.quitBtn.clicked.connect(self.close_window)
        self.tonghuaBtn.clicked.connect(self.yuyintonghua)
        self.on_lineBtn.clicked.connect(self.show_friend)
        self.tableWidget.itemDoubleClicked.connect(self.send_img_textbrowser)
        self.jiluBtn.clicked.connect(self.xiaoxi_jilu)

    def show_jilu(self, text):
        if text == '#over':
            self.msg = self.msg.replace('#jilu#','')
            self.xiaoxijilu = Xiaoxi_jilu(self.msg)
            self.xiaoxijilu.show()
            self.msg = ''
        else:
            self.msg += text + '\n'


    def xiaoxi_jilu(self):
        self.s.send(b'##xiaoxijilu##')   

    def send_img_textbrowser(self):
        item = self.tableWidget.selectedItems()[0]#通过select获取单元格文本信息
        print(item.text())
        if item == 0:
            print('图片未选中/图片出错')
        else:
            img = "<img src = '表情/" + item.text() + ".png' width='50' height='50'/>"#将表情文件名插入，由于textbrowser是ＨＴＭＬ格式，所以用＜img＞做插入
            self.num = item.text()
            self.num_L.append(self.num)
            self.textEdit.append(img)
            # self.s.send(text)
            # "<p style='color: blue'>" + "[" + self.name + "]" + time + "</p>" + 

    # 语音通话
    def yuyintonghua(self):
        print("开启语音通话通话功能")
        # self.s.send(b'##audiochat##')
        # time.sleep(1)
        # self.au_c = Audio_Client(self.ADDR3)

    def message_box(self, msg):
        if msg == "不能添加自己为好友":
            QMessageBox.information(self, 'Information', '不能添加自己为好友')
            # self.close()
        elif msg == "好友已存在":
            QMessageBox.information(self, 'Information', '好友已存在')
            # self.close()
        else:
            QMessageBox.information(self, 'Information', '添加好友成功')
            # self.close()

    def show_friend(self):
        self.s.send(b'##friendlist##')
        # f_info = self.s.recv(1024)
        # print(f_info, "-----show_list----")
        # friend_l = re.split(r'\W', f_info.decode())
        # #friend_l.pop(0)
        # #friend_l.pop(-1)
        # print(friend_l)
        # if friend_l:
        #     self.listwidget.addItem(friend_l[0])
        #     QApplication.processEvents()
        #     time.sleep(0.1)
        # self.listwidget.itemClicked.connect('<Button-3>',self.addfriend)

    # def addfriend(self):

    def close_window(self):
        self.close()
        # self.th.finished()
        # self.s.send(b'exit')
        # print('退出群组聊天室')

    def closeEvent(self, event):
        self.s.send(b'#exit#')
        print('退出群组聊天室')

    def chat(self):
        data = self.textEdit.toPlainText().encode()
        # print(data)
        self.textEdit.clear()
        # print('---------------------')
        # print(data)
        # print('---------------------')
        if data == 'exit':
            self.s.send(b'exit')
        else:
            for i in range(len(self.num_L)):
                if b'\xef\xbf\xbc' in data:
                    redata = b'&&img' + self.num_L[i].encode() + b'&&'
                    data = data.replace(b'\xef\xbf\xbc',redata,1)
            self.num_L = []
            self.s.send(data)

    def display(self, text):
        # (self.th.message).decode('utf-8')
        if text[:14] == '##friendlist##':
            f_info = text[14:]
            print(f_info, "-----show_list----")
            friend_l = re.split(r'\W', f_info)
            print(friend_l)
            friend_l.pop(-1)
            self.listwidget.clear()
            for name in friend_l:
                self.listwidget.addItem(name)
            QApplication.processEvents()
            time.sleep(0.1)
            self.listwidget.setContextMenuPolicy(3)
            self.listwidget.customContextMenuRequested[QtCore.QPoint].connect(
                self.rightMenuShow)
            # self.listwidget.setContextMenuPolicy(Qt.CustomContextMenu)
            # self.listwidget.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)
        else:
            paragraph = re.split(r'\#\&\&\#', text)
            for line in paragraph:
                # print('------------------')
                # print(line)
                # print('-----------------')
                if line:
                    if '&&img' in line:
                        L = re.findall(r'&&img\w&&',line)
                        for l in range(len(L)):
                            self.chnum = L[l][5]
                            self.n_L.append(self.chnum)
                        for i in self.n_L:
                            su = '&&img'+i+'&&'
                            img = "<img src = '表情/" + i + ".png' width='50' height='50'/>"
                            msg = '<p>'+img+'</p>'
                            line = line.replace(su,msg,1)
                        self.n_L = []
                        print(line)
                        line = time.ctime() + ' ' + line
                        self.textBrowser.append(line)
                    else:
                        line = time.ctime()[11:19] + ' ' + line
                        self.textBrowser.append(line)

    def add_Item(self):
        print('-----添加------')
        name = self.listwidget.currentItem().text()
        print(name)
        data = b'##add_my_friend##' + name.encode()
        self.s.send(data)

    # 创建右键菜单
    def rightMenuShow(self, point):
        print('--point:--', point)
        rightMenu = QMenu(self.listwidget)
        addAction = QAction(
            u"添加好友", self, triggered=self.add_Item)       # 也可以指定自定义对象事件
        rightMenu.addAction(addAction)
        rightMenu.exec_(QtGui.QCursor.pos())

class Xiaoxi_jilu(QWidget):
    def __init__(self,msg):
        self.message = msg
        super().__init__()
        self.setWindowTitle('历史消息')
        self.resize(500,450)
        self.move(200,300)
        self.closebutton = QPushButton('关闭')
        self.closebutton.resize(60,40)
        self.closebutton.move(420,400)

        self.text_browser = QTextBrowser(self)
        self.text_browser.resize(450,380)
        self.text_browser.move(20,20)

        self.closebutton.clicked.connect(self.close)
        self.show_text_borwser()
    def show_text_borwser(self):
        if self.message:
            self.text_browser.append(self.message)


                    
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import *

    class MyMainWindow(QMainWindow, Ui_Form):
        def __init__(self, parent=None):
            super(MyMainWindow, self).__init__(parent)
            self.setupUi(self)
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
    print(os.path.dirname(__file__))



    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    #     self.pushButton.setText(_translate("MainWindow", "PushButton"))
    #     Item1 = QTableWidgetItem(QIcon("/home/tarena/my_first_project/chatroom/表情/1.png"),"1")#通过Qicon插入
    #     self.tableWidget.setItem(0,0,Item1)
    #     Item2 = QTableWidgetItem(QIcon("/home/tarena/my_first_project/chatroom/表情/2.png"),"2")
    #     self.tableWidget.setItem(0,1,Item2)
    #     Item3 = QTableWidgetItem(QIcon("/home/tarena/my_first_project/chatroom/表情/3.png"),"3")
    #     self.tableWidget.setItem(0,2,Item3)
    #     item = QTableWidgetItem()
    #     print(item.text())





    # def show_hide(self):#控制窗口隐藏信号函数
    #     if self.value == 0:
    #         self.tableWidget.show()
    #         self.value += 1
    #     else:
    #         self.tableWidget.hide()
    #         self.value = 0

    # # def getTableitems(self):#对选中图片做回应
    # #     return self.QTableWidgetItem()

    # def getTableitems(self):
    #     return self.getTableitems()

    # def send_img_textbrowser(self):
    #     item = self.tableWidget.selectedItems()[0]#通过select获取单元格文本信息
    #     print(item.text())
    #     if item == 0:
    #         print('图片未选中/图片出错')
    #     else:
    #         img = "<img src = '/home/tarena/my_first_project/chatroom/表情/" + item.text() + ".png' width='50' height='50'/>"#将表情文件名插入，由于textbrowser是ＨＴＭＬ格式，所以用＜img＞做插入
    #         self.textBrowser.append(img)

