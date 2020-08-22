"""
@author:chenzhan
@date:2020-08-22
desc:冒泡排序
"""

def bubble_sort(numbers):
    size = len(numbers)
    index = 0
    while index < size -1 :
        inner_index = 0
        while inner_index<size-1-index:
            if numbers[inner_index]>numbers[inner_index+1]:
                numbers[inner_index],numbers[inner_index+1]=numbers[inner_index+1],numbers[inner_index]
            inner_index+=1
        index += 1


numbers = [0,5,7,3,4,9]
bubble_sort(numbers)
print(numbers)





