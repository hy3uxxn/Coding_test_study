def solution(n):
    # div=[]
    # for i in range(1, n+1):
    #     if n%i==0:
    #         div.append(i)
    # if len(div)%2!=0:
    #     return 1
    # else:
    #     return 2

    return 1 if len([i for i in range(1, n+1) if n%i==0])%2!=0 else 2