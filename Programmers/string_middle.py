def solution(s):
    list_s = list(s)
    if int(len(list_s) % 2) == 1:
        answer = list_s[int(len(list_s) / 2)]
    else:
        answer = list_s[int((len(list_s) / 2)-0.5)] + list_s[int((len(list_s) / 2)+0.5)]
    return answer