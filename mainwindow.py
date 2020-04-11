# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from gl_in_widget_logic import *
from grabber import GLWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(49, 29, 411, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.openGLWidget = QtWidgets.QOpenGLWidget(self.horizontalLayoutWidget)
        self.openGLWidget = GLWidget(self.horizontalLayoutWidget)
        self.openGLWidget.setObjectName("openGLWidget")
        self.horizontalLayout.addWidget(self.openGLWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)

        self.verticalSlider.setMinimum(-180)
        self.verticalSlider.setMaximum(180)
        self.verticalSlider.setValue(0)

        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_3.addWidget(self.verticalSlider)
        self.verticalSlider_2 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout_3.addWidget(self.verticalSlider_2)
        self.verticalSlider_3 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout_3.addWidget(self.verticalSlider_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.verticalSlider.valueChanged.connect(self.qwe)

        self.verticalSlider.valueChanged.connect(self.openGLWidget.setXRotation)
        self.verticalSlider_2.valueChanged.connect(self.openGLWidget.setYRotation)
        self.verticalSlider_3.valueChanged.connect(self.openGLWidget.setZRotation)


    def qwe(self, i):
        print(i)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))





# def specialkeys(key, x, y):
#     # Сообщаем о необходимости использовать глобального массива pointcolor
#     # Обработчики специальных клавиш
#     if key == glut.GLUT_KEY_UP:          # Клавиша вверх
#         gl.glRotatef(5, 1, 0, 0)       # Вращаем на 5 градусов по оси X
#     if key == glut.GLUT_KEY_DOWN:        # Клавиша вниз
#         gl.glRotatef(-5, 1, 0, 0)      # Вращаем на -5 градусов по оси X
#     if key == glut.GLUT_KEY_LEFT:        # Клавиша влево
#         gl.glRotatef(5, 0, 1, 0)       # Вращаем на 5 градусов по оси Y
#     if key == glut.GLUT_KEY_RIGHT:       # Клавиша вправо
#         gl.glRotatef(-5, 0, 1, 0)      # Вращаем на -5 градусов по оси Y