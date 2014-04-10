from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys
import os
sys.path.append(os.path.join("..", ".."))

from ds_drawer.generators.lists import create_doubly_linked_list
from ds_drawer.viewer import viewer


def empty():
	return create_doubly_linked_list([])


def one_element():
	return create_doubly_linked_list([1], x=100)


def two_elements():
	return create_doubly_linked_list([2, 1], y=200)


def three_elements():
	return create_doubly_linked_list([2, 1, 3], y=300)


def draw():
    return empty() + one_element() + two_elements() + three_elements()


if __name__ == '__main__':
	viewer(draw)
