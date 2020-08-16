'''
@author：liaohaipeng
@date: 2020-8-16
@desc:  对比字典与列表的查找性能
'''

import time

numbers = []
container = {}
for _ in range(1,1000000):
    numbers.append(_)
    container[_]=_
start = time.perf_counter()
_ = 1000000 in numbers
end = time.perf_counter()
print("使用列表查找所消耗的时间{}".format(end - start))

start = time.perf_counter()
_ = 1000000 in container
end = time.perf_counter()
print("使用字典查找所消耗的时间{}".format(end - start))
