# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import (QtCore, QtGui, QtWidgets)
import OpenGL.GL as gl
from OpenGL import GLU as glu
import test_1 as t1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 370)

        #self.glWidget = GLWidget()
        #mainLayout = QGridLayout(self)
        #mainLayout.setContentsMargins(0, 0, 0, 0)
        #mainLayout.addWidget(self.glWidget)
        #self.setWindowTitle("Hello GL")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 30, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 60, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        #self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget =GLWidget(self.centralwidget)
        #self.openGLWidget = GLWidget()
        self.openGLWidget.setGeometry(QtCore.QRect(10, 10, 281, 291))
        self.openGLWidget.setObjectName("openGLWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 22))
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
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))


class GLWidget(QtWidgets.QOpenGLWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def initializeGL(self):
        gl.glClearColor(0, 0, 0, 0)
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glEnable(gl.GL_COLOR_MATERIAL)
        gl.glEnable(gl.GL_LIGHTING)
        ambientLight = [0.2, 0.2, 0.2, 1.0]
        diffuseLight = [0.5, 0.5, 0.5, 1.0]
        lightPos = [100, 100, 100, 0]
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_AMBIENT, ambientLight)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, diffuseLight)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, lightPos)
        gl.glEnable(gl.GL_LIGHT0)
        gl.glColorMaterial(gl.GL_FRONT_AND_BACK, gl.GL_AMBIENT_AND_DIFFUSE)

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glColor3f(1.0, 1.0, 2.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPushMatrix()
        gl.glTranslatef(0, 0, 0)
        qobj = glu.gluNewQuadric()
        glu.gluQuadricOrientation(qobj, glu.GLU_OUTSIDE)
        t1.subfunc()#отрисовка выпуклой фигуры
        #glu.gluSphere(qobj, 0.67, 100, 100)
        gl.glPopMatrix()

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0: return
        gl.glViewport((width - side) // 2, (height - side) // 2, side, side)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glScale(height / width, 1.0, 1.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
