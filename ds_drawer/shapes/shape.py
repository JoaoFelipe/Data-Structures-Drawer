from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from .point import Point


class Shape(Point):

    def __init__(self, point, color=(0,0,0)):
        super(Shape, self).__init__(point[0], point[1])
        self.color = color

    def draw(self, screen):
        pass
