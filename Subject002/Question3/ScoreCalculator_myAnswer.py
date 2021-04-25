# 3) 3명 학생의 이름, 과목1 점수, 과목2 점수, 과목3 점수를 입력받아 출력 결과와 같이 출력하는 파이썬 스크립트( list 이용 )
# * 90점이상은 excellent, 60점미만은 fail, 나머지는 공백
# * 평균을 이용하여 석차를 계산하여 출력

# [ 출력 결과 ]
# hong		50	50	50	150	50.00		3	fail
# kim		90	90	90	270	90.00		1	excellent
# lee		70 	70	70 	210	70.00		2

num_subject = 3
all_student_info = []
for i in range(0, 3):
    name = input("학생의 이름을 입력하세요 : ")
    subject1 = int(input("과목1 점수를 입력하세요 : "))
    subject2 = int(input("과목2 점수를 입력하세요 : "))
    subject3 = int(input("과목3 점수를 입력하세요 : "))
    subject_sum = subject1+subject2+subject3
    subject_avg = subject_sum / num_subject
    student_info = [name, subject1, subject2,
                    subject3, subject_sum, subject_avg]
    all_student_info.append(student_info)

ranking_list = [all_student_info[0][-1],
                all_student_info[1][-1], all_student_info[2][-1]]

for i in range(0, 3):
    if all_student_info[i][-1] == max(ranking_list):
        all_student_info[i].append(1)
    elif all_student_info[i][-1] == min(ranking_list):
        all_student_info[i].append(3)
    else:
        all_student_info[i].append(2)

for i in range(0, 3):
    if all_student_info[i][-2] >= 90:
        all_student_info[i].append("excellent")
    elif all_student_info[i][-2] <= 60:
        all_student_info[i].append("fail")

for x in range(0, 3):
    for y in range(0, len(all_student_info[x])):
        print(all_student_info[x][y], end="\t")
    print()
