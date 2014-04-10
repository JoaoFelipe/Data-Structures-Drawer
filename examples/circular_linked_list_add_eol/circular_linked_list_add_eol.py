from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_linked_list
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.shapes.sub_arrow import SubArrow
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.linked_list import LinkedList
from ds_drawer.viewer import viewer


RED = (255, 0, 0)


def draw():
    l, e8, a8n, n = create_linked_list([8])
    sa = SubArrow(e8.prox_2, e8.start_2)
    c1 = Cross(sa, color=RED)
    e5 = LinkedList((n.x + 30, e8.y), 5, color=RED)
    a85 = Arrow(e8.prox_1, e5.start_1, color=RED)
    sa2 = SubArrow(e5.prox_3, e8.start_1, color=RED, size_x2=20)
    return [
        l, e8, sa, 
        c1, e5, a85, sa2
    ] 


if __name__ == '__main__':
	viewer(draw)
