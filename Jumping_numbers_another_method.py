def find_jump_no(n):
    res = []
    l = len(str(n))
    print(l)
    if n < 10:
        for i in range(n+1):
            res.append(str(i))
    else:
        res = [i for i in range(10)]
        res = list(map(str, res))
        print(res)
        for i in range(1, int(str(n)[0])):
            x = str(i)
            y = str(i)
            for j in range(l-1):
                if int(x) < n and int(y) < n:
                    x = x + x[-1] + str(int(x[-1]) - 1)
                    print(x)
                    res.append(x)
                    print(res)
                    y = y + y[-1] + str(int(y[-1]) + 1)
                    print(y)
                    res.append(y)
                    print(res)
    print(res.sort())
    # return res


n = 200
find_jump_no(n)
# print(' '.join(find_jump_no(n)))