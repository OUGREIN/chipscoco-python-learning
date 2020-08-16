"""
@author:chenzhan
@date:2020-08-16
desc:求两个数值型变量的极值
"""
##思路： 两两之间进行比较，求出极值
x,y,z = 1,2,3
if x>y:
    max = x
    min = y
else:
    max = y
    min = x
if z>max:
    max = z
if z<min:
    min = z
print("最大值:%d\n最小值:%d" % (max, min))