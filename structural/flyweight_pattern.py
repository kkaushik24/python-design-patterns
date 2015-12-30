from abc import ABCMeta, abstractmethod
from random import randint


class Shape:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

    def __init__(self, color):
        self.color = color

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_radius(self, radius):
        self.radius = radius

    def draw(self):
        print "Circle: Draw color:{0} x:{1},y:{2},radius:{3}".format(self.color, self.x, self.y, self.radius)


class ShapeFactory:

    circle_dict = {}

    def get_circle(self, color):
        circle = ShapeFactory.circle_dict.get(color)
        if circle is None:
            circle = Circle(color)
            ShapeFactory.circle_dict.update({color: circle})
            print 'creating circle of color: ' + color

        return circle

# flyweight demo
if __name__ == '__main__':

    colors = ['red', 'green', 'blue', 'white', 'black']
    for color in colors:
        circle = ShapeFactory().get_circle(color)
        circle.set_x(randint(1, 10))
        circle.set_y(randint(1, 10))
        circle.set_radius(100)
        circle.draw()
