#求0到1000的合数的和是多少

sum = 0
for number in range(2,20):
    for _ in range(2,number):
        if number%_ == 0:
            sum+=number
            print(number)
            #判断能够整除就直接终结循环
            break
print(sum)


sum=0
number = 2
while number < 20:

    number2 = 2
    while number2 < number:

        if number%number2== 0:
            sum+=number
            print(number)
            break
        #在第二个while循环最后面进行更新number2
        number2 += 1
    #在第一个while循环最下面进行更新number
    number += 1

print(sum)


