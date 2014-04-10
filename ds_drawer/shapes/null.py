from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pygame

from .shape import Shape


class Null(Shape):

    def __init__(self, point, color=(0,0,0), height=30, l1=5, l2=3, l3=1):
        super(Null, self).__init__(point, color)
        self.height = height
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def draw(self, screen):
        y0 = self.y + self.height // 2
        y1 = y0 + self.height // 4
        pygame.draw.line(
            screen, 
            self.color, 
            (self.x, y0),
            (self.x, y1),
        )
        pygame.draw.line(
            screen, 
            self.color, 
            (self.x - self.l1, y1),
            (self.x + self.l1, y1),
        )
        y1 += self.height // 8
        pygame.draw.line(
            screen, 
            self.color, 
            (self.x - self.l2, y1),
            (self.x + self.l2, y1),
        )
        y1 += self.height // 8
        pygame.draw.line(
            screen, 
            self.color, 
            (self.x - self.l3, y1),
            (self.x + self.l3, y1),
        )

    @property
    def my(self):
        return self.y + 2 * (self.height // 4)
