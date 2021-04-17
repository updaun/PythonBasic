# 20개의 정수를 입력 받아 양수/음수의 개수, 양수일 때 짝수/홀수 개수를 출력하는 파이썬 스크립트

plus_count = 0
minus_count = 0
even_count = 0
odd_count = 0
zero_count = 0

for i in range(1,5):
    number = int(float(input("정수를 입력하세요 :")))
    if number > 0:
        plus_count += 1
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    elif number < 0:
        minus_count += 1
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    else:
        zero_count += 1
            
print(i,"개의 정수 중 양수의 개수는 ", plus_count, "개 이고, 음수의 개수는 ", minus_count," 개 입니다.")
print("그 중 양수일 때 짝수의 개수는 ", even_count," 개 이고, 홀수의 개수는 ", odd_count," 개 입니다.")
            