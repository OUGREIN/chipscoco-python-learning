class Cat:
    _species= "cat"
    @classmethod
    def catch_mice(cls):
        print("A cat that ")
    def __init__(self,name):
        self.__name,self.__foods,self.__index = name,[],0
    def feed(self, food):
        self.__foods.append(food)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__foods):
            food = self.__foods[self.__index]
            self.__index += 1
            return food
        self.__index = 0
        raise StopIteration
cat = Cat("kitty")
cat.feed("fish")
cat.feed("bread")
for food in cat:
    print(food)