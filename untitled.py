# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from gl_pazzle_logic import *

class Unt(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 327)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openGLWidget = PazzleGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(10, 10, 401, 281))
        self.openGLWidget.setObjectName("openGLWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 18))
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


class mw(QtWidgets.QMainWindow):
    def __init__(self):
        super(mw, self).__init__()
        self.ui = Unt()
        self.ui.setupUi(self)


    def resizeEvent(self, event):
        #print(event)
        x=self.size().width()
        y=self.size().height()

        self.ui.openGLWidget.resize(x-50,y-50)
        #self.ui.lineEdit.setText(str(self.ui.openGLWidget.paintingPolies))