# -9999가 입력될 때까지 반복하면서 이름, 과목1점수, 과목2점수를 입력받고 총점, 평균을 출력하는 파이썬 스크립트

while True:
    name = str(input("이름을 입력하세요 : "))
    if name == '-9999':
        break
    subject1 = int(float(input("과목1점수를 입력하세요 : ")))
    if subject1 == -9999:
        break
    subject2 = int(float(input("과목2점수를 입력하세요 : ")))
    if subject2 == -9999:
        break

    sum = subject1 + subject2
    avg = (subject1 + subject2)/2
    
    print("이름 : ", name, "\t총점 : ", sum, "\t평균 : ", avg,"\n")