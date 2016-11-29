def myfun(x,y):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    return x+y


print myfun(6,1)
print "========="


def myfun2(x,y):
    return x,y,x-y,x+y

print myfun2(6,1)

a,b,c,d = myfun2(6,1)
print a
print b
print c
print d
print "========="


def myfun3(x,y=2):
    return x*y

print myfun3(6)
print myfun3(6,3)

