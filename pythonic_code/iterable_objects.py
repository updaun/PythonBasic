cities = ["Seoul", "Busan", "Jeju"]

iter_obj = iter(cities)

# next
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

# iter(linked list 느낌)
memory_address_cities = iter(cities)
print(memory_address_cities)

print(next(memory_address_cities))
print(next(memory_address_cities))
print(next(memory_address_cities))