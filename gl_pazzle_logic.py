from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from sub_func import *

class PazzleGLWidget(QtWidgets.QOpenGLWidget):

    # xRotationChanged = pyqtSignal(int)
    # yRotationChanged = pyqtSignal(int)
    # zRotationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(PazzleGLWidget, self).__init__(parent)

        self.poly = []
        self.model3d = []
        self.reflectance=[]
        self.sloi =0
        self.sloiNumber = 0
        self.file = "models\model_1.txt"
        # "models\model_2.txt"
        # "models\model_1.txt"



    def initializeGL(self):

        lightPos = (5.0, 0, 10.0, 1.0) # новое освещение с отдалением 5 5 10 1
        glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)

        # m=self.file_reader(self.file)
        # for i in range(len(m)):
        #     self.poly+=[self.makePoly(m[i],self.reflectance[i])]
        self.changeFigeru()

        glEnable(GL_NORMALIZE)
        glClearColor(0.0, 0.0, 0.0, 1.0)



    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # нормальная отрисовка модели
        glPushMatrix()
        for i in self.poly:
            self.drawPoly(i)
        glPopMatrix()


    def resizeGL(self, width, height):
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
        m = self.file_reader(self.file)
        for i in range(len(m)):
            self.poly += [self.makePoly(m[i], self.reflectance[i])]

    def file_reader(self,file):
        # s="models\coord.txt"
        f = open(file, 'r')
        a = []
        m = []
        for s in f:
            j = [s.split()]
            for i in j:
                for k in i:
                    a += [float(k)]
        #print(a)

        sloi = int(a[0])
        self.sloi = sloi
        modelCount = int(a[1])
        k = 2
        #self.reflectance=[]
        for i in range(modelCount):
            reflectance = (random.random(), random.random(), random.random(), 1.0)
            self.reflectance+=[reflectance]
            # reflectance=self.reflectance[i]
            start = k
            for i in range(sloi):
                k += int(a[k]) * 2 + 1
            vi = [] + a[start:k]
            #print(vi)
            modelPazzle=modelGenerator(vi, sloi)
            m+=[modelPazzle[self.sloiNumber]]
            #m += [model3D(modelGenerator(vi, sloi), reflectance)]
        #print(m)
        return m

    def makePoly(self, verticies, reflectance):
        #print(verticies, reflectance)
        list = glGenLists(1)
        glNewList(list, GL_COMPILE)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, reflectance)

        if len(verticies)>2:
            polygons = []
            for i in range(1,len(verticies)-1):
                polygons+=[[0,i,i+1]]
            #print(polygons)

            glBegin(GL_TRIANGLES)
            for i in polygons:
                #norm = normal([verticies[i[0]], verticies[i[1]], verticies[i[2]]])
                #glNormal3d(-norm[0], -norm[1], -norm[2])
                glNormal3d(0,0,1)
                for j in range(3):
                    k = i[j]
                    glVertex3d(verticies[k][0], verticies[k][1], 0)
            glEnd()

        glEndList()
        return list

    def drawPoly(self,poly):
        glPushMatrix()
        glCallList(poly)
        glPopMatrix()



