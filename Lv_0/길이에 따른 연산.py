def solution(num_list):
    mul = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            mul *= i
        return mul

# from math import prod
# def solution(num_list):
#     return sum(num_list) if len(num_list)>=11 else prod(num_list)