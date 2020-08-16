'''
@author:chenzhan
@date:2020-08-16
des:用for循环打印出指定变量在列表中的索引值
'''
list_number = [1,3,5,8,2]
number = 100
index = -1

for _ in list_number:
    index += 1
    if _ == number:
        break
else:
    index = -1

print(index)






