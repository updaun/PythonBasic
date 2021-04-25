# 2) 정수를 입력받아 평균, 편차, 편차제곱, 분산을 계산하여  list에 저장하고 정수가 0이 입력되면 list 내용을 출력하는  파이썬 스크립트( list 이용 )

number = int(float(input("정수를 입력하세요(0 입력시 결과를 출력) : ")))
number_list = [number]
number_sum = 0
number_avg = 0
deviation_list = []
square_deviation_list = []
variance = 0
square_deviation_sum = 0

while number != 0:
    number = int(float(input("정수를 입력하세요(0 입력시 결과를 출력) : ")))
    number_list.append(number)

for i in range(0, len(number_list)-1):
    number_sum += number_list[i]
    number_avg = number_sum / (len(number_list)-1)

for i in range(0, len(number_list)-1):
    deviation_list.append(number_list[i]-number_avg) 
    square_deviation_list.append(deviation_list[i]*deviation_list[i])
    square_deviation_sum += square_deviation_list[i]
    variance = square_deviation_sum / (len(number_list)-1)

print("평균 =",number_avg,"\n")
print("편차 =",deviation_list,"\n")
print("편차 제곱 =",square_deviation_list,"\n")
print("분산 =",variance,"\n")