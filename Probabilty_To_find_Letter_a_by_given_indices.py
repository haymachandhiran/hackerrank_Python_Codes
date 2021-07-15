#https://www.hackerrank.com/challenges/iterables-and-iterators/problem
from itertools import combinations


def prob_of_ltr_a_in_K(s, n, k):
    comb = list(combinations(s, k))
    # for i in comb:
    #     print(i,end= ' ')
    tot = 0
    for i in comb:
        if 'a' in i:
            tot += 1
    return tot/len(comb)

N = int(input())
S = list(map(str, input().split()))
K = int(input())
print(prob_of_ltr_a_in_K(S, N, K))
