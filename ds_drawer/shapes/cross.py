from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pygame

from .shape import Shape


class Cross(Shape):

    def __init__(self, point, color=(0,0,0), size=5):
        super(Cross, self).__init__(point, color)
        
        self.size = size

    def draw(self, screen):
        pygame.draw.line(
            screen, 
            self.color, 
            (self.mx - self.size, self.my - self.size),
            (self.mx + self.size, self.my + self.size),
        )
        pygame.draw.line(
            screen, 
            self.color, 
            (self.mx - self.size, self.my + self.size),
            (self.mx + self.size, self.my - self.size),
        )
