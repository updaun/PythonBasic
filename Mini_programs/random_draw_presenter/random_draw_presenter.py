import random
import csv

def random_draw():
    #with open('classmate.csv', encoding='utf-8') as csvfile:
    with open('classmate.csv') as csvfile:
        csv_reader = csv.reader(csvfile)

        class_students_list = []

        input_num = input("반을 선택하겠습니다! 1 ~ 6의 숫자를 입력하세요! : ")
        print("")

        for row in csv_reader:
            if row[1] == input_num:
                class_students = row[0].strip()
                class_students_list.append(class_students)

        print("-" * 50)
        print('')
        print('축하합니다. 발표자는 \'{}\'님 입니다.'.format(random.choice(class_students_list)))
        print('')
        print("-" * 50)
        print('')
        restart_btn = input('다시 진행하시겠습니까? (y/n) : ')
        print("")

        if restart_btn == 'y' or restart_btn == 'Y':
            random_draw()
        else:
            print('랜덤 발표자 뽑기를 종료합니다. 이용해주셔서 감사합니다. \n')
            pass


def __main__():
    try:
        random_draw()
    except FileNotFoundError:
        print('같은 디렉토리에 "gj_ai_class_all.csv", [예시] : 홍길동,3 을 넣어주세요.\n')
    except IndexError:
        print('값의 범위를 벗어났습니다. 1~6 사이의 숫자를 입력하세요.\n')
        __main__()

    
__main__()