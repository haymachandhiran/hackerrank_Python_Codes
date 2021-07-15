def non_repeat_char(a, n):
    res = []
    check = []
    res.append(a[0])
    check.append(a[0])
    for i in range(1, n):
        if a[i] in check:
            res.append(str(-1))
        else:
            check.append(a[i])
            if res[-1] == '-1':
                res.append(check[-1])
            else:
                res.append(res[-1])
    return res


T = int(input())
while T > 0:
    N = int(input())
    x = list(map(str,input().split()))
    print(' '.join(non_repeat_char(x, N)))
    T -= 1
# a = ['a', 'a', 'b', 'c']
# n = len(a)
# print(non_repeat_char(a, n))