# 1) -9999가 입력될 때 까지 정수를 입력 받아 마지막에 합계, 평균을 출력하는 파이썬 스크립트( list 이용 )

number = 0
number_list = []
number_sum = 0
number_avg = 0

while number != -9999:
    number = int(float(input("정수를 입력하세요 : ")))
    number_list.append(number)

for i in range(0, len(number_list)-1):
    number_sum += number_list[i]

number_avg = number_sum / (len(number_list)-1)

print("합계 = {}, 평균 = {}".format(number_sum, number_avg))
