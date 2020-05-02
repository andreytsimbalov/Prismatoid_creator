import numpy as np
import math as m
import random

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class mazaika:
    # verticies=[]
    # edges=[]
    # polygons=[]
    kletki=[]
    layers=[]

    def __init__(self,number_angles):
        self.num_angles = number_angles
        if (number_angles==4 or number_angles==3 or number_angles==6):
            self.mazaika_cr(number_angles)
        else: self.first_creation(number_angles)
        # self.first_creation(number_angles)

    def first_creation(self,number):
        a=kletka(0.7,[0,0],number,1.57/3)
        self.kletki=[a]

    def add_kletk(self,number):
        a=kletka(0.7,[0,0],number,1.57/2)
        self.kletki+=[a]

    def mazaika_cr(self,number):
        self.kletki=[]
        radius=0.5
        if number==4:
            #print('qew',4)
            smesh = radius / (2 ** 0.5)
            for i in range(-2,3):
                for j in range(-2,3):
                    a = kletka(radius,[smesh*i*2, smesh*j*2], number, 1.57 / 2)
                    self.kletki += [a]
        elif number==3:
            #print('qew',3)
            smesh = 1.5*radius/(3**0.5)
            for i in range(-1,2):
                for j in range(-2,2):
                    a = kletka(radius, [smesh * i*2, radius*1.5*j+radius*0.5+radius*0.5*(j%2)], number, j%2*3.14)#+radius*0.5*j%2
                    self.kletki += [a]
            for i in range(-2,2):
                for j in range(-2,2):
                    a = kletka(radius, [smesh * i*2+smesh*1, radius*1.5*j+radius*0.5+radius*0.5*((j+1)%2)], number, (j+1)%2*3.14)
                    self.kletki += [a]
        elif number==6:
            smesh =1/ 2 * radius * (3 ** 0.5)
            for i in range(-1,1):
                for j in range(-1,2):
                    a = kletka(radius, [radius * i * 3+radius*1.5 , smesh*2*j], number, 1.57/3)
                    self.kletki += [a]
            for i in range(-1,2):
                for j in range(-2,2):
                    a = kletka(radius, [radius * i * 3, smesh*2*j+smesh], number, 1.57/3)
                    self.kletki += [a]




    def makeLayer(self,number_of_sloi):
        reflectance = (random.random(), random.random(), random.random(), 1)
        #list=0
        list = glGenLists(1)
        glNewList(list, GL_COMPILE)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, reflectance)

        # glBegin(GL_LINE_LOOP)
        c=0
        m=0
        for i in self.kletki:
            glBegin(GL_LINE_LOOP)
            m+=1
            i.layer_correct()
            sl = i.layers[number_of_sloi]
            for j in range(len(sl)):
                c+=1
                glVertex3f(sl[j][0], sl[j][1], 0)
            glEnd()
        # glEnd()
        #print(c,m)

        glEndList()

        self.layers=list
        #print(self.layers)
        #return list

    def draw(self):
        glPushMatrix()
        glCallList(self.layers)
        glPopMatrix()



class kletka:
    layers = []

    def __init__(self,radius,center,number_angles,rotate):
        self.num_angles = number_angles
        self.creation(radius,center,number_angles,rotate)

    def creation(self,radius,center, number,rotate):
        fc = []
        for i in range(number):
            ans = []
            phi = i * m.pi * 2 / number + rotate # повороты в радианах
            ans += [center[0] + radius * m.sin(phi)]
            ans += [center[1] + radius * m.cos(phi)]
            #ans += [center[2]]
            fc += [ans]
        # print(fc)
        # self.verticies=fc
        self.layers=[fc]

    def layer_correct(self):
        if len(self.layers)==1:
            self.layers+=self.layers
        #zCoord=np.arange(-1,1+0.001,2/(len(self.sloi)-1))
        #fc=[]
        #print(self.sloi)
        # return self.sloi


def drawPoly(poly):

    glPushMatrix()
    #glRotated(angle, 0.0, 0.0, 1.0)
    glCallList(poly)
    #print("123 ",poly)
    glPopMatrix()



if __name__== "__main__":
    pass