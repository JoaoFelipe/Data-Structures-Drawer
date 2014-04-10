from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_linked_list
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.shapes.linked_list import LinkedList
from ds_drawer.viewer import viewer


RED = (255, 0, 0)


def draw():
    l, e1, a13, e3, a35, e5, a5n, n = create_linked_list([None, 1, 3, 5])
    # Add 0
    e0 = LinkedList((e1.x - 40, e1.y + 40, 0), 0, color=RED)
    a01 = Arrow(e0.prox_1, e1.start_4, color=RED)
    novo = Pointer(e0, 'novo', direction='ul.start_0', color=RED)

    return [
    	l, e1, a13, e3, a35, e5, a5n, n,
        e0, novo, a01
    ]


if __name__ == '__main__':
	viewer(draw)
