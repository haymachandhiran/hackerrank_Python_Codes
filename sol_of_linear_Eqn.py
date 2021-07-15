# Given a linear equation of n variables, find number of non-negative integer solutions of it. For example,let the given equation be “x + 2y = 5”, solutions of this equation are “x = 1, y = 2”, “x = 5, y = 0” and “x = 1. It may be assumed that all coefficients in given equation are positive integers.

#
# Input:  coeff[] = {1, 2}, rhs = 5 :
# Output: 3
# The equation "x + 2y = 5" has 3 solutions.
# (x=3,y=1), (x=1,y=2), (x=5,y=0)


# Input:  coeff[] = {2, 2, 3}, rhs = 4
# Output: 3
# The equation "2x + 2y + 3z = 4"  has 3 solutions.
# (x=0,y=2,z=0), (x=2,y=0,z=0), (x=1,y=1,z=0)


from itertools import permutations
from itertools import combinations_with_replacement


n = int(input())
cf = list(map(int, input().split()))
rhs = int(input())
t = list(range(rhs + 1))
print(t)
comb = list(combinations_with_replacement(t, n))
print(sorted(comb))
perm = []
for i in comb:
    perm.extend(list(set(permutations(i, n))))
res = 0
for i in perm:
    temp = 0
    for j in range(len(i)):
        temp += cf[j] * i[j]
    if temp == rhs:
        res += 1
        print(i)
print(res)


# def countSol(coeff, n, rhs):
#     dp = [0 for i in range(rhs + 1)]
#     dp[0] = 1
#     print(dp)
#     for i in range(n):
#         for j in range(coeff[i], rhs + 1):
#             dp[j] += dp[j - coeff[i]]
#             #print(f'Value of i : {i} and value of dp[{j}] = {dp[j]}')
#             print(dp)
#     return dp[rhs]
#
#
# # Driver Code
# coeff = [2,2,3]
# rhs = 8
# n = len(coeff)
# print(countSol(coeff, n, rhs))
