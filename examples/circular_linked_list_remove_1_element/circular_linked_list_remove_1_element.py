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


def ok():
    l, e3, a3n, n = create_linked_list([3])
    sa = SubArrow(e3.prox_2, e3.start_2)
    c3 = Cross(e3, color=RED, size=20)
    circ = Circle((n.x + 40, n.y), "3", color=BLUE)
    return [
        l, e3, sa,
        c3, circ
    ]


def fail():
    l, e2, a2n, n = create_linked_list([2], y=200)
    sa = SubArrow(e2.prox_2, e2.start_2)
    circ = Circle((n.x + 40, n.y), "3", color=BLUE)
    return [
        l, e2, sa,
        circ
    ]

def draw():
    return ok() + fail()


if __name__ == '__main__':
	viewer(draw)
