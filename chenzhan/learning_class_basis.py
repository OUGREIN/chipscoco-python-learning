class Cat:
    @classmethod
    def catch(cls):
        print('1')
    def eat(self):
        print("2")

class HouseCat(Cat):
    def __init__(self, name):
        self.__name = name
        print("猫名字是：",name)


HouseCat.catch()

house_cat=HouseCat("kitty")

house_cat.eat()

