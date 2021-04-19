# 3개의 정수를 입력 받아 큰수, 중간수, 작은수 순으로 출력하는 파이썬 스크립트

# 문제 분석 )

# 입력 자료 : 3개의 정수
# 출력 자료( 결과 ) : 3개의 입력 받은 정수를 큰수, 중간수, 작은수 순으로 출력
# 알고리즘 설계 )

# 0. 출력 자료 변수 정의
# 1. 3개의 정수를 입력받는다.
# 2. 3개의 정수를 큰수, 중간수, 작은수 순으로 나눈다.
# 3. 큰수, 중간수, 작은수 순으로 출력한다.

# Symbolic Constant
MAX = -99999

# 1. 3개의 정수를 입력받는다.
number1 = int( input( '첫 번째 정수 입력 ( -99999 : 종료 ) : ' ) )
while number1 != -99999:
        number2 = int( input( '두 번째 정수 입력 : ' ) )
        number3 = int( input( '세 번째 정수 입력 : ' ) )

        # 2. 3개의 정수를 큰수, 중간수, 작은수 순으로 나눈다.
        if number1 > number2:
            if number1 > number3:
                max = number1
                if number2 > number3:
                    mid = number2
                    min = number3
                else:
                    mid = number3
                    min = number2
            else:
                max = number3
                mid = number1
                min = number2
        elif number2 > number3:
            max = number2
            if number1 > number3:
                mid = number1
                min = number3
            else:
                mid = number3
                min = number1
        else:
            max = number3
            mid = number2
            min = number1
            
        # 3. 큰수, 중간수, 작은수 순으로 출력한다.    
        print( '\n입력 : ', number1, number2, number3 )
        print( '결과 : ', max, mid, min )
        
        number1 = int( input( '\n첫 번째 정수 입력 ( -99999 : 종료 ) : ' ) )