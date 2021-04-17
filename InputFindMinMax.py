# 10개의 정수를 입력 받아 최대값과 최소값을 출력 하는 파이썬 스크립트

max_number = int(float(input("정수를 입력하세요 : ")))
min_number = int(float(input("정수를 입력하세요 : ")))

if max_number > min_number:
    for i in range(1,11):
        input_number = int(float(input("정수를 입력하세요 : ")))
        if(max_number < input_number):
            max_number = input_number
        if(min_number > input_number):
            min_number = input_number
            
if min_number >= max_number:
    min_number = max_number
    for i in range(1,11):
        input_number = int(float(input("정수를 입력하세요 : ")))
        if(max_number < input_number):
            max_number = input_number
        if(min_number > input_number):
            min_number = input_number

    
print("최대값은 ", max_number,"이고 최솟값은 ", min_number,"입니다.")