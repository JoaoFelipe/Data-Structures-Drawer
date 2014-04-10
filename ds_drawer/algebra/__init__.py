from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from math import sin, cos, atan2, sqrt

def rotate_point(ang, p):
    x, y = p[0], p[1]
    return [
        x * cos(ang) - y * sin(ang),
        x * sin(ang) + y * cos(ang)
    ]

def rotate(points, ang):
    return [rotate_point(ang, p) for p in points]

def translate(points, p):
    return [[px + p[0], py + p[1]] for (px, py) in points]

def mid_point(p1, p2):
    return ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def angle(p1, p2):
    return atan2(p2[1]-p1[1], p2[0]-p1[0])