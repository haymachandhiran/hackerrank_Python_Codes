#https://www.hackerrank.com/challenges/non-divisible-subset/problem

from itertools import combinations


def nonDivisibleSubset(k, s):
    for i in range(len(s), 0, -1):
        for j in combinations(s, i):
            t = 0
            print(i, j)
            for h in combinations(j, 2):
                print(h)
                if sum(h) % k != 0:
                    pass
                else:
                    t = 1
                    break
            if t == 0:
                return len(j)


n, k = input().rstrip().split()
n = int(n)
k = int(k)
s = list(map(int, input().rstrip().split()))
print(nonDivisibleSubset(k, s))
