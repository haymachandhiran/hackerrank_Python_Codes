# Given
# a
# string
# s, recursively
# remove
# adjacent
# duplicate
# characters
# from the string
#
# s.The
# output
# string
# should
# not have
# any
# adjacent
# duplicates.
#
# Input:
# The
# first
# line
# of
# input
# contains
# an
# integer
# T, denoting
# the
# no
# of
# test
# cases.Then
# T
# test
# cases
# follow.Each
# test
# case
# contains
# a
# string
# str.
#
# Output:
# For
# each
# test
# case, print
# a
# new
# line
# containing
# the
# resulting
# string.
#
# Constraints:
# 1 <= T <= 100
# 1 <= Length
# of
# string <= 50
#
# Example:
# Input:
# 2
# geeksforgeek
# acaaabbbacdddd
#
# Output:
# gksforgk
# acac
# Input:
# mississipie
#
# Its Correct output is:
# mpie
#
# And Your Code's output is:
# miiipie

def remove_adjacent_dup(s, n):
    '''
    Recursive function to remove all duplicate adjacent of a given string
    '''
    sub = []
    sub_len = 0
    if s[0] != s[1]:
        sub.append(s[0])
    for i in range(1, n-1):
        if s[i] == s[i+1] or s[i] == s[i-1]:
            continue
        else:
            sub.append(s[i])
    if s[-1] != s[n-2]:
        sub.append(s[n-1])
    sub = ''.join(sub)
    sub_len = len(sub)
    #for recursion
    if sub_len >= 2:
        if sub[0] == sub[1]:
            return remove_adjacent_dup(sub, sub_len)
    for i in range(1, sub_len-1):
        if sub[i] == sub[i+1] or sub[i] == sub[i-1]:
            return remove_adjacent_dup(sub, sub_len)
    if sub_len >= 2:
        if sub[-1] == sub[sub_len-2]:
            return remove_adjacent_dup(sub, sub_len)
    return sub


T = int(input())

while T > 0:
    str = input()
    n = len(str)
    print(''.join(remove_adjacent_dup(str, n)))
    T -= 1



# S = 'azxxzay'
# print(S)
# n = len(S)
# print(remove_adjacent_dup(S, n))
