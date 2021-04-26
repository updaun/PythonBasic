# 1) -9999가 입력될 때 까지 정수를 입력 받아 마지막에 합계, 평균을 출력하는 파이썬 스크립트( list 이용 )

# 입력 자료 : 정수  
# 출력 자료( 결과 ) : 합계, 평균

# 0. 변수 정의
# 1. -9999가 입력될 때 까지 반복
#     1.1 정수 입력
# 2. 합계 계산
# 3. 평균 계산
# 4. 결과 출력

# Symbolic Constant
END = -9999

# 0. 변수 정의
numbers = []
average = 0

# 1. -9999가 입력될 때 까지 반복
# 1.1 정수 입력( 2-read 기법 )
number = int( float( input( '정수 입력 : ' ) ) )
while number != END:
    numbers.append( number )
    number = int( float( input( '정수 입력 : ' ) ) )

# 2. 합계 계산
total = 0
for value in numbers:
    total += value

# 3. 평균 계산
if average > 0:
    average = total / len( numbers )
else:
    average = 0.0
# 4. 결과 출력
print( f'\ntotal = {total:10}' )
print( f'average = {average:8.2f}' )