class Cat:
    __species = 'Cat'
    def __init__(self,name):
        self.__name = name

    def __str__(self):
        return "这是一个描述"

cat = Cat('kitty')
print(cat)