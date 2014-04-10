from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pygame

from .shape import Shape
from .arrow import Arrow
from .line import Line
from .label import Label

class Pointer(Shape):

    def __init__(self, element, text, direction="ul.middle", 
            color=(0, 0, 0), dist=20, arrow=True):
        lp, method = direction.split('.')
        o = getattr(element, method)
        p = list(o)
        if 'u' in lp:
            p[1] -= dist    
        if 'l' in lp:
            p[0] -= dist
        if 'd' in lp:
            p[1] += dist
        if 'r' in lp:
            p[0] += dist
        self.label = Label(p, text, color=color, font_size=20)
        super(Pointer, self).__init__(self.label.rect.center, color)
        
        if arrow:
            self.arrow = Arrow(self.label.nearest(o), o, color=color)
        else:
            self.arrow = Line(self.label.nearest(o), o, color=color)

    def draw(self, screen):
        self.label.draw(screen)
        self.arrow.draw(screen)
