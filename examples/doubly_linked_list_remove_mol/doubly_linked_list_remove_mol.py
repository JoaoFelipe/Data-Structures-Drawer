from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_doubly_linked_list
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.doubly_linked_list import DoublyLinkedList
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.shapes.sub_arrow import SubArrow
from ds_drawer.shapes.circle import Circle
from ds_drawer.shapes.label import Label
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.viewer import viewer


RED = (255, 0, 0)
BLUE = (0, 0, 255)


def search():
    [
        l, s, as3, e3, a31, a13, e1, a12, a21, e2, a2e, e
    ] = create_doubly_linked_list([3, 1, 2])
    circ = Circle((e.x + 40, e.y), "1", color=BLUE)
    p = Pointer(e1, 'p = busca(l, 1)', direction='u.u_2', color=RED)
    label1 =  Label((e1.mx + 19, e1.my+25),
        "p->ant->prox = p->prox;", color=RED)
    label2 =  Label((e1.mx + 15, e1.my+40),
        "p->prox->ant = p->ant;", color=RED)
    ca31 = Circle(a31, "", color=RED, radius=10)
    ca21 = Circle(a21, "", color=RED, radius=10)
    return [
        l, s, as3, e3, a31, a13, e1, a12, a21, e2, a2e, e,
        p, circ, ca31, ca21, label1, label2
    ]


def remove():
    [
        l, s, as3, e3, a31, a13, e1, a12, a21, e2, a2e, e
    ] = create_doubly_linked_list([3, 1, 2], color=RED, y=220)
    ca31 = Cross(a31, color=BLUE)
    ca21 = Cross(a21, color=BLUE)
    desloc = lambda p, d: (p[0], p[1] + d)
    sa32 = SubArrow(desloc(e3.prox_1, - 3), desloc(e2.start_1, - 3), 
        size_y=-15, color=BLUE)
    sa23 = SubArrow(desloc(e2.ant_3, 3), desloc(e3.end_3, 3), 
        size_y=15, color=BLUE, reverse=True)
    c1 = Cross(e1.middle, color=BLUE, size=20)
    return [
        l, s, as3, e3, a31, a13, e1, a12, a21, e2, a2e, e,
        ca31, ca21, sa32, sa23, c1
    ]


def draw():
    return search() + remove()


if __name__ == '__main__':
	viewer(draw)
