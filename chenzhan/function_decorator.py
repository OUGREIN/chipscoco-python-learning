def filter(func):
    def filter_(*args):
        numbers = []
        for _ in args:
            if _ > 2:
                numbers.append(_)
        func(numbers)
    return filter_

@filter
def demo(*args):
    print(args)


demo(0,1,2,3,5)
