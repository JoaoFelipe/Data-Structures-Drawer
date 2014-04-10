from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_linked_list
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.shapes.label import Label
from ds_drawer.viewer import viewer


def draw():
    l, e1, a12, e2, a23, e3, a3n, n = create_linked_list(["", "", None, ""])
    
    ellipsis = Label((a23.mx, a23.my), "...")
    a2e = Arrow(e2.prox_2,(a23.mx - 10, a23.my))
    ae3 = Arrow(ellipsis.nearest(e3.start_2), e3.start_2)
    return [
        l, e1, a12, e2, e3, a3n, n,
        ellipsis, a2e, ae3
    ]


if __name__ == '__main__':
    viewer(draw)
