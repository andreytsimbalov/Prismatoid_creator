# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from gl_in_widget_logic import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 491, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #self.openGLWidget = QtWidgets.QOpenGLWidget(self.verticalLayoutWidget)
        self.openGLWidget = GLWidget(self.verticalLayoutWidget)
        self.openGLWidget.setObjectName("openGLWidget")
        self.horizontalLayout_3.addWidget(self.openGLWidget)

        self.verticalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setMinimum(-180)
        self.verticalSlider.setMaximum(180)
        self.verticalSlider.setValue(0)

        self.verticalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_2.setMinimum(-180)
        self.verticalSlider_2.setMaximum(180)
        self.verticalSlider_2.setValue(0)

        self.horizontalLayout_3.addWidget(self.verticalSlider_2)
        self.verticalSlider_3 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalSlider_3.setMinimum(-180)
        self.verticalSlider_3.setMaximum(180)
        self.verticalSlider_3.setValue(0)

        self.horizontalLayout_3.addWidget(self.verticalSlider_3)
        self.horizontalLayout_3.addWidget(self.verticalSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.verticalSlider.valueChanged.connect(self.openGLWidget.setXRotation)
        self.verticalSlider_2.valueChanged.connect(self.openGLWidget.setYRotation)
        self.verticalSlider_3.valueChanged.connect(self.openGLWidget.setZRotation)

        self.openGLWidget.xRotationChanged.connect(self.verticalSlider.setValue)
        self.openGLWidget.yRotationChanged.connect(self.verticalSlider_2.setValue)
        self.openGLWidget.zRotationChanged.connect(self.verticalSlider_3.setValue)


        self.pushButton_2.clicked.connect(self.openGLWidget.changeFigeru)
        self.pushButton.clicked.connect(self.openGLWidget.setPaintingPolies)
        #self.lineEdit.setText(str(self.openGLWidget.paintingPolies))
        #self.lineEdit.textChanged.connect(self.printText)
        self.lineEdit.textChanged.connect(self.openGLWidget.setTextString)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Вывести объекты"))
        self.pushButton_2.setText(_translate("MainWindow", "Сменить цвет"))

    def printText(self,a):
        print(type(a))
        print(a)
