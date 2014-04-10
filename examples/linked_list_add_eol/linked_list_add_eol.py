from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_linked_list
from ds_drawer.shapes.cross import Cross
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.viewer import viewer


RED = (255, 0, 0)


def draw():
    l, e2, a2n, n = create_linked_list([2])
    ca2n = Cross(a2n, color=RED)
    _, e4, a4n2, n2 = create_linked_list(
    	[4], 
    	x=e2.x + e2.width + 15,
    	y=e2.y + 40,
    	color=RED
    )
    a24 = Arrow(e2.prox_3, e4.start_1, color=RED)
    return [
    	l, e2, a2n, n,
    	ca2n, e4, a4n2, n2,
    	a24
    ]


if __name__ == '__main__':
	viewer(draw)
