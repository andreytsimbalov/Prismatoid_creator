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

class model3D:
    # verticies=[]
    # edges=[]
    # polygons=[]

    def __init__(self,ver,reflectance):
        self.verticies=ver
        self.poly = self.makePoly(ver,reflectance)

    def makePoly(self,ver, reflectance):
        list = glGenLists(1)
        glNewList(list, GL_COMPILE)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, reflectance)

        for i in range(len(ver)-1):
            v1=self.verticies[i]
            v2 = self.verticies[i+1]
            verticies = v1+v2
            edges = polygonizer_2(v1, v2)
            polygons = polygonizer_trangle(edges, len(v1), len(verticies))



            glBegin(GL_LINES)
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(verticies[vertex])
            glEnd()

            glBegin(GL_TRIANGLES)
            for i in polygons:
                norm = normal([verticies[i[0]], verticies[i[1]], verticies[i[2]]])
                glNormal3d(norm[0], norm[1], norm[2])
                for j in range(3):
                    k = i[j]
                    glVertex3d(verticies[k][0], verticies[k][1], verticies[k][2])
            glEnd()

        glEndList()
        return list

    def drawPoly(self):
        glPushMatrix()
        glCallList(self.poly)
        glPopMatrix()

    def poly(self):
        return self.poly


def file_reader(file):
    #s="models\coord.txt"
    f = open(file, 'r')
    a = []
    m=[]
    for s in f:
        j = [s.split()]
        for i in j:
            for k in i:
                a += [float(k)]
    #print(a)

    sloi = int(a[0])
    modelCount = int(a[1])
    k=2
    for i in range(modelCount):

        reflectance = (random.random(), random.random(), random.random(), 1.0)
        start=k
        for i in range(sloi):
            k+=int(a[k])*2+1
        vi=[]+a[start:k]
        #print(vi)
        m+=[model3D(modelGenerator(vi,sloi),reflectance)]
    return m

    # v1=fig_from_file("models\model_3.txt",1)
    # v2 = fig_from_file("models\model_2.txt", 0)
    # v3 = fig_from_file("models\coords.txt", -1)
    #
    # v=[]
    # v+=[v1]
    # v+=[v2]
    # v += [v3]
    #
    # #qwe=model3D(v,reflectance)
    #
    # f.close()
    # return model3D(v,reflectance)


def makePoly(reflectance, mashtab):
    # v1 = prav_fig(0.7*mashtab, [0, 0, 1*mashtab], 3)  # + [[-2, 0, 1]]  # правильный Н гранник
    # v2 = prav_fig(1*mashtab, [0, 0, 0*mashtab], 3)  # правильный М гранник


    #v1 = prav_fig(1*mashtab*random.random()+0.2, [random.randint(-10, 10) / 20, random.randint(-10, 10) / 20, 1*mashtab],random.randint(3, 10))  # + [[-2, 0, 1]]  # правильный Н гранник
    v2 = prav_fig(  1*mashtab*random.random()+0.2, [random.randint(-10, 10) / 20, random.randint(-10, 10) / 20, 0*mashtab]                         , random.randint(3, 10))

    v1=fig_from_file("models\coords_1.txt",1)
    v2 = fig_from_file("models\coords_2.txt", 0)

    v=[]
    v+=[v1]
    v+=[v2]

    #qwe=model3D(v,reflectance)
    # qwe=file_reader(reflectance)
    # return qwe.poly

    verticies = v1 + v2
    edges = polygonizer_2(v1, v2)

    #print(edges)

    # v1 = prav_fig(0.7 * mashtab, [0.5, 0, 1 * mashtab], 5)  # + [[-2, 0, 1]]  # правильный Н гранник
    # v2 = prav_fig(1 * mashtab, [0, 0, 0 * mashtab], 7)  # правильный М гранник
    # verticies = v1 + v2
    # edges = polygonizer_2(v1, v2)
    # print(edges)

    polygons = polygonizer_trangle(edges, len(v1), len(verticies))
    #print(polygons)

    list = glGenLists(1)
    glNewList(list, GL_COMPILE)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE,reflectance)

    #glShadeModel(GL_FLAT)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    # glBegin(GL_TRIANGLES)
    # for i in range(0,9):#[random.randint(0,8),random.randint(0,8),random.randint(0,8)]:
    #     glNormal3d(random.randint(0,1),random.randint(0,1),random.randint(0,1))
    #     glColor3f(random.random() * 2, random.random() * 2, 0.0)
    #     glVertex3d(verticies[i][0],verticies[i][1],verticies[i][2])
    # glEnd()
    glBegin(GL_TRIANGLES)
    for i in polygons:  # [random.randint(0,8),random.randint(0,8),random.randint(0,8)]:
        norm = normal([verticies[i[0]], verticies[i[1]], verticies[i[2]]])
        #print(i)
        #glNormal3d(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1))
        glNormal3d(norm[0],norm[1],norm[2])

        for j in range(3):
            k = i[j]
            #norm=normal([verticies[k], verticies[k], verticies[k]])
            #print(norm)
            #glNormal3d(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1))
            #glColor3f(random.random() * 2, random.random() * 2, 0.0)

            glVertex3d(verticies[k][0], verticies[k][1], verticies[k][2])
    glEnd()

    glEndList()
    return list



def drawPoly(poly):

    glPushMatrix()
    #glRotated(angle, 0.0, 0.0, 1.0)
    glCallList(poly)
    glPopMatrix()