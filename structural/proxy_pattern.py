from abc import ABCMeta, abstractmethod


class Image:
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self):
        pass


class RealImage(Image):

    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def display(self):
        print 'displaying' + self.filename

    def load_from_disk(self):
        print 'loading' + self.filename


class ProxyImage(Image):

    real_image = None

    def __init__(self, filename):
        self.filename = filename

    def display(self):
        if ProxyImage.real_image is None:
            real_image = RealImage(self.filename)
            ProxyImage.real_image = real_image
        ProxyImage.real_image.display()

# demo for proxy pattern
if __name__ == '__main__':

    image = ProxyImage('proxy_pattern.jpg')
    # image will be loaded
    image.display()

    # image will not be loaded
    image.display()
