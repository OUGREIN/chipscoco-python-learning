'''
@author:chenzhan
@date:2020-08-16
前提：数据集合中的元素必须有序（升序or降序）
原理:每次查找中间位置再根据升序or降序来查找另一半区间
des:使用二分查找，查找有序列表
'''

# 使用递归的方式来实现二分查找
def binary_search_recursive(data,value):
    left,right = 0,len(data)-1
    def __search(left,right):
        if left <= right:
            mid = (left+right)//2
            if data[mid]==value:
                return  mid
            elif data[mid]>value:
                return __search(left,mid-1)
            else:
                return __search(mid+1,right)
        else:
            #如果该元素不在列表里，则返回-1
            return -1
    return  __search(left,right)

print(binary_search_recursive([1,2,3,4,5,6,7],7))


# 使用while循环实现二分查找
data = [1,2,3,4,5]
value = 3
def binary_search(data,value):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left+right)//2
        if data[mid] == value:
            return mid
        elif data[mid] > value:
            right= mid-1
        else:
            left = mid +1
print(binary_search(data,value))
