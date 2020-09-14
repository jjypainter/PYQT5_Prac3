# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:48:29 2020

@author: ganglim
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Rizon Icon')
        self.setWindowIcon(QIcon('rizon.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())