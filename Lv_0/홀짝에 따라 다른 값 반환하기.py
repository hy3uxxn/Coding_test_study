def solution(n):
    sum = 0
    if n%2!=0:
        for i in range(1, n+1, 2):
            sum+=i
    else:
        for i in range(2, n+1, 2):
            sum+=i*i
    return sum


# if n%2:
#         return sum(range(1,n+1,2))
#     return sum([i*i for i in range(2,n+1,2)])