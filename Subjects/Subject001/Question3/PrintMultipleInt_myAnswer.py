# 1~10000사이에서 3의 배수와 5의 배수를 한 줄에 10개씩 출력하고, 마지막에 3의 배수와 5의 배수 갯수를 출력하는 파이썬 스크립트

count = 0
multipleThree_count = 0
multipleFive_count = 0

print("3의배수 출력")
for i in range(1,10001):
    if i % 3 == 0:
        print(i, end ="\t")
        count += 1
    if count == 10:
        print("")
        count = 0
        
count = 0             
print("\n5의배수 출력")
for i in range(1,10001):
    if i % 5 == 0:
        print(i, end ="\t")
        count += 1
    if count == 10:
        print("")
        count = 0


for i in range(1,10001):
    if i % 3 == 0:
        multipleThree_count += 1
    elif i % 5 == 0:
        multipleFive_count += 1  
    i += 1
    
print("1 ~",i,"사이에서의 3의 배수는 ", multipleThree_count, " 개이고 와 5의 배수의 개수는 ", multipleFive_count," 개 입니다.")