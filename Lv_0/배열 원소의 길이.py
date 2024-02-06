def solution(strlist):
    return [len(i) for i in strlist]

# 다른 풀이
def solution2(strlist):
    arr=[]
    for i in strlist:
        arr.append(len(i))
    return arr