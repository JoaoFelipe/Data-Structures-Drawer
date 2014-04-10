from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


class Point(object):

    def __init__(self, x, y=None):
        if isinstance(x, tuple):
            self.x, self.y = x
        self.x = x
        self.y = y

    def __getitem__(self, index):
        return [self.x, self.y][index]

    @property
    def mx(self):
        return self.x

    @property
    def my(self):
        return self.y

    @property
    def middle(self):
        return (self.mx, self.my)

    @property
    def point(self):
        return (self.x, self.y)
