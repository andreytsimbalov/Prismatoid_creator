# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from gl_in_widget_logic import *
from untitled import *



class Ui_MainWindow(object):
    new_window = []

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
        self.verticalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setMinimum(-180)
        self.verticalSlider.setMaximum(180)
        self.verticalSlider.setValue(0)

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
        # self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
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

        # self.pushButton_2.clicked.connect(self.openGLWidget.changeFigeru)
        self.pushButton.clicked.connect(self.openGLWidget.setPaintingPolies)
        self.lineEdit.textChanged.connect(self.openGLWidget.setTextString)
        self.pushButton_3.clicked.connect(self.qwe)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Histology"))
        self.pushButton.setText(_translate("MainWindow", "Вывести объекты"))
        # self.pushButton_2.setText(_translate("MainWindow", "Изменить цвет"))
        self.pushButton_3.setText(_translate("MainWindow", "Показать пазлы"))

    def qwe(self):
        self.new_window=[]
        for i in range(self.openGLWidget.sloi):

            self.new_window += [mw()]
            self.new_window[i].ui.openGLWidget.file = self.openGLWidget.file
            self.new_window[i].ui.openGLWidget.sloiNumber=i
            self.new_window[i].ui.openGLWidget.reflectance = self.openGLWidget.reflectance
            self.new_window[i].resize(700, 700)
            self.new_window[i].setWindowTitle("Pazzle"+str(i+1))
            self.new_window[i].show()


