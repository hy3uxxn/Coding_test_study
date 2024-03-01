def solution(my_string, index_list):
    a = ''
    for i in index_list:
        a += my_string[i]
    return a

#조금더 파이썬 다운 코드
# def solution(my_string, index_list):
#     return ''.join(my_string[i] for i in index_list)