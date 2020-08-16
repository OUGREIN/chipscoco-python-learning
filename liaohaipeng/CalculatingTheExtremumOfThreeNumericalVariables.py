'''
@author：liaohaipeng
@date: 2020-8-16
@desc:  计算三个数值型变量的极值
'''
x,y,z = 1,2,3
# 如果x大于y，最大值为x。最小值为y
if x > y:
    max=x
    min=y
else:
    max=y
    min=x
if max < z:
    max=z
if min > z:
    min=z