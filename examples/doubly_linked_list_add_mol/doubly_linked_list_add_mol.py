from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_doubly_linked_list
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.doubly_linked_list import DoublyLinkedList
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.shapes.circle import Circle
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.viewer import viewer


RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw():
    [
    	l, s, as1, e1, a13, a31, e3, a34, a43, e4, a4e, e
    ] = create_doubly_linked_list([1, None, 3, 4])
    ca21 = Cross(a13, color=RED)
    ca12 = Cross(a31, color=RED)
    e2 = DoublyLinkedList((e3.x - 70, e3.y + 40), 2, color=RED)
    a12 = Arrow(e1.prox_3, e2.start_0, color=RED)
    a21 = Arrow(e2.ant_2, e1.d_3, color=RED)
    a23 = Arrow(e2.prox_2, e3.d_1, color=RED)
    a32 = Arrow(e3.ant_3, e2.u_4, color=RED)
    circ = Circle((e.x + 40, e.y), "2", color=BLUE)
    p1 = Pointer(e1, 'p', direction='u.u_2', color=RED)
    p3 = Pointer(e3, 'p', direction='u.u_2', color=RED)
    cp1 = Cross(p1.label, color=RED)
    return [
        l, s, as1, e1, a13, a31, e3, a34, a43, e4, a4e, e,
        circ, ca21, ca12, e2, a12, a21, a23, a32, p1, p3, cp1
    ]


if __name__ == '__main__':
	viewer(draw)
