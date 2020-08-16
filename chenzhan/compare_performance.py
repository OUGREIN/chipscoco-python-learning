'''
@author:chenzhan
@date:2020-08-16
des:比较字典与列表的执行性能
'''
#导入time模块，执行time模块中的perf_counter方法来获取程序的执行时间

import time
numbers = []
container = {}

#使用for循环结构，分别往列表和字典中，添加1百万个数据
for _ in range(1,1000000):
    numbers.append(_)
    container[_]=_

#获取查找前的时间
start = time.perf_counter()
_ = 1000000 in numbers
#获取查找后的时间
end = time.perf_counter()
#end-start就为查找过程中所耗费的查询时间
print("使用列表查找所消耗的时间{}".format(end-start))
start = time.perf_counter()
_ =1000000 in container
end = time.perf_counter()
print("使用字典查找所消耗的时间{}".format(end-start))
