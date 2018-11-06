# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_qun1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 419)
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
        self.skyLabel.setGeometry(QtCore.QRect(10, 370, 291, 41))
        self.skyLabel.setText("")
        self.skyLabel.setObjectName("skyLabel")
        self.on_lineNlabel = QtWidgets.QLabel(Form)
        self.on_lineNlabel.setGeometry(QtCore.QRect(460, 360, 121, 21))
        self.on_lineNlabel.setObjectName("on_lineNlabel")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(450, 50, 221, 311))
        self.listView.setStyleSheet("background-color: rgb(213, 230, 255);")
        self.listView.setObjectName("listView")
        self.on_lineBtn = QtWidgets.QPushButton(Form)
        self.on_lineBtn.setGeometry(QtCore.QRect(450, 20, 221, 31))
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
        self.on_lineNlabel.raise_()
        self.listView.raise_()
        self.on_lineBtn.raise_()

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
        self.on_lineNlabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; color:#dc4900;\">在线人数：</span></p></body></html>"))
        self.on_lineBtn.setText(_translate("Form", "在线用户"))

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
