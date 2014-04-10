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


def draw():
    l, e0, a03, e3, a32, e2, a2n, n = create_linked_list([0, 3, 2])
    sa = SubArrow(e2.prox_2, e0.start_2)
    ant0 = Pointer(e0, 'ant', direction='d.d_2', color=RED, dist=25)
    p0 = Pointer(e0, 'p', direction='u.u_2', color=RED)
    ant3 = Pointer(e3, 'ant', direction='d.d_2', color=RED, dist=25)
    p3 = Pointer(e3, 'p', direction='u.u_2', color=RED)
    ant2 = Pointer(e2, 'ant', direction='d.d_2', color=RED, dist=25)
    p2 = Pointer(e2, 'p', direction='u.u_2', color=RED)
    circ = Circle((n.x + 40, n.y), "1", color=BLUE)
    
    cant0 = Cross(ant0.label, color=RED)
    cant3 = Cross(ant3.label, color=RED)
    cp3 = Cross(p3.label, color=RED)
    cp2 = Cross(p2.label, color=RED)

    c = Cross((a03.mx, a03.my - 10), size=10, color=RED)

    return [
        l, e0, a03, e3, a32, e2, sa, circ,
        ant0, ant3, ant2, p0, p3, p2,
        cant0, cant3, cp3, cp2, c
    ]

if __name__ == '__main__':
	viewer(draw)
