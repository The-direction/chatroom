# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_1v1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from recvThread import myThread
from PyQt5.QtWidgets import *
from weather import *
import time

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 424)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("#Form{\n"
"border-image: url(haizeiwang3333_看图王.jpg);}\n"
"")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 21, 411, 201))
        self.textBrowser.setStyleSheet("\n"
"background-color: rgb(221, 246, 255);")
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
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
        icon.addPixmap(QtGui.QPixmap("xiaoxi.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.luyinBtn.setIcon(icon)
        self.luyinBtn.setFlat(True)
        self.luyinBtn.setObjectName("luyinBtn")
        self.tonghuaBtn = QtWidgets.QPushButton(Form)
        self.tonghuaBtn.setGeometry(QtCore.QRect(180, 230, 91, 27))
        self.tonghuaBtn.setStyleSheet("background-color: rgb(245, 255, 194);\n"
"background-image: url(999.jpg);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("tonghu.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.biaoqingBtn = QtWidgets.QPushButton(Form)
        self.biaoqingBtn.setGeometry(QtCore.QRect(30, 230, 31, 27))
        self.biaoqingBtn.setStyleSheet("background-image: url(beijing.jpg);")
        self.biaoqingBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("p=0.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.biaoqingBtn.setIcon(icon2)
        self.biaoqingBtn.setFlat(True)
        self.biaoqingBtn.setObjectName("biaoqingBtn")
        self.skyLabel = QtWidgets.QLabel(Form)
        self.skyLabel.setGeometry(QtCore.QRect(25, 366, 291, 51))
        self.skyLabel.setText("")
        self.skyLabel.setObjectName("skyLabel")
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

        self.retranslateUi(Form)
        self.quitBtn.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "单人聊天"))
        self.luyinBtn.setText(_translate("Form", "语音消息"))
        self.tonghuaBtn.setText(_translate("Form", "语音通话"))
        self.sendBtn.setText(_translate("Form", "发送"))
        self.jiluBtn.setText(_translate("Form", "聊天记录"))
        self.quitBtn.setText(_translate("Form", "退出"))
        self.skyLabel.setText(_translate("Form",now(nowtq_status)))
        QApplication.processEvents()
        time.sleep(0.1)
class Mychatwindow(QMainWindow,Ui_Form):
    def __init__(self, s, obj, parent=None):
        self.s = s
        self.obj = obj
        print("欢迎来到与", obj, "的聊天室")
        # self.s.send(b'OK all')
        super().__init__()
        self.setupUi(self)
        self.th = myThread(self.s)
        self.th.pressed.connect(self.display)
        self.th.start()
        self.sendBtn.clicked.connect(self.chat)
        self.sendBtn.setEnabled(False)
        self.quitBtn.clicked.connect(self.close_window)
        self.setWindowTitle("和%s聊天中．．．"%self.obj)
        self.textEdit.textChanged.connect(self.check_button)
    
    def check_button(self):
        if self.textEdit.toPlainText():
            self.sendBtn.setEnabled(True)
        else:
            self.sendBtn.setEnabled(False)    
    def close_window(self):
        self.close()
        # self.th.finished()
        # self.s.send(b'exit')
        # print('退出群组聊天室')

    def closeEvent(self, event):
        self.s.send(b"#exit#")
        print('退出单人聊天室')

    def chat(self):
        data = self.textEdit.toPlainText()
        self.textEdit.clear()
        print('----',data,'--self.chat()----')
        if data == 'exit':
            self.s.send(b'exit')
        else:
            text = self.obj + ':' + data
            self.s.send(text.encode())
            self.textBrowser.append("self : "+data)

    def display(self, text):
        # (self.th.message).decode('utf-8')
        print('----',text,'--self.display()----')
        self.textBrowser.append(text)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import *

    class MyMainWindow(QMainWindow,Ui_Form):
        def __init__(self,parent=None):
            super(MyMainWindow,self).__init__(parent)
            self.setupUi(self)
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())