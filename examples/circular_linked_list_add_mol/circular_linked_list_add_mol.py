from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_circular_linked_list
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.linked_list import LinkedList
from ds_drawer.viewer import viewer


RED = (255, 0, 0)


def draw():
    l, e1, a12, e2, a23, e3, sa = create_circular_linked_list(
        ["", None, "", ""])
    c1 = Cross(a12, color=RED)
    en = LinkedList((e2.x - 60, e2.y - 40), "", color=RED)
    a1n = Arrow(e1.prox_1, en.start_4, color=RED)
    an2 = Arrow(en.prox_3, e2.start_0, color=RED)
    return [
        l, e1, a12, e2, a23, e3, sa,
        c1, en, a1n, an2,
    ]


if __name__ == '__main__':
	viewer(draw)
