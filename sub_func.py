from test_1 import *

# def subfunc():
#     v1 = prav_fig(0.5, [0, 0, 1], 3)  # + [[-2, 0, 1]]  # правильный Н гранник
#     v2 = prav_fig(1, [0, 0, 0], 7)  # правильный М гранник
#
#     #print(v1)
#
#     verticies = v1 + v2
#     edges = polygonizer_2(v1, v2)
#
#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             glVertex3fv(verticies[vertex])
#     glEnd()
#
#     # array_vert=[]
#     # for i in verticies:
#     #     for j in i:
#     #         array_vert+=[j]
#     # glEnableClientState(GL_VERTEX_ARRAY)
#     # glVertexPointer(3, GL_FLOAT, 0, array_vert)
#     # random.random()
#     # glColor3f(random.random()*2, random.random()*2, 0.0)
#     # glDrawArrays(GL_TRIANGLES, 0, 9)
#     # glDisableClientState(GL_VERTEX_ARRAY)
#
#     #glDrawElements()
#
#     # glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
#     # glBegin(GL_TRIANGLES)
#     # for i in range(9):#[rand.randint(8),rand.randint(8),rand.randint(8)]:
#     #     glColor3f(random.random() * 2, random.random() * 2, 0.0)
#     #     glVertex3fv(verticies[i])
#     # glEnd()
#
#     #glNormal3d(0.0, 0.0, -1)
#
#     glBegin(GL_TRIANGLES)
#     for i in range(1,10):#[rand.randint(8),rand.randint(8),rand.randint(8)]:
#         glColor3f(random.random() * 2, random.random() * 2, 0.0)
#         glVertex3d(verticies[i][0],verticies[i][1],verticies[i][2])
#     glEnd()


def makePoly(reflectance, mashtab):
    v1 = prav_fig(1*mashtab, [0, 0, 1*mashtab], 3)  # + [[-2, 0, 1]]  # правильный Н гранник
    v2 = prav_fig(1*mashtab, [0, 0, 0], 7)  # правильный М гранник


    verticies = v1 + v2
    edges = polygonizer_2(v1, v2)

    list = glGenLists(1)
    glNewList(list, GL_COMPILE)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE,reflectance)

    #glShadeModel(GL_FLAT)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)
    for i in range(1,10):#[rand.randint(8),rand.randint(8),rand.randint(8)]:
        glColor3f(random.random() * 2, random.random() * 2, 0.0)
        glVertex3d(verticies[i][0],verticies[i][1],verticies[i][2])
    glEnd()

    glEndList()

    return list







def drawPoly(poly, dx, dy, dz, angle):
    glPushMatrix()
    glTranslated(dx, dy, dz)
    #glRotated(angle, 0.0, 0.0, 1.0)
    glCallList(poly)
    glPopMatrix()