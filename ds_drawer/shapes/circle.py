from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from math import sqrt
import pygame

from .shape import Shape


class Circle(Shape):

    def __init__(self, point, text, color=(0,0,0), radius=15, font_size=25):
        super(Circle, self).__init__(point, color)
        self.text = text
        self.radius = radius

        self.font = pygame.font.SysFont("", font_size)
        self.surface = self.font.render(str(self.text), True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.surface, self.rect.topleft)
        pygame.draw.circle(
            screen, 
            self.color, 
            (self.x, self.y), 
            self.radius,
            1
        )

    def nearest(self, p):
        # y = a*x + b
        a = float(p[1] - self.y) / float(p[0] - self.x)
        b = float(p[1] - a*p[0])
        # y = a1*x**2 + b1*x + c1
        a1 = (1 + a**2)
        b1 = (-2 * self.x - 2*a*self.y + 2*a*b)
        c1 = (self.x**2 + self.y**2 + b**2 - 2*b*self.y - self.radius**2)
        d = b1**2 - 4*a1*c1
        x1 = (-b1 + sqrt(d)) / (2 * a1)
        x2 = (-b1 - sqrt(d)) / (2 * a1)
        y1 = a*x1 + b
        y2 = a*x2 + b
        points = [(x1, y1), (x2, y2)]
        dist = lambda p1, p2: sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        return min(points, key=lambda x: dist(p, x))
