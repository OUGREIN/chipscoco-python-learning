'''
@author:chenzhan
@date:2020-08-16
des:用for循环打印出指定在列表中最大值和最大值的索引值
'''
list_number = [1,10,2,45,8,9,20]
max = 0
index = 0
index_max = 0
for number in list_number:
    if number>max:
        max = number
        index_max = index
    index += 1
print("最大值为%d,索引为%d" % (max,index_max))



