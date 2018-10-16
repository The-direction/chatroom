from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import signal
import os


class loginPage(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用户界面")
        self.setGeometry(900, 100, 270, 480)
        user_label = QLabel('  '*5+'>我的好友', self)
        user_label.setFont(QFont('黑体', 15))
        user_label.resize(290, 170)
        user_label.move(50, 10)
        user_label.setStyleSheet('QLabel{color:blank}')

        users_label = QLabel('  '*5+'>我的群聊', self)
        users_label.setFont(QFont('黑体', 15))
        users_label.resize(290, 170)
        users_label.move(50, 40)
        users_label.setStyleSheet('QLabel{color:blank}')

    def closeEvent(self, event):
        print('退出客户端')
        os.kill(os.getpid(),signal.SIGINT)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("bgpic2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
