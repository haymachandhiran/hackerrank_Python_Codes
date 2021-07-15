#https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem


def check_best(x):
    if x == 3:
        return '555'
    if x == 5:
        return '33333'
    li = list(range(1, x//2 + 1))
    print(li)
    res = 0
    t = 0
    for i in li:
        if (i % 3 == 0 or i % 5 == 0) and ((x-i) % 3 == 0 or (x-i) % 5 == 0):
            t = 1
            print(x-i, i)
            res_val = ''
            temp1, temp2 = '5',  '3'
            if (x-i) % 3 == 0:
                res_val += temp1 * (x - i)
                chg = res_val[::-1]
                if int(chg) > int(res_val):
                    res_val = chg
            else:
                res_val += temp2 * (x - i)
                chg = res_val[::-1]
                if int(chg) > int(res_val):
                    res_val = chg
            if i % 3 == 0:
                res_val += temp1 * i
                chg = res_val[::-1]
                if int(chg) > int(res_val):
                    res_val = chg
            else:
                res_val += temp2 * i
                chg = res_val[::-1]
                if int(chg) > int(res_val):
                    res_val = chg
            res_val = int(res_val)
            if res_val > res:
                res = res_val
    if t == 0:
        return '-1'
    else:
        return res


t = int(input())
for _ in range(t):
    x = int(input())
    print(check_best(x))


