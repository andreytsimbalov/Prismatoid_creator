from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
# import OpenGL.GL as gl
# from OpenGL import GLU as glu
# from OpenGL import GLUT as glut
from sub_func import *



class GLWidget(QtWidgets.QOpenGLWidget):

    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.poly = 0

        self.xRot = 0.0
        self.yRot = 0.0
        self.zRot = 0.0

        self.xRotAngle = 0.0
        self.yRotAngle = 0.0
        self.zRotAngle = 0.0
        self.gear1Rot = 0


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
    #
    # def setXRotation(self, angle):
    #     #self.normalizeAngle(angle)
    #
    #     if angle != self.xRotAngle:
    #
    #         self.xRot = angle - self.xRotAngle
    #         self.xRotAngle = angle
    #         print(angle)
    #         # self.xRotationChanged.emit(angle)
    #         # if self.xRot>0:
    #         #     self.xRot=4.0
    #         # else:
    #         #     self.xRot = -4.0
    #         self.update()
    #
    # def setYRotation(self, angle):
    #     #self.normalizeAngle(angle)
    #
    #     if angle != self.yRotAngle:
    #         self.yRot = angle - self.yRotAngle
    #         self.yRotAngle = angle
    #         self.update()
    #
    # def setZRotation(self, angle):
    #     #self.normalizeAngle(angle)
    #
    #     if angle != self.zRotAngle:
    #         self.zRot = angle - self.zRotAngle
    #         self.zRotAngle = angle
    #         self.update()


    def initializeGL(self):
        # glClearColor(0, 0, 0, 0)
        # glShadeModel(GL_SMOOTH)
        # glEnable(GL_COLOR_MATERIAL)
        # glEnable(GL_LIGHTING)
        # ambientLight = [0.2, 0.2, 0.2, 1.0]
        # diffuseLight = [0.5, 0.5, 0.5, 1.0]
        # lightPos = [100, 100, 100, 0]
        # glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight)
        # glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight)
        # glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
        # glEnable(GL_LIGHT0)
        # glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        lightPos = (5.0, 5.0, 10.0, 1.0)
        reflectance1 = (0.8, 0.1, 0.0, 1.0)
        reflectance2 = (0.0, 0.8, 0.2, 1.0)
        reflectance3 = (0.2, 0.2, 1.0, 1.0)

        glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)

        #subfunc()

        self.poly = makePoly(reflectance2,1)

        # self.gear1 = self.makeGear(reflectance1, 1.0, 4.0, 1.0, 0.7, 20)
        # self.gear2 = self.makeGear(reflectance2, 0.5, 2.0, 2.0, 0.7, 10)
        # self.gear3 = self.makeGear(reflectance3, 1.3, 2.0, 0.5, 0.7, 10)

        glEnable(GL_NORMALIZE)
        glClearColor(0.0, 0.0, 0.0, 1.0)



    def paintGL(self):
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # #glPushMatrix()
        # #glColor3f(1.0, 1.0, 2.0)
        # #glShadeModel(GL_FLAT)
        # glRotated(self.xRot , 1.0, 0.0, 0.0)
        # glRotated(self.yRot , 0.0, 1.0, 0.0)
        # glRotated(self.zRot , 0.0, 0.0, 1.0)
        # #glMatrixMode(GL_MODELVIEW)
        # glPushMatrix()
        #
        # gluPerspective(60.0, (1 / 1), 1, 142.0)
        # glTranslatef(0, 0, -5)
        # glRotatef(30, -1.0, 0, 0.2)
        # #subfunc()
        # # qobj = glu.gluNewQuadric()
        # # glu.gluQuadricOrientation(qobj, glu.GLU_OUTSIDE)
        # # glu.gluSphere(qobj, 0.67, 100, 100)
        # # отрисовка выпуклой фигуры
        # glPopMatrix()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotated(self.xRot , 1.0, 0.0, 0.0)
        glRotated(self.yRot , 0.0, 1.0, 0.0)
        glRotated(self.zRot , 0.0, 0.0, 1.0)
        #self.drawGear(self.gear1, -3.0, -2.0, 0.0, self.gear1Rot / 16.0)
        drawPoly(self.poly, -0, -0, -2, self.gear1Rot / 16.0)
        glPopMatrix()


    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0: return
        glViewport((width - side) // 2, (height - side) // 2, side, side)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glScale(height / width, 1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + dy/2)
            self.setYRotation(self.yRot + dx/2)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + dy/2)
            self.setZRotation(self.zRot + dx/2)

        self.lastPos = event.pos()

    def xRotation(self):
        return self.xRot

    def yRotation(self):
        return self.yRot

    def zRotation(self):
        return self.zRot

    def normalizeAngle(self, angle):
        while (angle < 0):
            angle += 360

        while (angle > 360):
            angle -= 360