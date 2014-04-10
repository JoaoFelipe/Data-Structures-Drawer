from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pygame

from .shape import Shape
from ds_drawer.algebra import distance

class Label(Shape):

    def __init__(self, point, text, color=(0, 0, 0), font_size=20):
        self.text = text
        self.font = pygame.font.SysFont("", font_size)
        self.surface = self.font.render(str(self.text), True, color)
        self.rect = self.surface.get_rect()
        self.rect.center = (point[0], point[1])
        super(Label, self).__init__(self.rect.center, color)
        
    def draw(self, screen):
        screen.blit(self.surface, self.rect.topleft)

    def nearest(self, p):
        p00 = self.rect.topleft
        p22 = self.rect.bottomright 
        xi = p00[0]
        xf = p22[0]
        hx = (xi + xf) // 2
        yi = p00[1]
        yf = p22[1]
        hy = (yi + yf) // 2
        points = [
            (xi, yi), (xi, hy), (xi, yf),
            (hx, yi), (hx, hy), (hx, yf),
            (xf, yi), (xf, hy), (xf, yf)
        ]
        return min(points, key=lambda x: distance(p, x))
