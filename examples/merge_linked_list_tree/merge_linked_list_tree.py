from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_linked_list
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.shapes.linked_list import LinkedList
from ds_drawer.shapes.circle import Circle
from ds_drawer.shapes.line import Line
from ds_drawer.viewer import viewer


RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw():
    # Level 0
    l, n = create_linked_list([], x=35, y=50)
    c2 = Circle((100, 60), "2")
    x = (75, 90)
    li1 = Line((n.x, 70), x, color=BLUE)
    li2 = Line(c2.nearest(x), x, color=BLUE)

    # Level 1
    nl, e2, a2n, n2 = create_linked_list([2], x=45, y=120)
    a2 = Arrow(x, e2.u_3, color=BLUE)
    novo2 = Pointer(e2, 'novo', direction='lu.start_0')
    c1 = Circle((150, 140), "1")
    x = (115, 170)
    li3 = Line(e2.d_4, x, color=BLUE)
    li4 = Line(c1.nearest(x), x, color=BLUE)
    
    # Level 2
    e1 = LinkedList((75, 200), 1)
    a1 = Arrow(x, e1.u_4, color=BLUE)
    novo3 = Pointer(e1, 'novo', direction='lu.start_0')
    a12 = Arrow(e1.prox_1, e2.d_2)
    c3 = Circle((180, 220), "3")
    x = (142, 250)
    li5 = Line(e1.d_4, x, color=BLUE)
    li6 = Line(c3.nearest(x), x, color=BLUE)

    # Level 3
    e3 = LinkedList((102, 280), 3)
    a3 = Arrow(x, e3.u_4, color=BLUE)
    novo4 = Pointer(e3, 'novo', direction='lu.start_0')
    a31 = Arrow(e3.prox_1, e1.d_2)
    l3 = Pointer(e3, 'l', direction='l.start_2')

    return [
        n, l, c2, li1, li2, e2, a2, novo2, a2n, n2,
        c1, li3, li4, e1, a1, novo3, a12, c3, li5, li6,
        e3, a3, novo4, a31, l3
    ]

if __name__ == '__main__':
	viewer(draw)
