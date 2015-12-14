from abc import ABCMeta, abstractmethod

class Item():
    __metaclass__ = ABCMeta

    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def packing(self):
        pass
    
    @abstractmethod
    def price(self):
        pass


class Packing():
    __metaclass__ = ABCMeta

    @abstractmethod
    def pack(self):
        pass


class Wrapper(Packing):

    def pack(self):
        return 'Wrapper'


class Bottle(Packing):

    def pack(self):
        return 'Bottle'


class Burger(Item):

    def packing(self):
        return Wrapper()


class ColdDrink(Item):
    
    def packing(self):
        return Bottle()



class VegBurger(Burger):
    
    def name(self):
        return 'VegBurger'

    def price(self):
        return 25


class ChickenBurger(Burger):

    def name(self):
        return 'ChickenBruger'

    def price(self):
        return 50


class Coke(ColdDrink):

    def name(self):
        return 'Coke'

    def price(self):
        return 10


class Pepsi(ColdDrink):

    def name(self):
        return 'Pepsi'

    def price(self):
        return 20


class Meal():

    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)

    def get_cost(self):
        total_cost = 0
        for item in self.item_list:
            total_cost = total_cost + item.price()
        return total_cost

    def show_items(self):
        print 'name packing cost'
        for item in self.item_list:
            print item.name(), item.packing().pack(), item.price()


class MealBuilder():

    def prepare_veg_meal(self):
        meal = Meal()
        meal.add_item(VegBurger())
        meal.add_item(Coke())

        return meal

    def prepare_nonveg_meal(self):
        meal = Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())

        return meal


if __name__ == "__main__":

    meal_builder = MealBuilder()
    veg_meal = meal_builder.prepare_veg_meal()
    print 'veg meal'
    veg_meal.show_items()
    print veg_meal.get_cost()

    nonveg_meal = meal_builder.prepare_veg_meal()
    print 'nonveg meal'
    nonveg_meal.show_items()
    print nonveg_meal.get_cost()
