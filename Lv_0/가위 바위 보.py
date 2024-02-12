def solution(rsp):
    arr=list(rsp)
    ans=[]
    for i in arr:
        if i == '0':
            ans.append('5')
        elif i == '2':
            ans.append('0')
        else:
            ans.append('2')
    return ''.join(ans)

# def solution(rsp):
#     d = {'0':'5','2':'0','5':'2'}
#     return ''.join(d[i] for i in rsp)