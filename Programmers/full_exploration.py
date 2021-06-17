def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    correct_1 = []
    correct_2 = []
    correct_3 = []
    answer = []

    for i in range(len(answers)):
        if answers[i] == p1[i%5]:
            correct_1.append(answers[i])
        if answers[i] == p2[i%8]:
            correct_2.append(answers[i])
        if answers[i] == p3[i%10]:
            correct_3.append(answers[i])

    a = len(correct_1)
    b = len(correct_2)
    c = len(correct_3)

    x = [a,b,c]

    if max(x) == a:
        answer.append(1)
    if max(x) == b:
        answer.append(2)
    if max(x) == c:
        answer.append(3)
    return answer
