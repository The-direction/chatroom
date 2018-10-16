#!/usr/bin/env python3
# coding=utf-8

from demo import *
import sys

app = QApplication(sys.argv)
demo = Demo()
demo.show()

sys.exit(app.exec_())
