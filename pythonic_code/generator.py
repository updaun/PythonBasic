def general_list(value):
    result = []
    for i in range(value):
        result.append(i)
    return result

print(general_list(50))

import sys
result = general_list(50)
print(sys.getsizeof(result))

def generator_list(value):
    result = []
    for i in range(value):
        yield i

print(generator_list(50))

for a in generator_list(50):
    print(a)

# 제너레이터를 만들면 메모리를 줄일 수 있다.
# 값이 필요할 때만 호출하여 사용
result = generator_list(50)
print(sys.getsizeof(result))

# generator comprehension
# 일반적인 iterator는 generator에 반해 훨씬 큰 메모리 용량을 사용
gen_ex = (n*n for n in range(500))
print(type(gen_ex))

# Why and When generators
print(sys.getsizeof(gen_ex))

print(sys.getsizeof(list(gen_ex)))

list_ex = [n*n for n in range(500)]
print(sys.getsizeof(list_ex))
