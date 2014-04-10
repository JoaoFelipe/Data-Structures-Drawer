from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pygame

from .shape import Shape
from ds_drawer.algebra import (
    rotate_point, rotate, translate, mid_point, angle
)


class Line(Shape):
    def __init__(self, p1, p2, color=(0,0,0), model=None):
        super(Line, self).__init__(mid_point(p1, p2), color)
        self.p1 = p1
        self.p2 = p2

    def draw(self, screen):
        pygame.draw.line(
            screen, 
            self.color, 
            self.p1,
            self.p2
        )
