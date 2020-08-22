# 冒泡排序
# 两两之间进行比较，以升序或降序的方式调换元素的大小
# 两个变量两两比较--一次
# 三个变量两两比较--2次
# n个变量两两比较--n-1次（n>=2）

numbers=[_ for _ in range(22,0,-1)]

def bubble_sort(numbers):
    size = len(numbers)
    index = 0
    # size-1 比较的轮数，n个元素需要n-1轮比较
    while index < size -1:
        inner_index=0
        while inner_index < size-1-index:
            if numbers[inner_index] > numbers[inner_index+1]:
                numbers[inner_index],numbers[inner_index+1]=numbers[inner_index+1],numbers[inner_index]
            inner_index += 1

        index +=1

bubble_sort(numbers)
#print(numbers)

class Computer:
    subgroup = ["cpu","display","hd"]

    @classmethod
    def calculate(cls):
        print(cls.subgroup)

    @staticmethod
    def price(x,z,y):
        pass

#computer = Computer()
#computer.calculate()
#Computer.calculate()


class Cat:
    species = "cat"
    @classmethod
    def catch_mice(cls):
        print(cls.species)
    @staticmethod
    def cry():
        print("cat cry like a baby")

print(Cat.species)
Cat.catch_mice()
Cat.cry()

cat = Cat()
print(cat.species)
cat.catch_mice()
cat.cry()

