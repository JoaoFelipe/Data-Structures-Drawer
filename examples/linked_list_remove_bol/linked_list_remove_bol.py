from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_linked_list
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.viewer import viewer


RED = (255, 0, 0)


def draw():
    l, e1, a12, e2, a23, e3, a3n, n = create_linked_list([1, 2, 3])
    cl = Cross(l.arrow, color=RED)
    c1 = Cross(e1.middle, color=RED, size=20)
    l2 = Pointer(e2, 'l', direction='lu.start_0', color=RED)
    return [
    	l, e1, a12, e2, a23, e3, a3n, n,
        cl, c1, l2
    ]


if __name__ == '__main__':
	viewer(draw)
