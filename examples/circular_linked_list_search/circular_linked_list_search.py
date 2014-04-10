from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_circular_linked_list
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.circle import Circle
from ds_drawer.viewer import viewer


RED = (255, 0, 0)


def search1():
    l, e1, a12, e2, a20, e0, sa = create_circular_linked_list([1, 2, 0])
    ant = Pointer(e1, 'ant', direction='d.d_2', color=RED, dist=25)
    p = Pointer(e2, 'p', direction='u.u_2', color=RED)
    c = Circle(a12.middle, "", color=RED, radius=10)
    return [
        l, e1, a12, e2, a20, e0, sa,
        ant, p, c
    ]


def search2():
    l, e1, a12, e2, a20, e0, sa = create_circular_linked_list(
        [1, 2, 0], y=220)
    ant = Pointer(e0, 'ant', direction='d.d_2', color=RED, dist=25)
    p = Pointer(e1, 'p', direction='u.u_2', color=RED)
    return [
        l, e1, a12, e2, a20, e0, sa,
        ant, p
    ]

def draw():
    return search1() + search2()


if __name__ == '__main__':
	viewer(draw)
