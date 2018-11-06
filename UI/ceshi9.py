# import sys
# from PyQt5.QtWidgets import *
# from Ui_qun import *

# class MyMainWindow(QMainWindow,Ui_Form):
#     def __init__(self,parent=None):
#         super(MyMainWindow,self).__init__(parent)
#         self.setupUi(self)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWin = MyMainWindow()
#     myWin.show()
#     sys.exit(app.exec_())

import os
path = os.path.split(os.path.realpath(__file__))[0]
print(path)