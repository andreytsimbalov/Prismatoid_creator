import pygame
import math as m
import logging as l
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def prav_fig(r,c,n): # рисование правильных фигур
    fc=[]
    for i in range(n):
        ans=[]
        phi=i*m.pi*2/n
        ans+=[c[0]+r*m.sin(phi)]
        ans += [c[1] + r * m.cos(phi)]
        ans+=[c[2]]
        l.info(ans)# не работает
        fc+=[ans]
    return fc

def qwe(n): # построение правильной пирамиды
    a=[]
    for i in range(1,n+1):

        b=[0]
        b+=[i]
        a+=[b]

        b= [i]
        b+=[(i)%(n) +1]
        a += [b]
    return a


# verticies = (
#     (1, -1, -1),
#     (1, 1, -1),
#     (-1, 1, -1),
#     (-1, -1, -1),
#     (1, -1, 1),
#     (1, 1, 1),
#     (-1, -1, 1),
#     (-1, 1, 1)
#     )

# verticies = [
#     [0,0,radius],
#     [0,radius,0],
#     [radius,-radius,0],
#     [-radius,-radius,0],
# ]

# edges = (
#     (0,1),
#     (0,3),
#     (0,2),
#     (2,1),
#     (1, 3),
#     (2, 3),
#     )

# edges = (
#     (0,1),
#     (0,3),
#     (0,4),
#     (2,1),
#     (2,3),
#     (2,7),
#     (6,3),
#     (6,4),
#     (6,7),
#     (5,1),
#     (5,4),
#     (5,7)
#     )


def Figure():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 52.0)
    glTranslatef(0,0.0, -7)# расположение на дисплее

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1) # скорость и углы вращения можели
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Figure()
        pygame.display.flip()
        pygame.time.wait(10)

def rast(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

def poligonizer(v1,v2):
    fc=[]
    sdvig = len(v1)
    sdvig1=0

    for i in range(len(v1)):
        b= [i]
        b+=[(i+1)%(len(v1))]
        fc += [b]

    for i in range(len(v2)):
        b= [sdvig+i]
        b+=[sdvig+(i+1)%(len(v2))]
        fc += [b]


    if len(v2)>len(v1):
        a=v1
        v1=v2
        v2=a

        sdvig1 = len(v1)
        sdvig = 0


    for i in range(len(v1)):
        rasts=[]
        for j in range(len(v2)):
            rasts+=[[rast(v1[i],v2[j]),j]]
        rasts.sort()
        fc+=[[sdvig1+i,sdvig+rasts[0][1]]]
        fc += [[sdvig1+i, sdvig + rasts[1][1]]]

    for i in range(len(v2)):
        rasts=[]
        for j in range(len(v1)):
            rasts+=[[rast(v2[i],v1[j]),j]]
        rasts.sort()
        fc+=[[sdvig+i,sdvig1+rasts[0][1]]]
        fc += [[sdvig+i,sdvig1+rasts[1][1]]]


    return fc








radius=1
count_of_fertex=6

# verticies=[[0,0,1]]+prav_fig(1,[0,0,0],count_of_fertex)
# edges=qwe(count_of_fertex)

v1=prav_fig(1,[0,0,1],6) # правильный Н гранник
v2=prav_fig(1,[0,0,0],4) # правильный М гранник



verticies=v1+v2
edges=poligonizer(v1,v2)


main()

