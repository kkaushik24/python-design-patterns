class Graphic:

    def print_(self):
        raise NotImplementedError


class CompositeGraphic(Graphic):

    def __init__(self):
        self.child_graphics = []

    def add(self, graphic):
        self.child_graphics.append(graphic)

    def remove(self, graphic):
        try:
            self.child_graphics.remove(graphic)
        except:
            pass

    def print_(self):
        for graphic in self.child_graphics:
            graphic.print_()


class Ellipse(Graphic):

    def print_(self):
        print "Ellipse"


class Circle(Graphic):

    def print_(self):
        print "Circle"


class Square(Graphic):

    def print_(self):
        print "Square"


if __name__ == '__main__':

    ellipse = Ellipse()
    circle = Circle()
    square = Square()

    composite_graphic = CompositeGraphic()
    composite_graphic1 = CompositeGraphic()
    composite_graphic2 = CompositeGraphic()

    composite_graphic1.add(ellipse)
    composite_graphic1.add(circle)

    composite_graphic2.add(square)

    composite_graphic.add(composite_graphic1)
    composite_graphic.add(composite_graphic2)

    composite_graphic.print_()
