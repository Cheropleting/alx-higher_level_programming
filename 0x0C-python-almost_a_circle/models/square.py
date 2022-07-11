#!/usr/bin/python3
""" Model Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y,
                self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **keywords):
        """ update square with keyword args """
        i = 0
        if args:
            while i < len(args):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
                i += 1
        else:
            for arg in keywords:
                setattr(self, arg, keywords.get(arg))

    def to_dictionary(self):
        """ dictionary definition """
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
