import random

num_list = [x for x in range(1,10)]
# print(num_list)

random.shuffle(num_list)
# print(num_list)

tournament_list = []
for i in range(4):
    tournament_list.append([num_list[0], num_list[-1]])
    num_list.remove(num_list[0])
    num_list.remove(num_list[-1])

print('토너먼스 순서 : ',tournament_list )
print('부전승 : ', num_list[0])