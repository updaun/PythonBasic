# mylib.py
# 사용자 모듈
#
def my_max(l):
    if len(l)>0:
        max = l[0]
        for v in l:
            if max < v:
                max = v

    else:
        max = None
        
    return max

def my_min(l):
    if len(l) > 0:
        min = l[0]
        for v in l:
            if min > v:
                min = v

    else:
        min = None

    return min