#https://www.hackerrank.com/challenges/separate-the-numbers/problem

# def separateNumbers(s):
#     if s[0] == '0':
#         return 'NO'
#     l = len(s)
#     dig_inc = 0
#     if l == 1:
#         return 'NO'
#     if l % 2 == 0:
#         dig = int(len(s) / 2)
#     else:
#         dig = int(len(s) / 2) + 1
#     for i in range(dig):
#         main_temp = int(s[0:i+1])
#         print(f'Series starts with : {main_temp}')
#         temp = int(s[0:i+1])
#         t = 0
#         for j in range(i+1, l):
#             if set(str(temp)) == set('9') or dig_inc == 1:
#
#                 print(s[j:j + i + 2])
#                 if int(s[j:j + i + 2]) - temp == 1:
#                     temp = int(s[j:j + i + 2])
#                     print('success')
#                     dig_inc = 1
#                 else:
#                     t = 1
#                     break
#             else:
#                 if int(s[j:j+i+1]) - temp == 1:
#                     print(s[j:j+i+1])
#                     temp = int(s[j:j+i+1])
#                     print('success')
#                 else:
#                     t = 1
#                     break
#         if t == 0:
#             return 'YES'+' '+str(main_temp)
#     return 'NO'
#
# def separateNumbers(s):
#     if s[0] == '0':
#         return 'NO'
#     l = len(s)
#     dig_inc = 0
#     if l == 1:
#         return 'NO'
#     if l % 2 == 0:
#         dig = int(len(s) / 2)
#     else:
#         dig = int(len(s) / 2) + 1
#     for i in range(dig):
#         main_temp = int(s[0:i + 1])
#         print(f'Series starts with : {main_temp}')
#         temp = int(s[0:i + 1])
#         t = 0
#         for j in range(i + 1, l):
#             if j < i + 2:
#
#
#
#
#
#
#
#
# S = input() #99910001001
# print(separateNumbers(S))


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(a):
    for i in range(len(a)//2):
        c=''
        f=a[:i+1]
        temp=int(a[:i+1])
        for _ in range(len(a)//(i+1)):
            c+=str(temp)
            if c not in a:
                break
            temp+=1
        if a in c:
            print('YES',f)
            break
    else:
        print('NO')


s = input()
separateNumbers(s)