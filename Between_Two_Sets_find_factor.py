#https://www.hackerrank.com/challenges/between-two-sets/problem


def getTotalX(arr, brr):
    ar = max(arr)
    br = min(brr)
    print(ar)
    print(br)
    res = []
    for i in range(ar, br+1, 1):
        t = 0
        for j in arr:
            if i % j == 0:
                pass
            else:
                t = 1
                break
        if t == 1:
            continue
        for k in brr:
            if k % i == 0:
                pass
            else:
                t = 1
                break
        if t == 1:
            continue
        if t == 0:
            res.append(i)
    print(res)
    return len(res)






first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
total = getTotalX(arr, brr)
print(total)
