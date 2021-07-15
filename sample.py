# from itertools import permutations
#
# w = 'dkhc'
# res = []
# perm = permutations(w)
# for i in list(perm):
#     res.append(''.join(i))
# res.sort()
# print(res)
# x = res.index(w)
# print(x)
# print(res[x+1])

# from itertools import product
# A = [1, 2]
# B = [3, 4]
# x = list(product(A, B))
# x.sort()
# for i in x:
#     print(i,end =' ')
#

from itertools import groupby


def find_repeat_times(num, n):


    res = []
    num = list(num)
    for key, group in (groupby(num)):
        res.append((len(list(group)), int(key)))
    for i in res:
        print(i, end=' ')

S = input()
n = len(S)
find_repeat_times(S, n)
