from abc import ABCMeta, abstractmethod

class Order:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def execute(self):
        pass


class Stock:
    __name__ = 'abc'
    __quantity__ = 10

    def buy(self):
        print "stock name:{0} quantity:{1} bought".format(__name__, __quantity__)

    def buy(self):
        print "stock name:{0} quantity:{1} sold".format(__name__, __quantity__)


class BuyStock(Order):
    
    def __init__(self, stock):
        self.__stock__ = stock

    def execute(self):
        self.__stock__.buy()


class SellStock(Order):

    def __init__(self, stock):
        self.__stock__ = stock
    
    def execute(self):
        self.__stock__.sell()


class Broker:

    def __init__(self):
        self.__order_list__ = []

    def take_order(self, order):
        orderList.append(order)

    def place_order(self):
        for order in self.__order_list__:
            order.execute()
        self.__order_list__ = []

if __name__ == '__main__':
    abc_stock = stock()
    buy_stock = BuyStock(abc_stock)
    sell_stock = SellStock(abc_stock)
    broker = Broker()
    broker.take_order(buy_stock)
    broker.take_order(sell_stock)
    broker.place_order()
