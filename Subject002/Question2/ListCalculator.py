# 2) 정수를 입력받아 평균, 편차, 편차제곱, 분산을 계산하여  list에 저장하고 정수가 0이 입력되면 list 내용을 출력하는  파이썬 스크립트( list 이용 )

# 평균 : 입력 수의 합 / 총 입력 수
# 편차 : 입력 개별 수 - 평균
# 편차 제곱 : 편차 * 편차
# 분산 : 편차 제곱의 평균

# 입력 자료 : 정수
# 출력 자료( 결과 ) : 평균, 편차, 편차제곱, 분산

# 0. 변수 정의
# 1. 0 이 입력될 때까지 정수 입력  
#     1.1 정수 입력
# 2. 평균 계산
# 3. 편차 계산
# 4. 편차 제곱 계산
# 5. 분산 계산
# 6. 결과 출력

# symbolic constant
END = 0
MAX_LINE = 10

# 0. 변수 정의
numbers = [] # 정수 저장 list
total = 0 # 합계 저장 변수
deviation_squareds_total = 0 # 편차 제곱 합 저장 변수

# 1. 0이 입력될 때까지 정수 입력
# 2.1 정수 입력( 2-read 기법)
i = 1
number = int( float( input( f"Input number[ {i:5} ]( 0 : end ) : " ) ) )
while number != END:
    numbers.append( number )
    total += number
    i += 1
    number = int( float( input( f"Input number[ {i:5} ]( 0 : end ) : " ) ) )

count = len( numbers ) # 입력된 정수 개수

# 2. 평균 계산
mean = total / count

# 3. 편차 계산
deviations = [] # 편차 저장 list
for value in numbers:
    deviations.append( value - mean )

# 4. 편차 제곱 계산
deviation_squareds = [] # 편차 제곱 list
for value in deviations:
    deviation_squareds.append( value ** 2 )

# 5. 분산 계산
for value in deviation_squareds:
    deviation_squareds_total += value
variance = deviation_squareds_total / count

# 5. 결과 출력
print()
line_count = 1
print( '\n변량 출력 :' )
for i in range( count ):
    print( f'{numbers[ i ]:8}', end = '' )
    line_count += 1
    if line_count > MAX_LINE:
        print()
        line_count = 1
print()

print( f'\nmean = {mean:8.2f}\n' )

print( '편차 출력 :' )
for i in range( count ):
    print( f'{deviations[ i ]:8.2f}', end = '' )
    line_count += 1
    if line_count > MAX_LINE:
        print()
        line_count = 1
print()

print( '편차 제곱 출력 :' )
for i in range( count ):
    print( f'{deviation_squareds[ i ]:8.2f}', end = '' )
    line_count += 1
    if line_count > MAX_LINE:
        print()
        line_count = 1
print()

print( f'\nvariance = {variance:8.2f}\n' )