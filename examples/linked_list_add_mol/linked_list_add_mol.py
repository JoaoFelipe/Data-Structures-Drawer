from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_circular_linked_list
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.shapes.linked_list import LinkedList
from ds_drawer.shapes.label import Label
from ds_drawer.viewer import viewer


RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw():
    l, e1, a13, e3, a35, e5, a5n, n = create_linked_list([1, 3, None, 5])
    e4 = LinkedList((e5.x - 60, e5.y + 40), 4, color=RED)
    novo = Pointer(e4, 'novo', direction='dl.start_4', color=RED)
    a45 = Arrow(e4.prox_1, e5.start_4, color=RED)
    a34 = Arrow(e3.prox_3, e4.start_0, color=RED)
    p1 = Pointer(e1, 'p', direction='d.d_2', color=RED)
    p3 = Pointer(e3, 'p', direction='d.d_2', color=RED)
    p5 = Pointer(e5, 'p', direction='d.d_2', color=RED)
    ant1 = Pointer(e1, 'ant', direction='dl.d_0', color=BLUE)
    ant3 = Pointer(e3, 'ant', direction='dl.d_0', color=BLUE)
    c1 = Cross(p1.label, color=RED)
    c3 = Cross(p3.label, color=RED)
    cant1 = Cross(ant1.label, color=BLUE)
    label1 =  Label(
        (p5.label.mx + 15, p5.label.my+20), "novo->prox = p;", color=RED)
    label2 =  Label(
        (p5.label.mx + 22, p5.label.my+40), "ant->prox = novo;", color=RED)
    
    return [
        l, e1, a13, e3, a35, e5, a5n, n,
        e4, novo, a34, a45, p1, p3, p5, c1, c3,
        ant1, ant3, cant1, label1, label2
    ]


if __name__ == '__main__':
	viewer(draw)
