# join
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
result2 = '-'.join(colors)
print(result)  # redbluegreenyellow
print(result2)  # red-blue-green-yellow

# split
items = 'zero one two three'.split()
print(items)
example = 'python, java, javascript'
for content in example.split(","):
    print(content.strip())

# list comprehension
result = [i for i in range(10)]
print(result)
result = [i for i in range(10) if i % 2 == 0]
print(result)

word_1 = 'Hello'
word_2 = 'World'
result = [i+j for i in word_1 for j in word_2]
# Nested For loop
print(result)

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
# fillter
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)
result.sort()
print(result)

# if-else
result = [i+j if not(i==j) else i for i in case_1 for j in case_2]
print(result)
