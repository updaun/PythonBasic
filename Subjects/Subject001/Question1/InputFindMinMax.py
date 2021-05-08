# 10개의 정수를 입력 받아 최대값과 최소값을 출력 하는 파이썬 스크립트

# 문제 분석 )

# 입력 자료 : 10개의 정수  
# 출력 자료( 결과 ) : 최대값, 최소값
# 알고리즘 설계 )

# 0. 출력 자료 변수 정의
# 1. 10번 반복한다.
#     1.1 정수를 입력 받는다.
#     1.2 최대값인지 판별한다.
#     1.3 최소값인지 판별한다.
# 2. 결과를 출력한다.
# 3. 종료한다.


import sys

# Symbolic Constant
MAX = 10

# 출력 자료 저장 변수 정의
max_number = -sys.maxsize -1 # 가장 작은 값
min_number = sys.maxsize # 가장 큰 값

# 10번 반복한다.
for i in range( 1, MAX + 1 ):
    # 1.1 정수를 입력 받는다.
    print( '[ ', i, ' ] 번째 정수를 입력하세요 : ', end = '' )
    number = int( input() )
    
    # 1.2 최대값인지 판별한다.
    if number > max_number:
        max_number = number
    
    # 1.3 최소값이지 판별한다.
    if number < min_number:
        min_number = number

# 2. 결과를 출력한다.
print( '\nmax number : ', max_number, '\nmin number : ', min_number )