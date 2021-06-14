# No hash
def solution1(participant, completion):
    for i in completion:
        participant.remove(i)
        answer = participant[0]
    return answer

# hash?
def solution2(participant, completion):
    dict = {}
    c_val = 0
    answer = ''
    for i in participant:
        dict[i] = 0
    for i in participant:
        dict[i] = dict[i]+1
    for i in completion:
        dict[i] = dict[i]-1
    for k,v in dict.items():
        if v != 0:
            answer = k
    return answer