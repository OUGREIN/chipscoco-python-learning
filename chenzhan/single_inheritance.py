class Cat:
    __species = 'cat'
    @classmethod
    def catch_mice(cls):
        print("A cat that doesn't catch a mouse is not a godd cat!")

    def __init__(self,name):
        self.__name = name

class Babby(Cat):
    def __init__(self,name,weight):
        # 继承父类__name属性
        super().__init__("cat")
        # 扩展子类参数
        self.__name = name
        self.__weight = weight

    @classmethod
    def catch_mice(cls):
        super().catch_mice()
        print("babby is too fat to catch mice!")

    def eat(self):
        print(self.__name)
        # 由于父类构造函数里__name是封装的，访问不到，所以要加前缀
        print(self._Cat__name)

ketty = Babby('kitty',18)
ketty.catch_mice()
ketty.eat()