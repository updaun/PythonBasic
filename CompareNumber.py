# 3개의 정수를 입력 받아 큰수, 중간수, 작은수 순으로 출력하는 파이썬 스크립트

number1 = int(float(input("정수를 입력하세요 : ")))
number2 = int(float(input("정수를 입력하세요 : ")))
number3 = int(float(input("정수를 입력하세요 : ")))

if number1 >= number2 >= number3:
    if number1 > number3:
        print(number1,number2,number3)
    else:
        print(number3,number2,number1)
        
elif number1 >= number2 <= number3:
    if number1 > number3:
        print(number1,number3,number2)
    else:
        print(number3,number1,number2)
        
elif number1 <= number2 >= number3:
    if number1 > number3:
        print(number2,number1,number3)
    else:
        print(number2,number3,number1)

elif number1 <= number2 <= number3:
    if number1 > number3:
        print(number1,number2,number3)
    else:
        print(number3,number2,number1)        