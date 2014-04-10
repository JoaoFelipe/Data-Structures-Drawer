from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pygame

from .shape import Shape


class LinkedList(Shape):

    def __init__(self, point, text="", color=(0,0,0), 
            width=30, height=30, pointer_width=10, font_size=25):
        super(LinkedList, self).__init__(point, color)
        self.text = text

        self.text_width = width
        self.height = height
        self.pointer_width = pointer_width

        self.font = pygame.font.SysFont("", font_size)

        self.update_points()
        
    def update_points(self):
        for i in range(5):
            setattr(self, ('prox_%d'%i), (
                self.x + self.text_width + self.pointer_width // 2,
                self.y + i * (self.height // 4)
            ))
            setattr(self, ('pre_prox_%d'%i), (
                self.x + self.text_width,
                self.y + i * (self.height // 4)
            ))
            setattr(self, ('start_%d'%i), (
                self.x,
                self.y + i * (self.height // 4)
            ))
            setattr(self, ('end_%d'%i), (
                self.x + self.text_width + self.pointer_width,
                self.y + i * (self.height // 4)
            ))
            setattr(self, ('u_%d'%i), (
                self.x + i * (self.width // 4),
                self.y
            ))
            setattr(self, ('d_%d'%i), (
                self.x + i * (self.width // 4),
                self.y + 4 * (self.height // 4)
            ))

    def draw(self, screen):
        pygame.draw.lines(screen, self.color, True, [
            self.start_0,
            self.end_0,
            self.end_4,
            self.start_4
        ])
        pygame.draw.line(
            screen,
            self.color,
            self.pre_prox_0,
            self.pre_prox_4
        )
        surface = self.font.render(str(self.text), True, self.color)
        rect = surface.get_rect()
        rect.center = self.middle
        screen.blit(surface, rect.topleft)

    @property
    def width(self):
        return self.text_width + self.pointer_width

    @property
    def mx(self):
        return self.x + self.text_width // 2

    @property
    def my(self):
        return self.y + self.height // 2
