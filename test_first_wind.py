# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_first_wind.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from gl_in_widget_logic import *
from gl_model_creator import *
from untitled import *
import work_with_ui as wwu
import  subprocess
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget = GLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(189, 9, 361, 311))
        self.openGLWidget.setObjectName("openGLWidget")
        self.openGLWidget.setMouseTracking(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 100, 171, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 190, 171, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 240, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 290, 171, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 171, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 171, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.comboBox.addItems(self.bla())
        self.comboBox_2.addItems(self.bla2())

        self.comboBox.currentIndexChanged.connect(self.openGLWidget.setNumOfAng)
        self.comboBox_2.currentIndexChanged.connect(self.pr)

        self.pushButton.clicked.connect(self.new_m)
        self.pushButton_2.clicked.connect(self.zxc)
        self.pushButton_3.clicked.connect(self.run_model)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Новая модель"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить слой"))
        self.pushButton_3.setText(_translate("MainWindow", "Показать модель"))
        self.label.setText(_translate("MainWindow", "Выбрать модель"))
        self.label_2.setText(_translate("MainWindow", "Выбрать слой"))

    def bla(self):
        a=[]
        for i in range(3,6):
            a+=[str(i+i//5)]
        return a

    def bla2(self):
        a = []
        i=self.openGLWidget.number_of_layers
        a += [str(i)]
        return a

    def pr(self,a):
        print(a)
        self.openGLWidget.work_layer=a
        self.openGLWidget.updateImage()

    def asd(self,a):
        print(a)
        self.openGLWidget.mazs.releas_text()

    def zxc(self,a):
        print(a)
        self.openGLWidget.mazs.add_layer()
        print(0)
        self.openGLWidget.work_layer += 1
        print(self.openGLWidget.work_layer)
        self.openGLWidget.updateImage()
        print(2)
        self.openGLWidget.number_of_layers+=1
        # self.comboBox_2.removeItem(1)
        self.comboBox_2.addItems(self.bla2())
        self.comboBox_2.setCurrentIndex(self.openGLWidget.number_of_layers-1)
        print(3)


    def new_m(self,a):
        print(a)
        # self.comboBox_2.removeItem(1)
        for i in range(self.openGLWidget.number_of_layers):
            self.comboBox_2.removeItem(1)
        self.openGLWidget.new_maza()


    def run_model(self,a):
        print(a)

        # subprocess.Popen(['python3', 'work_with_ui.py', 'argzzz1', 'argzzz2'])
        try:
            self.openGLWidget.mazs.releas_text()
            p=subprocess.Popen('python work_with_ui.py')
            print(p)
            # p=subprocess.Popen(['wwu.main()'])
            # os.system('work_with_ui.py')
            # wwu.main()
        except:
            print("error")


import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def resizeEvent(self, event):
        x=self.size().width()
        y=self.size().height()

        self.ui.openGLWidget.resize(x-230,y-50)




app = QtWidgets.QApplication([])
application = mywindow()
application.resize(1000,800)
application.show()
#application.ui.lineEdit.setText(str(application.ui.openGLWidget.textString))

sys.exit(app.exec())