# -9999가 입력될 때까지 반복하면서 이름, 과목1점수, 과목2점수를 입력받고 총점, 평균을 출력하는 파이썬 스크립트

# 문제 분석 )

# 입력 자료 : 이름, 과목1점수, 과목2점수
# 출력 자료( 결과 ) : 총점, 평균
# 알고리즘 설계 )

# 0. 출력 자료 변수 정의  
# 1. -9999가 입력될때 까지 반복한다.  
#     1.1 이름, 과목1점수, 과목2점수를 입력 받는다.  
#     1.2 총점, 평균을 계산한다.  
#     1.3 결과를 출력한다.  
# 2. 종료한다.

# Symbolic Constant
FINAL = '-99999'
MAX_SUBJECT = 2

# 처리 변수
count = 0

# 1. -9999가 입력될때 까지 반복한다.
name = input( '이름 입력 -99999이면 종료 ) : ' )
while name != FINAL:
    # 1.1 이름, 과목1점수, 과목2점수를 입력 받는다.
    subject1 = int( input( '과목1점수 입력 : ' ) )
    subject2 = int( input( '과목2점수 입력 : ' ) )
    count += 1
    
    # 1.2 총점, 평균을 계산한다.
    total = subject1 + subject2
    average = total / MAX_SUBJECT
    
    # 1.3 결과를 출력한다.
    print( name, '\t', subject1, '\t', subject2, '\t', total, '\t', average )
    name = input( '\n이름 입력 -99999이면 종료 ) : ' )