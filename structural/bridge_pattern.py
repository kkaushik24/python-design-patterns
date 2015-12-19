from abc import ABCMeta, abstractmethod


class DrawingApi:
    def draw_circle(self, x, y, radius):
        pass


class DrawingApi1(DrawingApi):

    def draw_circle(self, x, y, radius):
        print "Api1 ", x, y, radius


class DrawingApi2(DrawingApi):

    def draw_circle(self, x, y, radius):
        print "Api1 ", x, y, radius


class Shape:
    __metaclass__ = ABCMeta

    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize_by_percentage(pct):
        pass


class CircleShape(Shape):

    def __init__(self, x, y, radius, drawing_api):
        super(CircleShape, self).__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize_by_percentage(self, pct):
        self.radius = self.radius + (self.radius * pct / 100)
        return self.radius

if __name__ == '__main__':
    drawing_api1 = DrawingApi1()
    drawing_api2 = DrawingApi2()
    circle_shape1 = CircleShape(1, 2, 4, drawing_api1)
    circle_shape2 = CircleShape(4, 8, 12, drawing_api2)
    circle_shape1.draw()
    print 'resized circle1 radius', circle_shape1.resize_by_percentage(40)
    circle_shape2.draw()
    print 'resized circle2 radius', circle_shape2.resize_by_percentage(50)
