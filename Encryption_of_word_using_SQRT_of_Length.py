import math


def encryption(s):
    s = s.replace(' ', '')
    print(s)
    a = len(s)
    print(a)
    x = math.sqrt(a)
    if x - int(x) == 0:
        row = int(x)
        clm = int(x)
    else:
        row = int(math.sqrt(a))
        clm = int(math.sqrt(a)) + 1
    if row * clm < a:
        row += 1
    mat_spl = []
    print(row, clm)
    for i in range(0, a, clm):
        mat_spl.append(s[i:i + clm])
    print(mat_spl)
    for i in range(row):
        if len(mat_spl[i]) < clm:
            temp = clm - len(mat_spl[i])
            for j in range(temp):
                mat_spl[i] += ' '
    print(mat_spl)
    res = []
    for i in range(clm):
        t = ''
        for j in range(row):
            if mat_spl[j][i] != ' ':
                t += mat_spl[j][i]
        res.append(t)
    return ' '.join(res)


s = 'iffactsdontfittotheorychangethefacts'
print(encryption(s))

# from math import *
# from itertools import zip_longest
# # a = 'feedthedog'
# # b = []
# # k = ceil(pow(len(a) ,.5))
# # for i in range(0, len(a), k):
# #   b.append(a[i:i+k])
# # s = tuple(b)
# # for i in zip_longest(*s, fillvalue=''):
# #   print(*i, sep='', end = ' ')
# # print()
# z = ('csk','chennai','bang')
# print(list(zip_longest(*z,fillvalue='*')))

# isieae fdtonf fotrga anoyec cttctt tfhhhs


# # !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# # Complete the encryption function below.
# def encryption(s):
#     s = s.replace(' ', '')
#     # print(s)
#     a = len(s)
#     x = math.sqrt(a)
#     if x - int(x) == 0:
#         row = int(x)
#         clm = int(x)
#     else:
#         row = int(math.sqrt(a))
#         clm = int(math.sqrt(a)) + 1
#     if row * clm < a:
#         row += 1
#     mat_spl = []
#     # print(row, clm)
#     for i in range(0, a, clm):
#         mat_spl.append(s[i:i + clm])
#     # print(mat_spl)
#     for i in range(row):
#         if len(mat_spl[i]) < clm:
#             temp = clm - len(mat_spl[i])
#             print(temp)
#             for j in range(temp):
#                 mat_spl[i] += ' '
#     # print(mat_spl)
#     res = []
#     for i in range(clm):
#         t = ''
#         for j in range(row):
#             if mat_spl[j][i] != ' ':
#                 t += mat_spl[j][i]
#         res.append(t)
#     return (' '.join(res))
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = encryption(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()
