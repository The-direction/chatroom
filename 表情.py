# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHBoxLayout, QApplication, QWidget, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QIcon
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)  # 显示窗口大小
        self.textEdit = QTextEdit
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(25, 360, 491, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 540, 93, 28))
        self.pushButton.setObjectName("表情")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 302, 32))  # 设置表格大小
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)  # 设置表格不可编辑
        self.tableWidget.setShowGrid(False)  # 隐藏表格网格线
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)  # 设置表格列数
        self.tableWidget.setColumnWidth(3, 300)
        self.tableWidget.setRowHeight(1, 200)
        self.tableWidget.setRowCount(1)  # 设置表格行数
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏表格头
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.hide()  # 默认隐藏表情窗口
        self.value = 0
        self.pushButton.clicked.connect(
            self.show_hide)  # 自定义函数通过value值控制表情窗口的显示
        self.tableWidget.itemDoubleClicked.connect(self.send_img_textbrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        path = os.path.dirname(_file__)
        Item1 = QTableWidgetItem(
            QIcon("/home/tarena/my_first_project/chatroom/表情/1.png"), "1")  # 通过Qicon插入
        self.tableWidget.setItem(0, 0, Item1)
        Item2 = QTableWidgetItem(
            QIcon("/home/tarena/my_first_project/chatroom/表情/2.png"), "2")
        self.tableWidget.setItem(0, 1, Item2)
        Item3 = QTableWidgetItem(
            QIcon("/home/tarena/my_first_project/chatroom/表情/3.png"), "3")
        self.tableWidget.setItem(0, 2, Item3)
        item = QTableWidgetItem()
        print(item.text())

    def show_hide(self):  # 控制窗口隐藏信号函数
        if self.value == 0:
            self.tableWidget.show()
            self.value += 1
        else:
            self.tableWidget.hide()
            self.value = 0

    # def getTableitems(self):#对选中图片做回应
    #     return self.QTableWidgetItem()

    def getTableitems(self):
        return self.getTableitems()

    def send_img_textbrowser(self):
        item = self.tableWidget.selectedItems()[0]  # 通过select获取单元格文本信息
        print(item.text())
        if item == 0:
            print('图片未选中/图片出错')
        else:
            img = "<img src = '/home/tarena/my_first_project/chatroom/表情/" + item.text() + \
                ".png' width='50' height='50'/>"  # 将表情文件名插入，由于textbrowser是ＨＴＭＬ格式，所以用＜img＞做插入
            self.textBrowser.append(img)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    # from firstMainWin import *

    class MyMainWindow(QMainWindow, Ui_MainWindow):
        """docstring for MyMainWindow"""

        def __init__(self, parent=None):
            super(MyMainWindow, self).__init__(parent)
            self.setupUi(self)

    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
