'''
# 定义lion类，做为父类
class Lion:
    # 定义类熟悉species，表示lion所属的物种
    __species = "lion"
    # 类方法
    @classmethod
    def eat_meat(cls):
        print("A lion without meat is not a good lion")
# 定 littlelion类，表示小狮子继承lion
class Littlelion(Lion):
    pass


"""
(1) 通过类名()的方式来实例化一个对象：Littlelion()
()内需要传递与构造函数一致的参数，由于没有定义构造函数，所以Python会自动调用一个无参的构造函数
(2) 将实例化后的对象赋值给littlelion变量，那么littlelion就是实例化后的对象
"""
littlelion = Littlelion()
littlelion.eat_meat()
'''

'''
class Lion:
    __species = "lion"
    @classmethod
    def eat_meat(cls):
        print("A lion without meat is not a good lion")
    def __init__(self,name):
        self.__name = name



class Littlelion(Lion):
    def __init__(self, name, weight):
        super().__init__("rose")
        self.__name = name
        self.__weight = weight


littlelion = Littlelion("xinba", 320)
print(littlelion._Lion__name)
print(littlelion._Littlelion__name)
'''