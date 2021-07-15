# a = [2, 5, 200, 10, 15, 150, 25,  39, 155, 9, 19]
a = [100,90,80,70,60,50]
b = sorted(a, reverse=True)
if b == a:
    print(-1)
else:
    print(a)
    print(len(a))
    a.append(0)
    n = len(a)
    print(a)
    print(n)
    temp = []
    tot = 0
    for i in range(n-1):
        tot = tot + a[i]
        if a[i] <= a[i+1]:
            pass
        else:
            temp.append(tot)
            tot = 0
    res = sorted(temp, reverse=True)[0]
    print(res)
