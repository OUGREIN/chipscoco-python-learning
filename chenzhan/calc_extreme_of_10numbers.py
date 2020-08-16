"""
@author:chenzhan
@date:2020-08-16
desc:求两个数值型变量的极值
"""
numbers = [3,4,5,6,7,13,7,110,33,-7]
# 先定义列表其中一个元素为变量最值
max = min = numbers[0]
for number in numbers:
    max = max if max>number else number
    min = min if min<number else number
else:
    print("最大值为：%d/n最小值为：%d"%(max,min))