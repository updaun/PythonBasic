# 3) 3명 학생의 이름, 과목1 점수, 과목2 점수, 과목3 점수를 입력받아 출력 결과와 같이 출력하는 파이썬 스크립트( list 이용 )
# * 90점이상은 excellent, 60점미만은 fail, 나머지는 공백
# * 평균을 이용하여 석차를 계산하여 출력

# [ 출력 결과 ]
# hong		50	50	50	150	50.00		3	fail
# kim		90	90	90	270	90.00		1	excellent
# lee		70 	70	70 	210	70.00		2

# 입력 자료 : 이름, 3과목 성적
# 출력 자료( 결과 ) : 총점, 평균, 석차, 판정

# 0. 변수 정의  
# 1. 3만큼 반복  
#     1.1 이름, 3과목 점수 입력  
#     1.2 총점, 평균, 판정 계산  
# 2. 석차 계산
# 3. 성적 일람표 출력

# symbolic constant
MAX_STUDENT = 3
MAX_SUBJECT = 3
EXCELLENT = 90.0
FAIL = 60.0

# 0. 변수 정의
students = []

# 1. 3만큼 반복
for i in range( MAX_STUDENT ):
    student = []
    
    # 1.1 이름 입력
    name = input( f"Input student[ {i + 1:2} ] - name : " )
    student.append( name )

    # 1.1 3과목 점수 입력
    total = 0
    for i in range( MAX_SUBJECT ):
        subject = int( input( f"\tInput subject[ {i + 1:2} ] : " ) )
        while subject < 0 or subject > 100:
            print( '\tError : subject range 0 ~ 100' )
            subject = int( input( f"\tInput subject[ {i + 1:2} ] : " ) )
        student.append( subject )
        
        # 1.2 총점 계산
        total += subject
    student.append( total )

    # 1.2 평균 계산
    average = total / MAX_SUBJECT
    student.append( average )

    # 1.2 판정
    if average >= EXCELLENT:
        student.append( "excellent" )
    elif average < FAIL:
        student.append( "fail" )
    else:
        student.append( "" )

    students.append( student )
    print()

# 2. 석차 계산
for i in range( len( students ) ):
    rank = 1
    for j in range( len( students ) ):
        if students[ i ][ 5 ] < students[ j ][ 5 ]:
            rank += 1
    students[ i ].append( rank )

# 3. 성적일람표 출력
for i in range( MAX_STUDENT ):
    print( f'{students[ i ][ 0 ]:<20s}', end = '')
    print( f'{students[ i ][ 1 ]:3d} {students[ i ][ 2 ]:3d} {students[ i ][ 3 ]:3d}', end = '' )
    print( f'{students[ i ][ 4 ]:5d} {students[ i ][ 5 ]:6.2f}', end = '' )
    print( f'{students[ i ][ 7 ]:2d} {students[ i ][ 6 ]:<10s}' )