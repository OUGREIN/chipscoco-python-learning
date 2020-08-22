class Language:
    # 类属性
    __genre = ["java","c++","python"]
    # 类方法
    @classmethod
    def __write(cls):
        print("调用类方法:write， 访问类属性:{}".format(cls.__genre))



    # 静态方法需要显式地传递参数
    @staticmethod
    def __readable(cls):
        print("调用静态方法:readable, 访问类属性:{}".format(cls._Language__genre))
    # 构造属性
    def __init__(self,version):
        print("Python自动调用构造函数:__init__")
        self.version=version


class  Amount(Language):
       pass
#print(Lnguage.genre)
#Language.write()
#Language.readable(Language)
#language = Language("Python")
# print(language.version)

Language._Language__write()
print(Language._Language__genre)
Language._Language__readable(Language)