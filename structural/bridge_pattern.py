from abc import ABCMeta, abstractmethod

class DrawingApi:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def draw_circle(x, y, radius):
        pass


class DrawingApi1(DrawingApi):

    def draw_circle(x, y, radius):
        print "Api1 ",x,y,radius


class DrawingApi2(DrawingApi):

    def draw_circle(x, y, radius):
        print "Api1 ",x,y,radius


class Shape:
    __metaclass__ = ABCMeta

    def __init__(self, drawing_api):
        self.drawing_api = DrawingApi

    def draw(self):
        pass

    def resize_by_percentage(pct):
        pass

class CircleShape(Shape):

    def __init__(self,x, y, radius, drawing_api):
        super(CircleShape,self).__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x,self.y, self.radius)

    def resize_by_percentage(self, pct):
        self.radius = self.radius + (self.radius * pct / 100)

if __name__ == '__main__':

    circle_shape1 = CircleShape(1,2,4,DrawingApi1())
    circle_shape2 = CircleShape(4,8,12,DrawingApi2())
    circle_shape1.draw()
    circle_shape2.draw()



