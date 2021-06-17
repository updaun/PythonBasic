def solution(array, commands):
    answer = []
    for i in commands:
        f = i[0]-1
        e = i[1]
        p = i[2]-1
        if f == e:
            slicing_a = [array[f]]
            sort_a = slicing_a
        else:
            slicing_a = array[f:e]
            sort_a = sorted(slicing_a)
        answer.append(sort_a[p])
    return answer