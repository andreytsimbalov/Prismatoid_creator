import numpy as np
import math as m
import random
from test_1 import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class mazaika:
    # verticies=[]
    # edges=[]
    # polygons=[]

    kletki = []
    layers = 0
    inter_node = []
    objects = 0
    num_of_layer = 1

    def __init__(self, number_angles):
        print(self.objects)
        self.objects = 0
        self.kletki = []
        self.layers = 0
        self.inter_node = []
        self.num_of_layer = 1
        self.num_angles = number_angles
        if (number_angles == 4 or number_angles == 3 or number_angles == 6):
            self.mazaika_cr(number_angles)
        else:
            self.first_creation(number_angles)
        # self.first_creation(number_angles)

    def first_creation(self, number):
        a = kletka(0.7, [0, 0], number, 1.57 / 3)
        self.kletki = [a]

    def add_kletk(self, number):
        a = kletka(0.7, [0, 0], number, 1.57 / 2)
        self.kletki += [a]

    def mazaika_cr(self, number):
        self.kletki = []
        radius = 0.5
        if number == 4:
            # print('qew',4)
            smesh = radius / (2 ** 0.5)
            for i in range(-2, 3):
                for j in range(-2, 3):
                    a = kletka(radius, [smesh * i * 2, smesh * j * 2], number, 1.57 / 2)
                    self.kletki += [a]
        elif number == 3:
            # print('qew',3)
            smesh = 1.5 * radius / (3 ** 0.5)
            for i in range(-1, 2):
                for j in range(-2, 2):
                    a = kletka(radius, [smesh * i * 2, radius * 1.5 * j + radius * 0.5 + radius * 0.5 * (j % 2)],
                               number, j % 2 * 3.14)  # +radius*0.5*j%2
                    self.kletki += [a]
            for i in range(-2, 2):
                for j in range(-2, 2):
                    a = kletka(radius, [smesh * i * 2 + smesh * 1,
                                        radius * 1.5 * j + radius * 0.5 + radius * 0.5 * ((j + 1) % 2)], number,
                               (j + 1) % 2 * 3.14)
                    self.kletki += [a]
        elif number == 6:
            smesh = 1 / 2 * radius * (3 ** 0.5)
            for i in range(-1, 1):
                for j in range(-1, 2):
                    a = kletka(radius, [radius * i * 3 + radius * 1.5, smesh * 2 * j], number, 1.57 / 3)
                    self.kletki += [a]
            for i in range(-1, 2):
                for j in range(-2, 2):
                    a = kletka(radius, [radius * i * 3, smesh * 2 * j + smesh], number, 1.57 / 3)
                    self.kletki += [a]

    def makeLayer(self, number_of_sloi):
        # reflectance = (1, 1, 1, 1)
        # reflectance = (random.random(), random.random(), random.random(), 1)
        # list=0
        # print("MakeLayer", 1)
        list = glGenLists(1)
        glNewList(list, GL_COMPILE)
        glLineWidth(3)
        if self.objects != 0:
            #
            reflectance = (0.7, 0.2, 0.3, 1)
            glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, reflectance)
            glBegin(GL_TRIANGLE_FAN)

            center = self.objects.layers[0][0]
            # sl = self.objects.layers[number_of_sloi]

            glVertex3f(center[0] + 0.03, center[1] + 0.03, 0)
            glVertex3f(center[0] + 0.03, center[1] - 0.03, 0)
            glVertex3f(center[0] - 0.03, center[1] - 0.03, 0)
            glVertex3f(center[0] - 0.03, center[1] - 0.03, 0)
            glVertex3f(center[0] - 0.03, center[1] + 0.03, 0)
            glVertex3f(center[0] + 0.03, center[1] + 0.03, 0)

            sl = self.objects.activ_lines[number_of_sloi]
            counter = 0
            # glVertex3f(center[0] - 0.03, center[1] + 0.03, 0)
            # glVertex3f(center[0] + 0.03, center[1] + 0.03, 0)
            glVertex3f(center[0], center[1], 0)
            for i in range(len(sl)):
                if sl[i] != [-100, -100]:
                    glVertex3f(sl[i][0], sl[i][1], 0)
                    # print(i)
                    # counter += 1
                    # if counter == 2:
                    #     counter = 0
                    #     glVertex3f(center[0], center[1], 0)
                    #     glVertex3f(sl[i][0], sl[i][1], 0)
            for i in range(len(sl)):
                if sl[i] != [-100, -100]:
                    glVertex3f(sl[i][0], sl[i][1], 0)
                    # glVertex3f(center[0], center[1], 0)
                    break

            # for j in range(len(sl)):
            #     if len(sl) == 1:
            #         glVertex3f(sl[j][0] + 0.03, sl[j][1] + 0.03, 0)
            #         glVertex3f(sl[j][0] + 0.03, sl[j][1] - 0.03, 0)
            #         glVertex3f(sl[j][0] - 0.03, sl[j][1] - 0.03, 0)
            #         glVertex3f(sl[j][0] - 0.03, sl[j][1] - 0.03, 0)
            #         glVertex3f(sl[j][0] - 0.03, sl[j][1] + 0.03, 0)
            #         glVertex3f(sl[j][0] + 0.03, sl[j][1] + 0.03, 0)
            #
            #     glVertex3f(sl[j][0], sl[j][1], 0)
            glEnd()

            # print(len(self.objects.lines))
            b = self.objects.lines
            glBegin(GL_LINES)
            for j in b:
                for k in j:
                    glVertex3f(k[0], k[1], 0)

            glEnd()

        reflectance = (1, 1, 1, 1)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, reflectance)

        glLineWidth(2)
        # glBegin(GL_LINE_LOOP)

        # print("MakeLayer",2)

        for i in self.kletki:
            glBegin(GL_LINE_LOOP)

            # i.layer_correct()
            sl = i.layers[number_of_sloi]
            for j in range(len(sl)):
                glVertex3f(sl[j][0], sl[j][1], 0)
            glEnd()
        # glEnd()
        # print(c,m)

        # print("MakeLayer",3)

        glEndList()

        self.layers = list
        # print(self.layers)
        # return list

    def draw(self):
        glPushMatrix()
        glCallList(self.layers)
        glPopMatrix()

    def add_layer(self):
        print("adding maz")
        for i in self.kletki:
            print(len(i.layers))
            i.add_layer()
            print(len(i.layers))

        print("adding obj")
        if self.objects != 0:
            self.objects.add_layer()

        print("adding maz")

    def add_obj(self, x, y, sl):
        self.objects = obj_kl(x, y, len(self.kletki[0].layers))
        eps = 0.01
        kl_sopr = []
        for i in self.kletki:
            s = i.layers[sl]
            for vert in s:
                if rast_per_2_points(x, y, vert[0], vert[1]) < eps:
                    kl_sopr += [i]
        self.objects.kl_sopr = kl_sopr

        self.objects.lines = []

        eps = 0.01
        for i in self.objects.kl_sopr:
            kl = i.layers[sl]
            ob = self.objects.layers[sl]

            for j in range(len(kl)):
                for k in range(len(ob)):
                    if rast_per_2_points(kl[j][0], kl[j][1], ob[k][0], ob[k][1]) < eps:
                        if len(self.objects.lines) == 0:
                            self.objects.lines += [[ob[k], kl[(j - 1) % len(kl)]]]

                        flag_1 = True
                        for i in self.objects.lines:
                            if rast(i[1], kl[(j - 1) % len(kl)]) < 0.01:
                                flag_1 = False
                                break
                        if flag_1:
                            self.objects.lines += [[ob[k], kl[(j - 1) % len(kl)]]]
                        # self.objects.lines += [[ob[k], kl[(j - 1) % len(kl)]]]
                        flag_1 = True
                        for i in self.objects.lines:
                            if rast(i[1], kl[(j + 1) % len(kl)]) < 0.01:
                                flag_1 = False
                                break
                        if flag_1:
                            self.objects.lines += [[ob[k], kl[(j + 1) % len(kl)]]]

        v1 = [self.objects.lines[0][1][0] - self.objects.lines[0][0][0],
              self.objects.lines[0][1][1] - self.objects.lines[0][0][1]]
        min_angle = 3.142
        j_flag = 0
        for i in range(1, len(self.objects.lines)):
            v2 = [self.objects.lines[i][1][0] - self.objects.lines[i][0][0],
                  self.objects.lines[i][1][1] - self.objects.lines[i][0][1]]
            if angle_between(v1, v2) < min_angle:
                min_angle = angle_between(v1, v2) + 0.01
                j_flag = i
        print("ma", min_angle)
        v1 = [self.objects.lines[j_flag][1][0] - self.objects.lines[j_flag][0][0],
              self.objects.lines[j_flag][1][1] - self.objects.lines[j_flag][0][1]]
        array_of_lines = [0, j_flag]
        # print(array_of_lines)
        iterable_flag = 0
        while len(array_of_lines) != len(self.objects.lines):
            iterable_flag += 1
            if iterable_flag > 100:
                break

            for i in range(1, len(self.objects.lines)):
                if not (i in array_of_lines):
                    v2 = [self.objects.lines[i][1][0] - self.objects.lines[i][0][0],
                          self.objects.lines[i][1][1] - self.objects.lines[i][0][1]]
                    if angle_between(v1, v2) < min_angle:
                        j_flag = i
                        array_of_lines += [i]
                        v1 = [self.objects.lines[j_flag][1][0] - self.objects.lines[j_flag][0][0],
                              self.objects.lines[j_flag][1][1] - self.objects.lines[j_flag][0][1]]
        print(array_of_lines)

        arr = []
        for i in array_of_lines:
            arr += [self.objects.lines[i]]
        self.objects.lines = [] + arr

        for i in range(len(self.objects.layers)):
            a = [[-100, -100]] * (len(self.objects.lines))
            self.objects.activ_lines += [a]
        print("qwqwe", self.objects.activ_lines)

        if iterable_flag > 100:
            self.objects = 0

        # v1 = [self.objects.lines[0][1][0] - self.objects.lines[0][1][1],
        #       self.objects.lines[0][0][0] - self.objects.lines[0][0][1]]
        # v2 = [self.objects.lines[1][1][0] - self.objects.lines[1][1][1],
        #       self.objects.lines[1][0][0] - self.objects.lines[1][0][1]]
        # print("angle", angle_between(v1, v2))

    def add_obj_vert(self, x, y, sl):
        print("added")
        # self.objects.layers[sl]+=[[x,y]]
        for i in range(len(self.objects.lines)):
            s = self.objects.lines[i]
            if abs(rast(s[0], s[1]) - rast(s[0], [x, y]) - rast(s[1], [x, y])) < 0.01:
                self.objects.activ_lines[sl][i] = [x, y]
                flag_add = False

                print("zxc", i)

                # for j in range(1, len(self.objects.layers[sl])):
                #     e = self.objects.layers[sl][j]
                #     if abs(rast(s[0], s[1]) - rast(s[0], e) - rast(s[1], e)) < 0.01:
                #         self.objects.layers[sl][j] = [x, y]
                #         flag_add = True
                #         break
                #
                # if not (flag_add):
                #     self.objects.layers[sl] += [[x, y]]

        # for i in self.objects.lines:
        #     if abs(rast(i[0],i[1])-rast(i[0],[x,y])-rast(i[1],[x,y]))<0.05:
        #         self.objects.activ_lines+=[j]

        # s=self.objects.layers[sl][0]
        # for i in self.objects.layers[sl]:
        #     for k in range(len(self.objects.lines)):
        #         j = k * 2
        #         a = self.objects.lines[j]
        #         b = self.objects.lines[j + 1]
        #         if abs(rast(a, b) - rast(a, [x, y]) - rast(b, [x, y])) < 0.05:
        # self.objects.layers[sl]

    def bliz_point_search(self, x, y, sl):
        rast = 4
        xi = 0
        yi = 0
        for i in self.kletki:
            s = i.layers[sl]
            for vert in s:
                if rast_per_2_points(x, y, vert[0], vert[1]) < rast:
                    rast = rast_per_2_points(x, y, vert[0], vert[1])
                    xi = vert[0]
                    yi = vert[1]

        return [xi, yi]

    def cleaning_activ_lines(self, sl):
        self.objects.activ_lines[sl] = [[-100, -100]] * len(self.objects.activ_lines[sl])

    def line_and_point_search(self, x, y, sl):
        if self.objects != 0:

            eps1 = 0.1
            eps = 0.01
            for i in self.objects.layers[0]:
                if rast([x, y], i) < eps1:
                    # for i in range(len(self.objects.activ_lines[sl])):
                    #
                    # print('123',self.objects.activ_lines[sl])
                    # self.objects.activ_lines[sl]=[[-100,-100]]*len(self.objects.activ_lines[sl])
                    return i
            fl = 0
            fl1 = 0
            h = 4
            c = 4
            per_point = [0, 0]
            for j in range(len(self.objects.lines)):
                s = self.objects.lines[j]
                r = [(s[0][0] + s[1][0]) / 2, (s[0][1] + s[1][1]) / 2]
                if rast(r, [x, y]) < c:
                    c = rast(r, [x, y])
                    fl1 = j
                # if rast(s[1], [x, y]) < c:
                #     c = rast(s[1], [x, y])
                #     fl1 = j

                t1 = s[0]
                t2 = s[1]
                k = line_k(s[0], s[1])
                d_centr = line_d([k[1], -k[0]], [x, y])
                d_point = line_d(k, s[1])
                p_peres = point_per_two_lines(k, d_point, d_centr)
                h_contr = rast([x, y], p_peres)
                # print(h_contr)
                if h_contr < h:
                    h = h_contr
                    # fl = j
                    per_point = p_peres

            s = self.objects.lines[fl1]
            # return per_point
            # print(fl1, s[0], s[1])
            # print(rast(s[0], s[1]), rast(s[0], per_point), rast(s[1], per_point))
            if abs(rast(s[0], s[1]) - rast(s[0], per_point) - rast(s[1], per_point)) < eps:
                # print("per",abs(rast(s[0],s[1])-rast(s[0],per_point)-rast(s[1],per_point)))
                return per_point
            else:
                if rast([x, y], s[0]) < rast([x, y], s[1]):
                    # print(rast([x,y],s[0]),rast([x,y],s[1]))
                    return s[0]
                else:
                    # print(rast([x, y], s[0]), rast([x, y], s[1]))
                    return s[1]

        else:
            print("_______error_______")
            return [x, y]
            return [0, 0]

    def releas_text(self):
        print("end")
        # point=[0,0]
        if self.objects != 0:

            f = open('text.txt', 'w')

            matr=[]
            matr1=[]
            matr2=[]
            numb_lay = len(self.objects.activ_lines)
            if numb_lay == 1:
                numb_lay = 2
            f.write(str(numb_lay) + '\n')
            n = len(self.objects.kl_sopr)
            f.write(str(n + 1) + '\n')  # позже используем
            # f.write(str(1) + '\n')
            # numb_lay = 2
            # numb_lay = len(self.objects.activ_lines)
            for sloi in range(numb_lay):
                print("sloi", sloi)
                if len(self.objects.activ_lines) == 1:
                    sl = 0
                else:
                    sl = sloi
                a = []
                count = 0
                c_nach = 0
                nach_fl = False
                c_stat = 0
                if self.num_angles == 3:
                    for i in range(len(self.objects.activ_lines[sl])):
                        q = 0
                        if (self.objects.activ_lines[sl][i] != [-100, -100]) and (
                                self.objects.activ_lines[sl][(i + 1) % 6] != [-100, -100]) and (
                                self.objects.activ_lines[sl][(i - 1) % 6] != [-100, -100]):
                            cent = [self.objects.lines[0][0][0], self.objects.lines[0][0][1]]
                            pa = rast(cent, self.objects.activ_lines[sl][(i + 1) % 6])
                            pb = rast(cent, self.objects.activ_lines[sl][(i - 1) % 6])
                            pc = 2 * pa * pb * m.cos(3.14 / 3) / (pa + pb)
                            if rast(cent, self.objects.activ_lines[sl][i]) < pc:
                                self.objects.activ_lines[sl][i] = [-100, -100]

                    for i in range(len(self.objects.activ_lines[sl])):
                        if (self.objects.activ_lines[sl][i] == [-100, -100]) and (
                                self.objects.activ_lines[sl][(i + 1) % 6] != [-100, -100]) and (
                                self.objects.activ_lines[sl][(i - 1) % 6] != [-100, -100]):
                            cent = [self.objects.lines[0][0][0], self.objects.lines[0][0][1]]
                            pa = rast(cent, self.objects.activ_lines[sl][(i + 1) % 6])
                            pb = rast(cent, self.objects.activ_lines[sl][(i - 1) % 6])
                            pc = 2 * pa * pb * m.cos(3.14 / 3) / (pa + pb)+0.001
                            v1 = self.objects.lines[i]
                            pv = [cent[0] + (v1[1][0] - v1[0][0]) * pc / rast(v1[0], v1[1]),
                                  cent[1] + (v1[1][1] - v1[0][1]) * pc / rast(v1[0], v1[1])]
                            print("otnoshenie", pc / rast(v1[0], v1[1]))
                            self.objects.activ_lines[sl][i] = pv

                for i in range(len(self.objects.activ_lines[sl])):
                    if (self.objects.activ_lines[sl][i] != [-100, -100]) and (
                            self.objects.activ_lines[sl][(i - 1) % len(self.objects.lines)] != [-100, -100]):
                        j_fl=0

                        for s in range(len(self.objects.kl_sopr)):
                            count_kl=0
                            for k in self.objects.kl_sopr[s].layers[sl]:
                                if rast(k,self.objects.lines[i][1])<0.01:
                                    count_kl+=1
                                if rast(k,self.objects.lines[(i - 1) % len(self.objects.lines)][1])<0.01:
                                    count_kl+=1
                            if count_kl==2:
                                j_fl=s
                                break
                        matr+=[[j_fl,sl,i]]


                for i in range(len(self.objects.activ_lines[sl])):
                    if (self.objects.activ_lines[sl][i] != [-100, -100]) and (
                            self.objects.activ_lines[sl][(i - 1) % len(self.objects.lines)] == [-100, -100]):
                        j_fl=-1

                        for s in range(len(self.objects.kl_sopr)):
                            count_kl=0
                            for k in self.objects.kl_sopr[s].layers[sl]:
                                if rast(k,self.objects.lines[i][1])<0.01:
                                    count_kl+=1
                                if rast(k,self.objects.lines[(i - 1) % len(self.objects.lines)][1])<0.01:
                                    count_kl+=1
                            if count_kl==2:
                                j_fl=s
                                break
                        if j_fl!=-1:
                            matr1+=[[j_fl,sl,i]]
                            print("ADD", matr1)

                for i in range(len(self.objects.activ_lines[sl])):
                    if (self.objects.activ_lines[sl][i] != [-100, -100]) and (
                            self.objects.activ_lines[sl][(i + 1) % len(self.objects.lines)] == [-100, -100]):
                        j_fl=-1

                        for s in range(len(self.objects.kl_sopr)):
                            count_kl=0
                            for k in self.objects.kl_sopr[s].layers[sl]:
                                if rast(k,self.objects.lines[i][1])<0.01:
                                    count_kl+=1
                                if rast(k,self.objects.lines[(i + 1) % len(self.objects.lines)][1])<0.01:
                                    count_kl+=1
                            if count_kl==2:
                                j_fl=s
                                break
                        if j_fl != -1:
                            matr2+=[[j_fl,sl,i]]
                            print("ADD", matr2)




                for i in self.objects.activ_lines[sl]:
                    count += 1
                    if i != [-100, -100]:
                        if not (nach_fl):
                            c_nach = count - 1
                            nach_fl = True
                        if count - 1 > c_stat:
                            c_stat = count - 1
                        count = 0
                        a += [[i[0], i[1]]]
                c_nach += count
                if c_nach > c_stat:
                    c_stat = c_nach

                if (c_stat >= len(self.objects.lines) // 2) and (a != []):
                    print("POINT ADDED", c_stat, len(self.objects.lines))
                    a += [[self.objects.lines[0][0][0], self.objects.lines[0][0][1]]]

                if (a == []):
                    print("POINT ADD1", c_stat, len(self.objects.lines))
                    a += [[self.objects.lines[0][0][0], self.objects.lines[0][0][1]]]
                else:
                    asd = chasovshik(a)
                    print(a)
                    i_flag = 0
                    a_flag = a[0][0]
                    for i in range(len(a)):
                        if a[i][0] > a_flag:
                            a_flag = a[i][0]
                            i_flag = i
                    if i_flag > 0:
                        i_flag -= 1
                        i = i_flag + 1
                        b = []
                        while i != i_flag:
                            b += [a[i]]
                            i = (i + 1) % len(a)
                        b += [a[i]]
                        a = [] + b

                # point=center(a)
                # print(point)
                # for i in range(len(a)):
                #     a[i][0]-=point[0]
                #     a[i][1] -= point[1]

                print(a)
                f.write(str(len(a)) + '\n')
                for i in a:
                    f.write(str(i[0]) + ' ' + str(i[1]) + '\n')
                print(sloi)



            for i in range(len(self.objects.kl_sopr)):
                for j in range(len(self.objects.kl_sopr[i].layers)):
                    j_fl=-1
                    j2_fl=-1
                    for mi in matr:
                        if (mi[0]==i)and(mi[1]==j):
                            j_fl=mi[2]

                    for mi in matr1:
                        if (mi[0]==i)and(mi[1]==j):
                            j2_fl=mi[2]
                    for mi in matr2:
                        if (mi[0]==i)and(mi[1]==j):
                            j2_fl=mi[2]
                    zxc=len(self.objects.kl_sopr[i].layers[j])
                    if (j_fl!=-1)or(j2_fl!=-1):
                        zxc+=1
                    f.write(str(zxc) + '\n')
                    if j2_fl!=-1:
                        r = self.objects.activ_lines[j][j2_fl]
                        f.write(str(r[0]) + ' ' + str(r[1]) + '\n')
                        print("qqqqqqqqqqqqqqqqqqq")
                    for k in self.objects.kl_sopr[i].layers[j]:
                        if (rast(k,self.objects.lines[0][0])<0.01)and(j_fl!=-1):
                            r=self.objects.activ_lines[j][j_fl]
                            f.write(str(r[0]) + ' ' + str(r[1]) + '\n')
                            r = self.objects.activ_lines[j][(j_fl - 1) % len(self.objects.lines)]
                            f.write(str(r[0]) + ' ' + str(r[1]) + '\n')

                        else:
                            f.write(str(k[0]) + ' ' + str(k[1]) + '\n')



            # for i in range(len(self.objects.kl_sopr)):
            #     for j in self.objects.kl_sopr[i].layers:
            #         f.write(str(len(j)) + '\n')
            #         for k in j:
            #             f.write(str(k[0]) + ' ' + str(k[1]) + '\n')

            print("end", len(self.objects.kl_sopr[0].layers))
            f.write(str(123456789))
            f.close()


class kletka:
    layers = []

    def __init__(self, radius, center, number_angles, rotate):
        self.num_angles = number_angles
        self.layers = []
        self.creation(radius, center, number_angles, rotate)

    def creation(self, radius, center, number, rotate):
        fc = []
        for i in range(number):
            ans = []
            phi = i * m.pi * 2 / number + rotate  # повороты в радианах
            ans += [center[0] + radius * m.sin(phi)]
            ans += [center[1] + radius * m.cos(phi)]
            # ans += [center[2]]
            fc += [ans]
        # print(fc)
        # self.verticies=fc
        self.layers = [fc]

    def add_layer(self):
        self.layers += [self.layers[0]]

    def layer_correct(self):
        if len(self.layers) == 1:
            self.layers += self.layers


class obj_kl:
    kl_sopr = []
    layers = []
    lines = []
    activ_lines = []

    def __init__(self, x, y, numb_of_layers):
        # print(self.activ_lines)
        self.kl_sopr = []
        self.layers = []
        self.lines = []
        self.activ_lines = []
        for i in range(numb_of_layers):
            self.layers += [[[x, y]]]
            print(numb_of_layers)

    def add_layer(self):
        asd = len(self.activ_lines[0])
        zxc = [[-100, -100]] * asd
        self.activ_lines += [zxc]

    def layer_correct(self):
        if len(self.layers) == 1:
            self.layers += self.layers

    def add_kl_sopr(self, mas):
        self.kl_sopr += mas


def drawPoly(poly):
    glPushMatrix()
    glCallList(poly)
    glPopMatrix()


def rast_per_2_points(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def point_draw(x, y):
    reflectance = (1, 0, 0, 1)
    # list=0
    list = glGenLists(1)
    glNewList(list, GL_COMPILE)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, reflectance)

    # glBegin(GL_LINE_LOOP)
    glBegin(GL_TRIANGLES)
    glVertex3f(x + 0.03, y + 0.03, 0)
    glVertex3f(x + 0.03, y - 0.03, 0)
    glVertex3f(x - 0.03, y - 0.03, 0)

    glVertex3f(x - 0.03, y - 0.03, 0)
    glVertex3f(x - 0.03, y + 0.03, 0)
    glVertex3f(x + 0.03, y + 0.03, 0)

    glEnd()

    glEndList()

    # self.layers = list
    # print(self.layers)
    # print(list)
    # return list

    glPushMatrix()
    glCallList(list)
    glPopMatrix()
    # print("painting",x,y)


if __name__ == "__main__":
    pass
