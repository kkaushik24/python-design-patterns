from abc import ABCMeta, abstractmethod


class Shape():
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):

    def draw(self):
        print 'In Rectangle'


class Square(Shape):

    def draw(self):
        print 'In Square'


class Circle(Shape):

    def draw(self):
        print 'In Circle'


class Color():
    __metaclass__ = ABCMeta

    @abstractmethod
    def fill(self):
        pass


class Red(Color):

    def fill(self):
        print 'Fill Red'


class Green(Color):

    def fill(self):
        print 'Fill Green'


class Blue(Color):

    def fill(self):
        print 'Fill Blue'


class AbstractFactory():
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_color(self, color_type):
        pass

    @abstractmethod
    def get_shape(self, shape_type):
        pass


class ColorFactory(AbstractFactory):

    def get_color(self, color_type):
        if color_type == 'RED':
            red = Red()
            return red
        if color_type == 'GREEN':
            green = Green()
            return green
        if color_type == 'BLUE':
            blue = Blue()
            return blue

    def get_shape(self, shape_type):
        return


class ShapeFactory(AbstractFactory):

    def get_color(self, color_type):
        return

    def get_shape(self, shape_type):
        if shape_type == 'RECTANGLE':
            rectangle = Rectangle()
            return rectangle

        if shape_type == 'SQUARE':
            square = Square()
            return square
        if shape_type == 'CIRCLE':
            circle = Circle()
            return circle


class FactoryProducer():

    def get_factory(self, choice):
        if choice == 'SHAPE':
            return ShapeFactory()
        if choice == 'COLOR':
            return ColorFactory()


# Abstract Factory Demo
if __name__ == '__main__':
    shape_factory = FactoryProducer().get_factory('SHAPE')
    color_factory = FactoryProducer().get_factory('COLOR')

    # shapes
    rectangle = shape_factory.get_shape('RECTANGLE')
    rectangle.draw()
    square = shape_factory.get_shape('SQUARE')
    square.draw()
    circle = shape_factory.get_shape('CIRCLE')
    circle.draw()

    # colors
    red = color_factory.get_color('RED')
    red.fill()
    blue = color_factory.get_color('BLUE')
    blue.fill()
    green = color_factory.get_color('GREEN')
    green.fill()
