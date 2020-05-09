from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from sub_func import *
import mazaika_fw_logic as mfl


class GLWidget(QtWidgets.QOpenGLWidget):

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        # self.poly = 0
        # self.model3d = []
        # self.reflectance=[]
        # self.sloi =0
        # self.file = "models\model_1.txt"
        # "models\model_1.txt"
        # "models\model_2.txt"
        # "models\model_3.txt"

        self.number_of_angles = 3
        self.number_of_layers = 1
        self.mazs = 0
        self.h = 0
        self.w = 0
        self.x = 0
        self.y = 0
        self.point_obj = []
        self.work_layer = 0
        self.obj_on_map = False

    def initializeGL(self):
        lightPos = (5.0, 0, 10.0, 1.0)  # новое освещение с отдалением 5 5 10 1

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

        # self.number_of_angles = 4
        # self.mazs = mfl.mazaika(self.number_of_angles)
        # self.updateImage()

        self.new_maza()

        glEnable(GL_NORMALIZE)
        glClearColor(0.2, 0.2, 0.2, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # нормальная отрисовка модели
        # glPushMatrix()
        # self.mazs.draw(len(self.mazs.layers)-1)
        # mfl.mazaika.draw(self.poly)
        glPushMatrix()
        point = [self.x, -self.y]
        # print("paintGL",1)
        if not (self.obj_on_map):
            point = self.mazs.bliz_point_search(self.x, -self.y, self.work_layer)

        if self.obj_on_map:
            point = self.mazs.line_and_point_search(self.x, -self.y, self.work_layer)
        # print("paintGL", 2)
        mfl.point_draw(point[0], point[1])
        # if self.point_obj!=[]:
        #     for i in self.point_obj:
        #         mfl.point_draw(i[0], i[1])
        self.mazs.draw()
        # print("paintGL", 3)
        glPopMatrix()
        # mfl.drawPoly(a)

        #print("len", self.mazs.layers)
        # mfl.drawPoly(self.mazs.layers)
        # self.mazs.draw()
        # for i in self.paintingPolies:
        #     drawPoly(self.model3d[i].poly)

        # glPopMatrix()

    def resizeGL(self, width, height):
        # print(width, height)
        self.w = width
        self.h = height
        side = min(width, height)  # ресайз с изменением соотношения сторон
        if side < 0: return
        glViewport((width - side) // 2, (height - side) // 2, side, side)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslated(0.0, 0.0, -10.0)

    def new_maza(self):
        glDeleteLists(0, 10)
        self.obj_on_map=False
        self.number_of_layers=1
        self.work_layer=0
        self.point_obj=[]
        self.mazs=0
        self.mazs = mfl.mazaika(self.number_of_angles)
        self.mazs.makeLayer(self.work_layer)
        self.update()

    def updateImage(self):
        glDeleteLists(0, 10)
        # self.mazs = mfl.mazaika(self.number_of_angles)
        self.mazs.makeLayer(self.work_layer)
        self.update()

    def setNumOfAng(self, n):
        self.number_of_angles = n + 3+n//2
        print(self.number_of_angles)
        self.updateImage()

    def mousePressEvent(self, event):
        self.updateImage()
        point = self.mazs.bliz_point_search(self.x, -self.y, self.work_layer)
        if self.obj_on_map:
            point = self.mazs.line_and_point_search(self.x, -self.y, self.work_layer)
            self.mazs.add_obj_vert(point[0], point[1], self.work_layer)
            if rast(point, self.point_obj) < 0.1:
                self.mazs.cleaning_activ_lines(self.work_layer)
        if (self.obj_on_map == False):
            self.obj_on_map = True
            print("pre")
            self.point_obj = point
            print("pre")
            self.mazs.add_obj(point[0], point[1], self.work_layer)
            print("pre")

        # if self.obj_on_map:
        #     point = self.mazs.line_and_point_search(self.x, -self.y, self.work_layer)
        #     self.mazs.add_obj_vert(point[0],point[1],self.work_layer)

        print("press")
        self.updateImage()

        # h=self.h
        # w=self.w
        #
        # self.y=(event.pos().y()-h/2)/h*4
        # self.x=(event.pos().x()-w/2)/w*4

    def mouseMoveEvent(self, event):
        self.updateImage()
        h = self.h
        w = self.w
        self.y = (event.pos().y() - h / 2) / h * 4
        self.x = (event.pos().x() - w / 2) / w * 4
        # print(self.x,self.y)
        # self.update()
        # self.paintGL()


if __name__ == "__main__":
    pass
