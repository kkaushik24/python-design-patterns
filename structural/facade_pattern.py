from abc import ABCMeta, abstractmethod


class Shape:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):

    def draw(self):
        print 'draw rectangle'


class Square(Shape):

    def draw(self):
        print 'draw square'


class Circle(Shape):

    def draw(self):
        print 'draw circle'


class ShapeMaker():

    def __init__(self):
        self.rectangle = Rectangle()
        self.square = Square()
        self.circle = Circle()

    def draw_square(self):
        self.square.draw()

    def draw_circle(self):
        self.circle.draw()

    def draw_rectangle(self):
        self.rectangle.draw()

if __name__ == '__main__':
    shape_maker = ShapeMaker()
    shape_maker.draw_rectangle()
    shape_maker.draw_circle()
    shape_maker.draw_square()
