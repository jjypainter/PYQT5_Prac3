# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 01:26:20 2020

@author: ganglim
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import uic


form_class = uic.loadUiType("main_windows.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setUI()
        
    def setUI(self):
        self.setUI()


if __name__ == "__main__":
    print("hello world");
    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    app.exec_()