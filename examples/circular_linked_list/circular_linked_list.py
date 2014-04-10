from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_circular_linked_list
from ds_drawer.viewer import viewer

def draw():
    return (
        create_circular_linked_list([]) +
        create_circular_linked_list([""], x=100)
    )


if __name__ == '__main__':
	viewer(draw)
