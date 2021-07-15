# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a, b):
    alice = 0
    bob = 0
    res = []
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] == b[i]:
            pass
        else:
            bob += 1
    res.append(alice)
    res.append(bob)
    return res


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
print(' '.join(map(str, result)))
