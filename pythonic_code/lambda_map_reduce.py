f = lambda x,y: x+y
print(f(1,4))
print((lambda x,y: x+y)(10, 50))

up_low = lambda x : "-".join(x.split())
print(up_low("My Happy"))

# map
ex = [1,2,3,4,5]
f = lambda x : x**2
print(list(map(f, ex)))

print([f(value) for value in ex])

print(list(map(lambda x:x**2 if x % 2 == 0 else x, ex)))

print([value**2 if value % 2 == 0 else value for value in ex])


# reduce
# 대용량 데이터 다룰 때 사용한다.
from functools import reduce
print(reduce(lambda x, y:x+y, [1,2,3,4,5]))