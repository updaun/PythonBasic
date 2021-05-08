# 20개의 정수를 입력 받아 양수/음수의 개수, 양수일 때 짝수/홀수 개수를 출력하는 파이썬 스크립트

# 문제 분석 )

# 입력 자료 : 20개의 정수
# 출력 자료( 결과 ) : 양수 개수, 음수 개수, 짝수 개수, 홀수 개수
# 알고리즘 설계 )

# 0. 출력 자료 변수 정의
# 1. 20번 반복한다.
#     1.1 정수를 입력 받는다.
#     1.2 입력된 정수가 양수/음수 판별하여 개수를 센다.
#     1.3 입력된 정수가 양수이면 양수/짝수 판별하여 개수를 센다.
# 2. 결과를 출력한다.
# 3. 종료한다.

# Symbolic Constant
MAX = 20

# 출력 자료 저장 변수 정의
positive = 0
negative = 0
even = 0
odd = 0

# 처리 자료 - 알고리즘을 표현하기 위해 구현시 추가된 변수
error_count = 0

# 1. 20번 반복한다.
for i in range( 1, MAX + 1 ):
    # 1.1 정수를 입력 받는다.
    print( '[', i, '] 번째 정수를 입력하세요 : ', end = '' )
    number = int( input() )
    
    # 1.2 양수/음수 판별하여 개수를 센다.
    if number > 0:
        positive += 1
        
        # 1.3 양수이면 짝수/홀수 판별하여 개수를 센다. 
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    elif number < 0:
        negative += 1
    else:
        print( 'Error : 0은 짝수도 홀수도 아닙니다.' )
        error_count += 1
        
# 2. 결과를 출력한다.
print( '\npositive count : ', positive )
print( '\teven count : ', even, '\n\todd count: ', odd )
print( '\nnegative count : ', negative )
print( '\nerror count : ', error_count )