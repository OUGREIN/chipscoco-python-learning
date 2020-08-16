'''
@author：liaohaipeng
@date: 2020-8-16
@desc:  计算10个数值型变量的极值
'''
# 思路:量量之间进行比较
numbers=[3,4,5,6,7,13,7,110,33,-7]
max=min=numbers[0]
for number in numbers:
    max = max if max > number else number
    min = min if min < number else number
else:
    print("最大值:%d\n最小值:%d" % (max, min))

numbers=[3,4,5,6,7,13,7,110,33,-7]




