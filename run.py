# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:40:52 2020

@author: ganglim
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main_windows.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked")
        
if __name__ == "__main__":
    app =QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()