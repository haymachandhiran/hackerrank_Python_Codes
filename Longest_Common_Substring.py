# Given two strings X and Y. The task is to find the length of the longest common substring.
#
# Input:
# First line of the input contains number of test cases T. Each test case consist of three lines, first of which contains 2 space separated integers N and M denoting the size of string X and Y strings respectively. The next two lines contains the string X and Y.
#
# Output:
# For each test case print the length of longest  common substring of the two strings .
#
# Constraints:
# 1 <= T <= 200
# 1 <= N, M <= 100
#
# Example:
# Input:
# 2
# 6 6
# ABCDGH
# ACDGHR
# 3 2
# ABC
# AC
#
# Output:
# 4
# 1
#
# Example:
# Testcase 1: CDGH is the longest substring present in both of the strings.
def long_sub_string(a, b):
    l = min(len(a), len(b))
    res = 0
    x = ''
    res = 0
    x_len = 0
    if a in b or b in a:
        return l
    for i in range(len(a)):
        x = a[i]
        if b.find(x) == -1:
            continue
        for j in range(i+1, len(a)):
            if b.find(x+a[j]) == -1:
                break
            x = x + a[j]
        if len(x) > res:
            res = len(x)

    return res


T = int(input())

while T > 0:
    N, M = input().split()
    N = int(N)
    M = int(M)
    X = input()
    Y = input()
    print(long_sub_string(X, Y))
    T -= 1

