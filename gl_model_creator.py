from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from sub_func import *
import mazaika_fw_logic as mfl


class GLWidget(QtWidgets.QOpenGLWidget):

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.poly = 0
        self.model3d = []
        self.reflectance=[]
        self.sloi =0
        self.number_of_angles=3
        self.file = "models\model_1.txt"
        # "models\model_1.txt"
        # "models\model_2.txt"
        # "models\model_3.txt"
        self.mazs=0

    def initializeGL(self):
        lightPos = (5.0, 0, 10.0, 1.0) # новое освещение с отдалением 5 5 10 1

        glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)

        # print(1)
        # self.layers=[mfl.mazaika(4)]
        # #self.poly+=[self.qwe[0].makePoly(0)]
        #
        # # print(1)
        # self.layers[0].makeLayer(0)
        # print("poly", self.layers[0].layers)

        # self.number_of_angles=6
        self.changeFigeru()



        glEnable(GL_NORMALIZE)
        glClearColor(0.0, 0.0, 0.0, 1.0)



    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # нормальная отрисовка модели
        # glPushMatrix()
        # self.mazs.draw(len(self.mazs.layers)-1)
        # mfl.mazaika.draw(self.poly)

        self.mazs.draw()

        print("len",self.mazs.layers)
        # mfl.drawPoly(self.mazs.layers)
        self.mazs.draw()
        # for i in self.paintingPolies:
        #     drawPoly(self.model3d[i].poly)

        # glPopMatrix()


    def resizeGL(self, width, height):
        #print(width, height)
        side = min(width, height) # ресайз с изменением соотношения сторон
        if side < 0:return
        glViewport((width - side) // 2, (height - side) // 2, side, side)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslated(0.0, 0.0, -10.0)

    def changeFigeru(self):
        #self.mazs=0
        #print(self.mazs.layers)
        #self.mazs.layers=0

        #glDeleteLists(0,10)
        self.mazs = mfl.mazaika(self.number_of_angles)
        #print(len(self.mazs.kletki))
        self.mazs.makeLayer(0)
        #print('kar',self.mazs.layers)

        self.update()


    def setNumOfAng(self,n):
        self.number_of_angles = n+3
        print(self.number_of_angles)
        self.changeFigeru()


    def mousePressEvent(self, event):
        self.changeFigeru()
        self.lastPos = event.pos()
        print(event.pos())






if __name__== "__main__":
    pass