# def longest_common_substring(s, n):
#     x = ''
#     res = ''
#     len_of_x = 0
#     comp = str(s.pop(0))
#     print(comp)
#     len_of_comp = len(comp)
#     n -= 1
#     x = comp[0]
#     for j in range(1, len_of_comp):
#         for k in range(n):
#             if s[k][0:j+1].find(x + comp[j]) == -1:
#                 break
#             if k == n-1:
#                 x = x + comp[j]
#     if len(x) > len_of_x:
#         len_of_x = len(x)
#         res = x
#     if res:
#         return res
#     else:
#         return -1
#
#
#
#
# s = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
# # s = ['apple', 'ape', 'april']
# n = len(s)
# sort_of_s = sorted(s,  key=len)
# print(sort_of_s)
# print(longest_common_substring(sort_of_s, n))

# T = int(input())
#
# while T > 0:
#     N = int(input())
#     S = list(map(str,input().split()))
#     sort_of_s = sorted(S,  key=len)
#     print(longest_common_substring(sort_of_s, N))
#     T -= 1


# s = 'hereiamstackerrank'
# print(list(s))

from itertools import product

x = [1, 2, 3, 0, 5]
y = [7, 8, 9, 10]
# x = list(map(str, x))
# y = list(map(str, y))
prod = list(product(x, y))
print(prod)
tot = 0
for i in prod:
    if sum(i) == 10:
        tot += 1
print(tot)
