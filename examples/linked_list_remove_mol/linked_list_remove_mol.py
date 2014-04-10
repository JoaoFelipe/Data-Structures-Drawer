from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_linked_list
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.shapes.sub_arrow import SubArrow
from ds_drawer.shapes.label import Label
from ds_drawer.viewer import viewer


RED = (255, 0, 0)


def draw():
    l, e1, a12, e2, a23, e3, a3n, n = create_linked_list([1, 2, 3])
    ant = Pointer(e1, 'ant', direction='d.d_2', color=RED)
    p1 = Pointer(e1, 'p', direction='u.u_2', color=RED)
    c1 = Cross(p1.arrow, color=RED)
    c2 = Cross(e2.middle, color=RED, size=20)
    c3 = Cross(a12, color=RED)
    p2 = Pointer(e2, 'p', direction='u.u_2', color=RED)
    sa = SubArrow(e1.prox_3, e3.start_3, color=RED)
    lab = Label((sa.mx, sa.my+20), "ant->prox = p->prox", color=RED)
    return [
        l, e1, a12, e2, a23, e3, a3n, n,
        c1, c2, c3, p1, p2, ant, sa, lab
    ]


if __name__ == '__main__':
    viewer(draw)
