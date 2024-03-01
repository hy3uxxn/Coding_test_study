def solution(my_string, is_prefix):
    a = my_string[0:len(is_prefix)]
    if a == is_prefix:
        return 1
    else:
        return 0

# 최적화 한 코드
# def solution(my_string, is_prefix):
#     return my_string[:len(is_prefix)] == is_prefix

# startswith 함수 사용한 코드
# def solution(my_string, is_prefix):
#     return int(my_string.startswith(is_prefix))