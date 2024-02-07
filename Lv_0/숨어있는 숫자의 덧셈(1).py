def solution(my_string):
    return sum([int(i) for i in list(my_string) if i.isdigit()])