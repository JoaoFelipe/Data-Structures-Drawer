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
from ds_drawer.viewer import viewer


RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw():
    l, e2, a24, e4, a4n, n = create_linked_list([None, 2, None, 4])
    # Add 0
    cl = Cross(l, color=RED)
    e0 = LinkedList((e2.x - 40, e2.y + 40, 0), 0, color=RED)
    a02 = Arrow(e0.prox_1, e2.start_4, color=RED)
    l0 = Pointer(e0, 'l', direction='ul.start_0', color=RED)
    # Add 3
    ca24 = Cross(a24, color=BLUE)
    e3 = LinkedList((e4.x - 60, e4.y + 40, 0), 3, color=BLUE)
    a23 = Arrow(e2.prox_3, e3.start_0, color=BLUE)
    a34 = Arrow(e3.prox_1, e4.start_4, color=BLUE)
   
    ant = Pointer(e2, 'ant', direction='u.u_2', color=BLUE)
    pp = Pointer(e4, 'p', direction='u.u_2', color=BLUE)
    novo = Pointer(e3, 'novo', direction='d.d_2', color=BLUE)

    return [
    	l, e2, a24, e4, a4n, n,
    	cl, e0,  a02, l0,
        ca24, e3, a23, a34,
        ant, pp, novo
    ]


if __name__ == '__main__':
	viewer(draw)
