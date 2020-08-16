x,y,z = 1444,575,22
if x > y:
    max=x
    min=y
else:
    max=y
    min=x

if max < z:
    max=z
if min > z:
    min=z

print("the max:{}\n the min:{}".format(max, min))
