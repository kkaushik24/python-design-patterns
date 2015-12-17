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
        self.drawing_api = DrawingApi()

    def draw(self):
        pass

    def resize_by_percentage(pct):
        pass

