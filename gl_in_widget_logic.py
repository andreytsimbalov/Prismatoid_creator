from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from sub_func_1 import *


class GLWidget(QtWidgets.QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.poly = []
        self.model3d = []
        self.paintingPolies = []
        self.textString = ""
        self.reflectance = []
        self.sloi = 0
        self.file = "text.txt"
        # self.file ="models\model_1.txt"
        # self.file ="models\model_2.txt"
        # self.file ="models\model_3.txt"

        self.xRot = 0.0
        self.yRot = 0.0
        self.zRot = 0.0

        self.xRotAngle = 0.0
        self.yRotAngle = 0.0
        self.zRotAngle = 0.0
        self.gear1Rot = 0

    def setTextString(self, text):
        a = ''
        if type(text) == list:
            for i in text:
                a += str(i)
                a += ' '
            a = a[:len(a) - 1]
        elif type(text) == str:
            a = text
        self.textString = a

    def setPaintingPolies(self):
        text = self.textString
        a = []
        if type(text) == str:
            for i in text.split():
                a += [int(i)]
        self.paintingPolies = a
        print(a)
        self.update()

    def setXRotation(self, angle):  # повороты по осям
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
        # glClearColor(0, 0, 0, 0) # старое отвещение без отдаления
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

        lightPos = (5.0, 0, 10.0, 1.0)  # новое освещение с отдалением 5 5 10 1

        glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)

        self.changeFigeru()

        print("start")

        # self.model3d = file_reader("models\model_2.txt")
        # #"models\model_2.txt"
        # #"models\model_1.txt"
        # for i in self.model3d:
        #     self.poly += [i.poly]

        for i in range(len(self.model3d)):
            self.paintingPolies += [i]

        self.setTextString(self.paintingPolies)

        glEnable(GL_NORMALIZE)
        glClearColor(0.2, 0.2, 0.2, 1.0)

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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # нормальная отрисовка модели
        glPushMatrix()
        glRotated(self.xRot, 1.0, 0.0, 0.0)
        glRotated(self.yRot, 0.0, 1.0, 0.0)
        glRotated(self.zRot, 0.0, 0.0, 1.0)
        # self.drawGear(self.gear1, -3.0, -2.0, 0.0, self.gear1Rot / 16.0)

        for i in self.paintingPolies:
            # drawPoly(self.model3d[i].poly)
            drawPoly(self.poly[i])
            # print(self.model3d[i].poly)
        # print("poly: ",self.model3d[0].poly)

        # for i in self.model3d:
        #     i.drawPoly(self)

        # drawPoly(self.model3D, -0, -0, 0, self.gear1Rot / 16.0)
        glPopMatrix()

    def resizeGL(self, width, height):
        # side = min(width, height) #ресайз с обрезанием фигуры
        # if side < 0: return
        # glViewport((width - side) // 2, (height - side) // 2, side, side)
        # glMatrixMode(GL_PROJECTION)
        # glLoadIdentity()
        # glScale(height / width, 1.0, 1.0)
        # glMatrixMode(GL_MODELVIEW)

        # reflectance1 = (0.8, 0.1, 0.0, 1.0)
        # self.poly = makePoly(reflectance1, 0.5)  #

        side = min(width, height)  # ресайз с изменением соотношения сторон
        if side < 0: return
        glViewport((width - side) // 2, (height - side) // 2, side, side)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslated(0.0, 0.0, -10.0)

    def changeFigeru(self):
        # self.model3d = self.file_reader(self.file)
        self.file_reader(self.file)
        # self.edges_priority(4, 0)
        self.poly = []
        for i in self.model3d:
            # print("I",i)
            self.poly += [i.poly]
        # print(self.poly)

        self.update()

    def mousePressEvent(self, event):
        # self.changeFigeru()
        # self.file = "models\model_"+str(random.randint(1,3))+".txt"
        # self.changeFigeru()

        # self.edges_priority(4, 0)
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + dy / 2)
            self.setYRotation(self.yRot + dx / 2)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + dy / 2)
            self.setZRotation(self.zRot + dx / 2)

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

    def file_reader(self, file):
        # s="models\coord.txt"
        f = open(file, 'r')
        a = []
        m = []
        for s in f:
            j = [s.split()]
            for i in j:
                for k in i:
                    a += [float(k)]

        sloi = int(a[0])
        self.sloi = sloi
        modelCount = int(a[1])
        k = 2
        self.reflectance = []
        for i in range(modelCount):
            r = 1 - i / modelCount
            g = random.random()
            b = i / modelCount

            reflectance = (r, g, b, 1.0)
            # reflectance = (random.random(), random.random(), random.random(), 1.0)
            # print(reflectance)
            self.reflectance += [reflectance]
            start = k
            for j in range(sloi):
                k += int(a[k]) * 2 + 1
            # print("Aaa",a[start:k],len(a[start:k]))
            vi = [] + a[start:k]
            print("I", i)
            m += [model3D(modelGenerator(vi, sloi), reflectance)]
        # self.edges_priority(4, 0)
        self.model3d = m
        for i in range(1, len(self.model3d)):
            self.edges_priority(0, i)
        for i in self.model3d:
            i.makePoly()

    def edges_priority(self, i1, i2):
        # print(self.model3d[i1].verticies)
        # print(self.model3d[i1].edges)
        # print(self.model3d[i2].edges)
        for i in range(len(self.model3d[i1].edges)):
            n1 = [len(self.model3d[i1].verticies[i]), len(self.model3d[i1].verticies[i + 1])]
            n2 = [len(self.model3d[i2].verticies[i]), len(self.model3d[i2].verticies[i + 1])]
            v1 = self.model3d[i1].verticies[i] + self.model3d[i1].verticies[i + 1]
            v2 = self.model3d[i2].verticies[i] + self.model3d[i2].verticies[i + 1]
            # print(len(v1))
            # print(self.model3d[i2].verticies[i],self.model3d[i2].verticies[i+1])
            # print(len(v2))

            lj = []
            lk = []
            for j in range(n1[0]):
                for k in range(n2[0]):
                    if (rast(self.model3d[i1].verticies[i][j],
                             self.model3d[i2].verticies[i][(k - 1) % n2[0]]) < 0.01) and (
                            rast(self.model3d[i1].verticies[i][(j - 1) % n1[0]],
                                 self.model3d[i2].verticies[i][k]) < 0.01):
                        lj = [j, (j - 1) % n1[0]]
                        lk = [k, (k - 1) % n2[0]]

            lj1 = []
            lk1 = []
            for j in range(n1[1]):
                for k in range(n2[1]):
                    if (rast(self.model3d[i1].verticies[i + 1][j],
                             self.model3d[i2].verticies[i + 1][(k - 1) % n2[1]]) < 0.01) and (
                            rast(self.model3d[i1].verticies[i + 1][(j - 1) % n1[1]],
                                 self.model3d[i2].verticies[i + 1][k]) < 0.01):
                        lj1 = [n1[0] + j, n1[0] + (j - 1) % n1[1]]
                        lk1 = [n2[0] + k, n2[0] + (k - 1) % n2[1]]
            # print(lj, lk)
            # print(lj1, lk1)

            if (lj != []) and (lj1 != []):

                line = [lj[0], lj1[0]]
                if not (line in self.model3d[i1].edges[i]):
                    b = self.model3d[i1].edges[i] + [line]
                    c = b[n1[0] + n1[1]:]
                    c.sort()
                    self.model3d[i1].edges[i] = b[:n1[0] + n1[1]] + c
                    print("adddddddd")

                k=n1[0]+n1[1]
                # while k<len(self.model3d[i1].edges[i]):
                #     j=self.model3d[i1].edges[i][k]
                #     if j[0] == line[0]:
                #         e = j[1]
                #         if (e != (line[1] - 1 - n1[0]) % n1[1] + n1[0]) and (
                #                 e != (line[1] + 1 - n1[0]) % n1[1] + n1[0]) and (e != line[1]):
                #             self.model3d[i1].edges[i].remove(j)
                #             print("низ верх удалён")
                #             k-=1
                #     k+=1

                line = [lj[1], lj1[1]]
                if not (line in self.model3d[i1].edges[i]):
                    b = self.model3d[i1].edges[i] + [line]
                    c = b[n1[0] + n1[1]:]
                    c.sort()
                    self.model3d[i1].edges[i] = b[:n1[0] + n1[1]] + c
                    print("adddddddd")

                # k = n1[0] + n1[1]
                # while k < len(self.model3d[i1].edges[i]):
                #     j = self.model3d[i1].edges[i][k]
                #     if j[1] == line[1]:
                #         e = j[0]
                #         if (e != (line[0] - 1 ) % n1[0]) and (
                #                 e != (line[0] + 1 ) % n1[0] ) and (e != line[0]):
                #             self.model3d[i1].edges[i].remove(j)
                #             print("верх низ удалён")
                #             k -= 1
                #     k += 1


                zam = []
                for j in lj:
                    for k in lj1:
                        if not ([j, k] in self.model3d[i1].edges[i]):
                            zam = [j, k]
                            # print(zam)
                            # print("DO", self.model3d[i1].edges)
                if zam == []:
                    print("error zam")
                else:
                    zamam = []
                    for j in lj:
                        for k in lj1:
                            if j != zam[0]:
                                if k != zam[1]:
                                    zamam = [j, k]
                    for j in range(len(self.model3d[i1].edges[i])):
                        if self.model3d[i1].edges[i][j] == zamam:
                            self.model3d[i1].edges[i][j] = zam
                            b = self.model3d[i1].edges[i]
                            c = b[n1[0] + n1[1]:]
                            c.sort()
                            self.model3d[i1].edges[i] = b[:n1[0] + n1[1]] + c

                    print(i,self.model3d[i1].edges[i])
                    print(zam)
                    print(zamam)
        # print("POSLE", self.model3d[i1].edges)
