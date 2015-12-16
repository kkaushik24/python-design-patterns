class Adaptee:
    
    def methodB(self):
        return 'B'


class Adaptor:

    adaptee = Adaptee()

    def mehodA(self):
        B = Adaptor.adaptee.methodB()
        return A+B


class Client:

    ataptor = Adaptor()

    def dowork(self):
        C = 'C'
        AB = adaptor.methodA()
        return AB + C



