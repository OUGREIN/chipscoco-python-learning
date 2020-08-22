# 冒泡排序
# 两两之间进行比较，以升序或降序的方式调换元素的大小
# 两个变量两两比较--一次
# 三个变量两两比较--2次
# n个变量两两比较--n-1次（n>=2）

numbers=[_ for _ in range(10,0,-1)]
size = len(numbers)
index = 0
# size-1 比较的轮数，n个元素需要n-1轮比较
while index < size -1:
    inner_index=0
    while inner_index < size-1-index:
        if numbers[inner_index] > numbers[inner_index+1]:
            numbers[inner_index],numbers[inner_index+1]=numbers[inner_index+1],numbers[inner_index]
    index +=1
print(numbers)