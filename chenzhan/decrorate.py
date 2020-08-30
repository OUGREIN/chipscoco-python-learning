'''
def count_backwards(number):
    if number>0:
        print(number)
        number-=1
        count_backwards(number)
count_backwards(10)
'''
'''
def decorator(func):
    def clousre(*args, **kwargs):
        for _ in args:
            if not isinstance(_,(int, float, bool)):
                print("illegal")
                break
        else:
            func(*args, **kwargs)
    return clousre


@decorator
def sum_(x):
   print(x)

sum_(5)
'''


'''
def decorator(types):
    def closure_outer(func):
        def closure_inner(*args,**kwargs):
            for _ in args:
                if not isinstance(_, types):
                    print("illegal")
                    break
            else:
                func(*args, **kwargs)
        return closure_inner
    return  closure_outer



@decorator((int, float, str))
def sum_(x):
    print(x)

sum_((1,2,4))
'''

x = 1
y =2
a = {"add":lambda x,y:x+y,"sub":lambda x,y:x-y}
b = a['add'](1,2)
print(b)





















