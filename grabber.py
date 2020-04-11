import sys
import math

from PyQt5.QtCore import pyqtSignal, QSize, Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QLabel,
        QMainWindow, QMessageBox, QOpenGLWidget, QScrollArea,
        QSizePolicy, QSlider, QWidget)

import OpenGL.GL as gl
import sub_func as sf
from gear_model import *

class GLWidget(QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.gear1 = 0
        self.gear2 = 0
        self.gear3 = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.gear1Rot = 0

        # timer = QTimer(self)
        # timer.timeout.connect(self.advanceGears)
        # timer.start(20)

    def setXRotation(self, angle):
        self.normalizeAngle(angle)

        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.update()

    def setYRotation(self, angle):
        self.normalizeAngle(angle)

        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.update()

    def setZRotation(self, angle):
        self.normalizeAngle(angle)

        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.update()

    def initializeGL(self):
        lightPos = (5.0, 5.0, 10.0, 1.0)
        reflectance1 = (0.8, 0.1, 0.0, 1.0)
        reflectance2 = (0.0, 0.8, 0.2, 1.0)
        reflectance3 = (0.2, 0.2, 1.0, 1.0)

        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, lightPos)
        gl.glEnable(gl.GL_LIGHTING)
        gl.glEnable(gl.GL_LIGHT0)
        gl.glEnable(gl.GL_DEPTH_TEST)

        #self.gear1 = self.makeGear(reflectance1, 1.0, 4.0, 1.0, 0.7, 20)

        self.gear1 = sf.makePoly(reflectance1,3)
        #self.gear2 = self.makeGear(reflectance2, 0.5, 2.0, 2.0, 0.7, 10)
        #self.gear3 = self.makeGear(reflectance3, 1.3, 2.0, 0.5, 0.7, 10)

        gl.glEnable(gl.GL_NORMALIZE)
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        gl.glPushMatrix()
        gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)

        #self.drawGear(self.gear1, -3.0, -2.0, 0.0, self.gear1Rot / 16.0)

        sf.drawPoly(self.gear1, 0, 0, 0.0, self.gear1Rot / 16.0)
        # self.drawGear(self.gear2, +3.1, -2.0, 0.0,
        #         -2.0 * (self.gear1Rot / 16.0) - 9.0)
        #
        # gl.glRotated(+90.0, 1.0, 0.0, 0.0)
        # self.drawGear(self.gear3, -3.1, -1.8, -2.2,
        #         +2.0 * (self.gear1Rot / 16.0) - 2.0)

        gl.glPopMatrix()

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        gl.glViewport((width - side) // 2, (height - side) // 2, side, side)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.glTranslated(0.0, 0.0, -40.0)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = event.pos()

    def advanceGears(self):
        self.gear1Rot += 2 * 16
        self.update()

    def xRotation(self):
        return self.xRot

    def yRotation(self):
        return self.yRot

    def zRotation(self):
        return self.zRot

    def normalizeAngle(self, angle):
        while (angle < 0):
            angle += 360 * 16

        while (angle > 360 * 16):
            angle -= 360 * 16


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.glWidget = GLWidget()
        self.pixmapLabel = QLabel()

        self.glWidgetArea = QScrollArea()
        self.glWidgetArea.setWidget(self.glWidget)
        self.glWidgetArea.setWidgetResizable(True)
        self.glWidgetArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setSizePolicy(QSizePolicy.Ignored,
                QSizePolicy.Ignored)
        self.glWidgetArea.setMinimumSize(50, 50)

        self.pixmapLabelArea = QScrollArea()
        self.pixmapLabelArea.setWidget(self.pixmapLabel)
        self.pixmapLabelArea.setSizePolicy(QSizePolicy.Ignored,
                QSizePolicy.Ignored)
        self.pixmapLabelArea.setMinimumSize(50, 50)

        xSlider = self.createSlider(self.glWidget.xRotationChanged,
                self.glWidget.setXRotation)
        ySlider = self.createSlider(self.glWidget.yRotationChanged,
                self.glWidget.setYRotation)
        zSlider = self.createSlider(self.glWidget.zRotationChanged,
                self.glWidget.setZRotation)

        self.createActions()
        self.createMenus()

        centralLayout = QGridLayout()
        centralLayout.addWidget(self.glWidgetArea, 0, 0)
        centralLayout.addWidget(self.pixmapLabelArea, 0, 1)
        centralLayout.addWidget(xSlider, 1, 0, 1, 2)
        centralLayout.addWidget(ySlider, 2, 0, 1, 2)
        centralLayout.addWidget(zSlider, 3, 0, 1, 2)
        centralWidget.setLayout(centralLayout)

        xSlider.setValue(15 * 16)
        ySlider.setValue(345 * 16)
        zSlider.setValue(0 * 16)

        self.setWindowTitle("Grabber")
        self.resize(1000, 600)

    def grabFrameBuffer(self):
        image = self.glWidget.grabFramebuffer()
        self.setPixmap(QPixmap.fromImage(image))

    def clearPixmap(self):
        self.setPixmap(QPixmap())

    def about(self):
        QMessageBox.about(self, "About Grabber",
                "The <b>Grabber</b> example demonstrates two approaches for "
                "rendering OpenGL into a Qt pixmap.")

    def createActions(self):
        self.grabFrameBufferAct = QAction("&Grab Frame Buffer", self,
                shortcut="Ctrl+G", triggered=self.grabFrameBuffer)

        self.clearPixmapAct = QAction("&Clear Pixmap", self,
                shortcut="Ctrl+L", triggered=self.clearPixmap)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=self.close)

        self.aboutAct = QAction("&About", self, triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
                triggered=QApplication.instance().aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.grabFrameBufferAct)
        self.fileMenu.addAction(self.clearPixmapAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def createSlider(self, changedSignal, setterSlot):
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QSlider.TicksRight)

        slider.valueChanged.connect(setterSlot)
        changedSignal.connect(slider.setValue)

        return slider

    def setPixmap(self, pixmap):
        self.pixmapLabel.setPixmap(pixmap)
        size = pixmap.size()

        if size - QSize(1, 0) == self.pixmapLabelArea.maximumViewportSize():
            size -= QSize(1, 0)

        self.pixmapLabel.resize(size)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())