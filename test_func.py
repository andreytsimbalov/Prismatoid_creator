def line_k(i1, i2):  # kx,ky
    return [i1[1] - i2[1], i2[0] - i1[0]]


def line_d(k, p):  # d
    return -p[0] * k[0] - p[1] * k[1]


def line(i1, i2):
    return [i1[1] - i2[1], i2[0] - i1[0], i1[0] * i2[1] - i2[0] * i1[1]]


def point_per_two_lines(k, d1, d2):  # k[0]x+k[1]y+d=0 - уравнение прямой, работает толко для перпенд прямых
    x = 0
    y = 0
    if k[0] == 0:
        x = -d2 / k[1]
        y = -d1 / k[1]
    elif k[1] == 0:
        y = -d2 / k[0]
        x = -d1 / k[0]
    else:
        y = (d1 / k[0] - d2 / k[1]) * (k[0] * k[1] / (-k[0] ** 2 - k[1] ** 2))
        x = (-y * k[1] - d1) / k[0]
    return [x, y]


k1 = line_k([2, 1], [0, 0])
d1 = line_d(k1, [0, 0])

k2 = line_k([1, -2], [0, 0])
d2 = line_d(k2, [3, -1])

print(point_per_two_lines(k1, d1, d2))
