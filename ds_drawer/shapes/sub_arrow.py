from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pygame

from .shape import Shape
from .line import Line
from .arrow import Arrow


class SubArrow(Shape):

    def __init__(self, p1, p2, color=(0,0,0), size_x1=15, size_x2=15, 
            size_y=20, reverse=False):
        if reverse:
            size_x1 = -size_x1
            size_x2 = -size_x2
        p1_1 = [p1[0] + size_x1, p1[1]]
        p1_2 = [p1[0] + size_x1, p1[1] + size_y]
        p2_1 = [p2[0] - size_x2, p2[1]]
        p2_2 = [p2[0] - size_x2, p1[1] + size_y]
        x, y = (p2_2[0] + p1_2[0]) // 2, (p2_2[1] + p1_2[1]) // 2
      	super(SubArrow, self).__init__((x, y), color)

        self.elements = [
            Line(p1, p1_1, color),
            Line(p1_1, p1_2, color),
            Line(p1_2, p2_2, color),
            Line(p2_2, p2_1, color),
            Arrow(p2_1, p2, color)
        ]

    def draw(self, screen):
        for element in self.elements:
            element.draw(screen)