"""
@author:chenzhan
@date:2020-08-16
desc:求两个数值型变量的极值
"""
x = 1
y = 2
'''
#使用三元运算符解决
max = x if x>y else y
min = y if y<x else x
'''

# 先定义变量存储其中一个数的值作为初始值
min = max = x
# 直接进行关系比较，得出最大值，最小值
if min <= y:
    min = x
    max = y
print("最大值:%d\n最小值:%d" % (max, min))




