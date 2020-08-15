# __author__ = chenzhan@chipscoco.com
# __date__ =  2020-08-08
#此文档代码用来练习循环语句
x = 155
y = 154
z = 1
if x > z + y :
    print('x > y')
elif x < z + y:
    print('x <= y')
else:
    print('x = y + z')

# 判断a,b,c 三个变量中的最大值和最小值
a = 4
b = 3
c = -5
if a>b:
    # 取一个中间变量进行比较大小
    max = a
    min = b
else:
    max = b
    min = a

if max<c:
    max = c
print('最大值为：',max)

if min>c:
    min = c
print('最小值为：',min)


#当if后面是假值时，不执行if下面的代码
is_happy = 0
if is_happy:
    print('是真值')
else:
    print('是假值')

is_happy = False
if is_happy:
    print('是真值')
else:
    print('是假值')

is_happy = None
if is_happy:
    print('是真值')
else:
    print('是假值')

is_happy = 0.0
if is_happy:
    print('是真值')
else:
    print('是假值')

#三元运算符
x = 12
y = 22
z = 99
the_max= x if x>y else y
print(the_max)
the_max= the_max if the_max>y else z
print(the_max)

counter = 0
# for循环语句
for number in 1,2,3,4,5:
    print('number',number)
    counter = counter + 1
    if counter > 3:
        break
else:
    print('正常退出')

#for循环于range类型配合使用
for number in range(1,101):
    print('number',number)
else:
    print('正常退出')
for number in range(100):
    print('number',number)
else:
    print('正常退出')

