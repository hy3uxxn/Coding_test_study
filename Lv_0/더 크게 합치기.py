def solution(a, b):
    return max(int(str(a)+str(b)),int(str(b)+str(a)))

    # return int(max(f"{a}{b}", f"{b}{a}"))