from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import pygame

from .shape import Shape


class DoublyLinkedList(Shape):

    def __init__(self, point, text="", color=(0,0,0), 
            width=30, height=30, pointer_width=10, font_size=25):
        super(DoublyLinkedList, self).__init__(point, color)
        self.text = text
        
        self.text_width = width
        self.height = height
        self.pointer_width = pointer_width

        self.font = pygame.font.SysFont("", font_size)

        self.update_points()
        
    def update_points(self):
        x_pos_ant = self.x + self.pointer_width
        x_pos_text = x_pos_ant + self.text_width
        step_y = self.height // 4
        step_x = self.width // 4
        for i in range(5):
            setattr(self, ('prox_%d'%i), (
                x_pos_text + self.pointer_width // 2,
                self.y + i * step_y
            ))
            setattr(self, ('pre_prox_%d'%i), (
                x_pos_text,
                self.y + i * step_y
            ))
            setattr(self, ('ant_%d'%i), (
                self.x + self.pointer_width // 2,
                self.y + i * step_y
            ))
            setattr(self, ('pos_ant_%d'%i), (
                x_pos_ant,
                self.y + i * step_y
            ))
            setattr(self, ('start_%d'%i), (
                self.x,
                self.y + i * step_y
            ))
            setattr(self, ('end_%d'%i), (
                x_pos_text + self.pointer_width,
                self.y + i * step_y
            ))
            setattr(self, ('u_%d'%i), (
                self.x + i * step_x,
                self.y
            ))
            setattr(self, ('d_%d'%i), (
                self.x + i * step_x,
                self.y + 4 * step_y
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
        pygame.draw.line(
            screen,
            self.color,
            self.pos_ant_0,
            self.pos_ant_4
        )
        surface = self.font.render(str(self.text), True, self.color)
        rect = surface.get_rect()
        rect.center = self.middle
        screen.blit(surface, rect.topleft)

    @property
    def width(self):
        return self.text_width + 2 * self.pointer_width

    @property
    def mx(self):
        return self.x + self.pointer_width + self.text_width // 2

    @property
    def my(self):
        return self.y + self.height // 2
