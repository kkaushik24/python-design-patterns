from abc import ABCMeta, abstractmethod
import copy


class ProtoType:
    __metaclass__ = ABCMeta

    @abstractmethod
    def clone(self):
        pass


class Circle(ProtoType):

    def __init__(self, radius):
        self.radius = radius

    def show_property(self):
        print 'radius of Circle is %s' % self.radius

    def clone(self):
        return copy.deepcopy(self)


class Square(ProtoType):

    def __init__(self, side):
        self.side = side

    def show_property(self):
        print 'side of Square is %s' % self.side

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':

    circle_a = Circle(12)
    # circle a property
    circle_a.show_property()
    circle_b = circle_a.clone()

    # circle b property
    circle_b.show_property()

    square_a = Square(20)
    # square a property
    square_a.show_property()
    square_b = square_a.clone()

    # square b property
    square_b.show_property()
