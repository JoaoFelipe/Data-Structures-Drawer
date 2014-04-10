from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import (
    create_circular_linked_list,
    create_linked_list,
)
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.circle import Circle
from ds_drawer.shapes.sub_arrow import SubArrow
from ds_drawer.viewer import viewer


RED = (255, 0, 0)
BLUE = (0, 0, 255)


def search():
    l, e1, a12, e2, a2n, n = create_linked_list([1, 2])
    sa = SubArrow(e2.prox_2, e1.start_2)
    ant1 = Pointer(e1, 'ant', direction='d.d_2', color=RED, dist=25)
    p1 = Pointer(e1, 'p', direction='u.u_2', color=RED)
    ant2 = Pointer(e2, 'ant', direction='d.d_2', color=RED, dist=25)
    p2 = Pointer(e2, 'p', direction='u.u_2', color=RED)
    circ = Circle((n.x + 40, n.y), "1", color=BLUE)
    cant1 = Cross(ant1.label, color=BLUE)
    cp2 = Cross(p2.label, color=RED)
    return [
        l, e1, a12, e2, sa, circ,
        ant1, ant2, p1, p2, cant1, cp2
    ]


def remove():
    l, e1, a12, e2, sa = create_circular_linked_list(
        [1, 2], color=RED, y=220)
    sa = SubArrow(e2.prox_2, e1.start_2, color=RED, size_y=40, size_x1=25)
    p1 = Pointer(e1, 'p', direction='u.u_2', color=RED)
    ant2 = Pointer(e2, 'ant', direction='d.d_2', color=RED, dist=25)
    sa2 = SubArrow(e2.prox_3, e2.start_3, color=BLUE, size_y=20)
    csa = Cross(sa, color=BLUE)
    cl = Cross(l.label, color=BLUE)
    l2 = Pointer(e2, 'l', direction='ul.u_0', color=BLUE)
    return [
        l, e1, a12, e2, sa,
        ant2, p1, sa2, csa, cl, l2
    ]


def draw():
    return search() + remove()


if __name__ == '__main__':
	viewer(draw)
