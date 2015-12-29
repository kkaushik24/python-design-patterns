from abc import ABCMeta, abstractmethod


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
