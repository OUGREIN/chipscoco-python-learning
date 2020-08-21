
# 2020123 
# 计算区间范围的极值，均值
# 思路：两两之间进行比较 --极值
# 相加求和再除以个数

count=0
numbers = [_ for _ in range(1000)]
sum_of_numbers=max=min=numbers[0]
for _ in numbers[1:]:
    count+=1
    max=max if max > _ else _
    min=min if min < _ else _
    sum_of_numbers += _
else:
    print("max:%d\nmin:%d" % (max,min))


