#https://www.hackerrank.com/challenges/maximize-it/problem

import math
import random
from itertools import *


def maximize_it(n, m):
    tot = 0
    print(*N, sep=',')
    res = 0
    for j in product(*N):
        print(j)
        if res < (sum(map(lambda x: x**2, j)) % m):
            res = (sum(map(lambda x: x**2, j)) % m)
    return res

K, M = map(int, input().split())
N = []
for i in range(K):
    N.append(list(map(int, input().split())))
    N[i].pop(0)
print(maximize_it(N, M))
