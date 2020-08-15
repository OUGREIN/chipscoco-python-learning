# 指令的练习
'''
2020-8-8的指令练习
'''

# import sys 是导入数据模块
import sys
number = 55+55
print(number)

# 算数运算 True是布尔类型的真假判断 可以换算为整型的 1或者1.0
number = 10+0.5*2/23+True
# print函数用来输出表达式的值
print(number)

# 变量的定义 定义了一个字符串的变量，将一个字符串赋值给变量
name = "liaohaipeng"
full_name = name
print (id(full_name))

# 变量的定义 定义了一个整数类型的变量，将整数赋值给变量
car = 25
number_of_car = car
# 用函数print来查看内存地址
print(id(number_of_car),id(25))
# 用函数print来查看类型名
print(type(car),type(number_of_car))
# 用函数print来查看变量的内存大小
print(sys.getsizeof(car))

# 变量的定义 定义了布尔类型的变量，将True的真值赋值给变量
is_animal = True
is_beast = is_animal
# 用函数print来查看内存地址
print(id(is_animal),id(True))
# 用函数print输出来查看类型名
print(type(is_animal),type(is_beast))
# 用函数print输出来查看变量的内存大小
print(sys.getsizeof(is_animal))

vegetables = 2.3
greenstuff = vegetables
print(id(vegetables))
print(type(vegetables),type(greenstuff))
print(sys.getsizeof(vegetables))

