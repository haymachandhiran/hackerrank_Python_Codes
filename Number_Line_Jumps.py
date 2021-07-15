def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return 'YES'
        else:
            return 'NO'
    else:
        res = (x1 - x2) / (v2 - v1)
        print(res)
        if res > 0 and (res - int(res) == 0):
            return 'YES'
        else:
            return 'NO'


x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)

print(result)