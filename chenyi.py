from weather import *
import time
import signal
from PyQt5 import *
from PyQt5.QtWidgets import *
import sys


class a(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,200,300,300)
        skyLabel = QLabel("",self)
        self.show()
        # itersignal.connect(self.skyLabel.setText)
        # self.run()
# class a:
#     pass
# def fun(sig, frame):
#     if sig == signal.SIGALRM:
#         continue
    # def run():
    #     itersignal = QtCore.pyqtSignal(str)
    #     while 1:
    #         print('--------------------')
    #         count = 0
    #         # signal.signal(signal.SIGALRM, fun)
    #         iter = now(nowtq_status)
    #         while count < 1000:
    #             data = next(iter)
    #             intersignal.emit(data)
    #             time.sleep(2)
    #             count += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aa = a()
    
    sys.exit(app.exec_())