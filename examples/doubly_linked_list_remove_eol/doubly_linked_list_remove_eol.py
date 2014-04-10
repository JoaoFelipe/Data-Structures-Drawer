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
from ds_drawer.shapes.null import Null
from ds_drawer.shapes.line import Line
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.viewer import viewer


RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw():
    [
        l, s, as3, e3, a31, a13, e1, a12, a21, e2, a2e, e
    ] = create_doubly_linked_list([3, 1, 2])
    circ = Circle((e.x + 40, e.y), "2", color=BLUE)
    ca12 = Cross(a12, color=RED)
    n = Null((a12.mx + 15, a12.my - 40), color=RED)
    desloc = lambda p, d: (p[0], p[1] + d)
    p = (a12.mx - 3, a12.my - 26)
    d1 = Line(p, n.middle, color=RED)
    d2 = Line(desloc(e1.prox_1, - 4), p, color=RED)
    c2 = Cross(e2.middle, color=RED, size=20)
    return [
        l, s, as3, e3, a31, a13, e1, a12, a21, e2, a2e, e,
        circ, ca12, n, d1, d2, c2
        
    ]


if __name__ == '__main__':
	viewer(draw)
