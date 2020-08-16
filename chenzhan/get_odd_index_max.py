'''
@author:chenzhan
@date:2020-08-16
des:用for循环打印出指定在列表中偶数最大值和其索引值
'''
list_number = [1,3,5,7,9]
odd_max = 0
index = 0
index_oddmax = -1
for number in list_number:
    if number % 2 == 0:
        if number> odd_max:
            odd_max = number
            index_oddmax = index
    index += 1

if index_oddmax != -1:
    print("最大的偶数为%d,索引值为%d" % (odd_max,index_oddmax))


