from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_linked_list
from ds_drawer.shapes.circle import Circle
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.viewer import viewer


RED = (255, 0, 0)


def draw():
    l, e1, a1_21, e21, a21_22, e22, a22_3, e3, a3n, n = create_linked_list(
        [1, 2, 2, 3])
    p = Pointer(e21, ' ', direction='u.u_2', color=RED)
    c = Circle((e21.mx + 4, e21.my - 2), "", radius=30, color=RED)
    return [
        l, e1, a1_21, e21, a21_22, e22, a22_3, e3, a3n, n,
        p, c
    ]


if __name__ == '__main__':
	viewer(draw)
