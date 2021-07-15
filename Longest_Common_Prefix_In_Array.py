# Given a array of N strings, find the longest common prefix among all strings present in the array.
#
# Input:
# The first line of the input contains an integer T which denotes the number of test cases to follow. Each test case contains an integer N. Next line has space separated N strings.
#
# Output:
# Print the longest common prefix as a string in the given array. If no such prefix exists print "-1"(without quotes).
#
# Constraints:
# 1 <= T <= 103
# 1 <= N <= 103
# 1 <= |S| <= 103
#
# Example:
# Input:
# 2
# 4
# geeksforgeeks geeks geek geezer
# 3
# apple ape april
#
# Output:
# gee
# ap
#
# Explanation:
# Testcase 1: Longest common prefix in all the given string is gee.


def comm(a):
    b = sorted(a)
    c = []
    for i in range(len(b[0])):
        temp = 0
    for j in range(1,len(b)):
        if b[0][0:i+1] != b[j][0:i+1]:
            temp = 1
    if temp == 0:
        c.append(b[0][0:i+1])
    if c:
        return sorted(c, key=len, reverse=True)[0]
    else:
        return -1


T = int(input())
while T > 0:
    N = int(input())
    A = input().split()
    print(comm(A))
    T -= 1














# Not working
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