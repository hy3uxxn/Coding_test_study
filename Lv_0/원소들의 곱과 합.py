def solution(num_list):
    mul = 1
    add = 0
    for i in num_list:
        mul *= i
    for i in num_list:
        add += i

    return 0 if mul > add * add else 1