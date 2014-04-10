from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from ds_drawer.shapes.null import Null
from ds_drawer.shapes.pointer import Pointer
from ds_drawer.shapes.linked_list import LinkedList
from ds_drawer.shapes.doubly_linked_list import DoublyLinkedList
from ds_drawer.shapes.arrow import Arrow
from ds_drawer.shapes.sub_arrow import SubArrow
from ds_drawer.shapes.line import Line


def empty_list(point, color=(0,0,0), label="l"):
    null = Null(point, color=color)
    pointer = Pointer(null, label, direction='l.middle', 
                      arrow=False, color=color)
    return [pointer, null]


def create_list(lis, create_element, create_arrows, x=50, y=100, 
        color=(0,0,0), label="l", space=30, none=60):

    result = []
    last = None
    for element in lis:
        if element is None:
            x += none
            continue

        current = create_element((x, y), element, color) 
        if last:
            result += create_arrows(last, current, color)
        result.append(current)

        x += current.width + space
        last = current

    null = Null((x - space // 2, y), color=color)
    line = Line(last.prox_2, null.middle, color=color)
    pointer = Pointer(result[0], label, direction='lu.start_0', color=color)
    return [pointer] + result + [line, null]


def create_linked_list(lis, x=50, y=100, color=(0,0,0), label="l", 
        space=30, none=60):
    
    if not lis:
        return empty_list((x + space // 2, y), color, label)

    return create_list(
        lis, 
        (lambda p, text, color: 
            LinkedList(p, text=text, color=color)
        ),
        (lambda last, current, color: [
            Arrow(last.prox_2, current.start_2, color=color)
        ]),
        x, y, color, label, space, none
    )


def create_circular_linked_list(lis, x=50, y=100, color=(0,0,0), label="l", 
        space=30, none=60):
    
    if not lis:
        return empty_list((x + space // 2, y), color, label)

    result = create_linked_list(lis, x, y, color, label, space, none)[:-2]
    return (
        result + 
        [SubArrow(result[-1].prox_3, result[1].start_3)]
    )


def create_doubly_linked_list(lis, x=50, y=100, color=(0,0,0), label="l", 
        space=30, none=60):
    
    if not lis:
        return empty_list((x + space // 2, y), color, label)

    null = Null((x + space // 2, y), color=color)
    result = create_list(
        lis, 
        (lambda p, text, color: 
            DoublyLinkedList(p, text=text, color=color)
        ),
        (lambda last, current, color: [
            Arrow(last.prox_1, current.start_1, color=color),
            Arrow(current.ant_3, last.end_3, color=color),
        ]),
        x + space, y, color, label, space, none
    )
    line = Line(result[1].ant_2, null.middle, color=color)
    return (
        [result[0], null, line] +
        result[1:]
    )


