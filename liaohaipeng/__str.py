class Cat:
    __species = "cat"
    def __init__(self, name):
        self.__name = name
    def __str__(self):
        return "333333"
cat = Cat("kitty")
print(cat)
