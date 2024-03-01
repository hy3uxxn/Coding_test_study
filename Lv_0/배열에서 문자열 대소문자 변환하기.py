def solution(strArr):
    answer = []

    for idx, val in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(val.lower())
        else:
            answer.append(val.upper())

    return answer

# def solution(strArr):
#     return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]