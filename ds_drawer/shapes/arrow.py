from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pygame

from .shape import Shape
from ds_drawer.algebra import (
    rotate_point, rotate, translate, mid_point, angle
)


class Arrow(Shape):
    def __init__(self, p1, p2, color=(0,0,0), model=None):
        super(Arrow, self).__init__(mid_point(p1, p2), color)
        if not model:
            model = [
                [2, 0],
                [-6, -4],
                [-6, 4],
            ]
        ang = angle(p1, p2)
        self.arrow = translate(rotate(model, ang), p2)
        self.p1 = p1
        self.p2 = p2

    def draw(self, screen):
        pygame.draw.line(
            screen, 
            self.color, 
            self.p1,
            self.p2
        )
        pygame.draw.polygon(
            screen, 
            self.color, 
            self.arrow,
        )
