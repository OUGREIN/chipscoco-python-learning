'''
@author：liaohaipeng
@date: 2020-8-16
@desc:  求两个数值型变量的极值
'''
# 直接进行关系比较，得出最大值、最小值

x = 55244443
y = 5444422
z = 6144
max = x if x > y else y
max = z if max < z else max

min = x if x < y else y
min = z if min > z else min

print("最大值:%d\n最小值：%d" % (max,min))