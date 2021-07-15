#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

from itertools import combinations


def divisibleSumPairs(n, k, ar):
    comb = list(combinations(ar, 2))
    tot = 0
    for i in comb:
        if sum(i) % k == 0:
            tot += 1
    return tot


nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)
print(result)

# 6 3
# 1 3 2 6 1 2