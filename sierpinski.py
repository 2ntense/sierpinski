from math import sqrt, inf, tan, pi
import random
from matplotlib import pyplot as plt


def init_pts():
    side_len = 10.
    height = sqrt(side_len ** 2 - (side_len / 2) ** 2)
    return [(0, 0), (side_len, 0), (side_len / 2, height)]


def add_first_pt(pts: list):
    if len(pts) != 3:
        return 0

    x_max = -inf
    y_max = -inf
    x_min = inf
    y_min = inf
    for pt in pts:
        if pt[0] > x_max:
            x_max = pt[0]
        if pt[1] > y_max:
            y_max = pt[1]
        if pt[0] < x_min:
            x_min = pt[0]
        if pt[1] < y_min:
            y_min = pt[1]

    mid_pt = (x_max, y_max / 2)

    new_pt = mid_pt

    while new_pt == mid_pt:
        rand_x = random.uniform(x_min, x_max)

        if rand_x >= x_max / 2:
            y_upper_bound = abs(rand_x - x_max) * tan(pi / 3)
        else:
            y_upper_bound = rand_x * tan(pi / 3)

        rand_y = random.uniform(y_min, y_upper_bound)
        new_pt = (rand_x, rand_y)

    pts.append(new_pt)


def add_pt(pts):
    if len(pts) == 3:
        add_first_pt(pts)

    rand_vtx = random.choice(pts[:3])
    last_pt = pts[-1]

    ctr_x = (rand_vtx[0] + last_pt[0]) / 2
    ctr_y = (rand_vtx[1] + last_pt[1]) / 2
    ctr_pt = (ctr_x, ctr_y)

    pts.append(ctr_pt)


def draw(pnt_amount):
    pts = init_pts()

    while len(pts) < pnt_amount:
        add_pt(pts)

    plt.scatter(*zip(*pts), s=.5)
    plt.show()


if __name__ == '__main__':
    draw(5000)
