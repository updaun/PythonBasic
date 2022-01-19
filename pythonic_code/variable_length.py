# *args
def asterisk_test(a, b, *args):
    print(list(args))
    print(type(args))
    return a+b+sum(args)

print(asterisk_test(1,2,3,4,5))

# **kwargs

def kwargs_test_1(**kwargs):
    print(kwargs)
    print(type(kwargs))

kwargs_test_1(first=3, second=4, third=5)

def kwargs_test_2(**kwargs):
    print(kwargs)
    print("first:{first}".format(**kwargs))
    print("second:{second}".format(**kwargs))
    print("third:{third}".format(**kwargs))

kwargs_test_2(first=3, second=4, third=5)

def kwargs_test_3(one, two, *args, **kwargs):
    print(one+two+sum(args))
    print(kwargs)

kwargs_test_3(3,4,5,6,7,8,9, first=3, second=4, third=5)


# unpacking a container
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1, *(2,3,4,5,6))

def asterisk_test_a(a, *args):
    print(a, args)
    print(type(args))

asterisk_test_a(1, (2,3,4,5,6))

# unpacking
print(['1','2','3','4'])
print(*['1','2','3','4'])
