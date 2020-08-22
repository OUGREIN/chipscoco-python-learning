class People:
    # 类属性
    __species = ["eyes","hair","hands"]
    @classmethod
    def speak(cls):
        # python会自动地将cls绑定为类类型
        print(cls.__species)

    @staticmethod
    def __say():
       print("sound")

    def __init__(self, name):
        # 定义对象属性
        # python自动地将self绑定为当前对象
        self.name = name
        self.__say()
        print(self.__species)



class BadPeople(People):
    # pass是一个空语句，相当于一个占位符
    pass

# 类名+(参数列表)的方式构造对象，构造过程中会自动调用__init__函数
# haipeng = People("海鹏")
#print(haipeng._People__species)

# badpeople = BadPeople("特朗普")
# print(badpeople._People__species)

class DregsMan(BadPeople):
    pass

print(DregsMan.__mro__)