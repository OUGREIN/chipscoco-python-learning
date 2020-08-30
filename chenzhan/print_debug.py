def accumulate(*args):
    value = 0
    print('for loop start,value:{}'.format(value))
    for arg in args:
        print('value is:{} arg is:{}'.format(value,arg))
        value += arg
    print('for loop end,value:{}'.format(value))
    return value
result = accumulate(1,2,3)