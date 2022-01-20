from re import X

from click import argument


def square(x):
    return x*x

def cube(x):
    return x*x*x

def formula(method, argument_list):
    return [method(value) for value in argument_list]

f = square
print(f(5))


# Inner fucntion
def print_msg(msg):
    # 내제 함수
    def printer():
        print(msg)
    printer()

print_msg("Hello, Python Inner fucntion!")

def print_msg_2(msg):
    # 내제 함수
    def printer():
        print(msg)
    return printer

another = print_msg_2("Hello, Python printer return")
another()
# closures : inner fucntion을 return값으로 반환

# 클로저 활용 예제

def tag_func(tag, text):
    text = text
    tag = tag
    def inner_func():
        return '<{0}>{1}<{0}>'.format(tag, text)
    return inner_func

h1_func = tag_func("title", "This is Python Class")
p_func = tag_func("p", "AI, ML, DL, BigData")

# decorator function
def star(func):
    def inner(*args, **kwargs):
        print("*"*30)
        func(*args, **kwargs)
        print("*"*30)
    return inner

@star
def star_printer(msg):
    print(msg)

star_printer("Hello")

def mark(func):
    def inner(*args, **kwargs):
        print(args[1]*30)
        func(*args, **kwargs)
        print(args[1]*30)
    return inner

@star
@mark
def star_printer(msg, mark):
    print(msg)

star_printer("Hello", "%")


def generate_power(exponent):
    def wrapper(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return wrapper

@generate_power(2)
def raise_two(n):
    return n**2

print(raise_two(7))

print(2**49)