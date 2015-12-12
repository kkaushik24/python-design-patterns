# factory pattern
from abc import ABCMeta, abstractmethod


class Shape():
    __metaclass__ = ABCMeta

    @abstractmethod
    def shape(self):
        pass


class Circle(Shape):
    def shape(self):
        print "Inside Circle"


class Square(Shape):
    def shape(self):
        print 'Inside Square'


class ShapeFactory():
    def get_shape(self, shape_type):
        if shape_type == 'CIRCLE':
            return Circle
        if shape_type == 'SQUARE':
            return Square


if __name__ == '__main__':
    shape_factory = ShapeFactory()
    shape_circle = shape_factory.get_shape('CIRCLE')
    shape_square = shape_factory.get_shape('SQUARE')
    shape_circle().shape()
    shape_square().shape()
