from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_linked_list
from ds_drawer.viewer import viewer


def draw():
    return create_linked_list([])


if __name__ == '__main__':
	viewer(draw)
