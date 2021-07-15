# Given a string S, find length of the longest substring with all distinct characters.  For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is String str.
#
# Output:
# Print length of smallest substring with maximum number of distinct characters.
# Note: The output substring should have all distinct characters.
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ size of str ≤ 10000
#
# Example:
# Input:
# 2
# abababcdefababcdab
# geeksforgeeks
#
# Output:
# 6 eksforg   ksforge
# 7

def long_dis_substring(s, n):
    l = 0
    sub = ''
    for i in range(n):
        sub = s[i]
        for j in range(i+1, n):
            if s[j] in sub:
                break
            sub = sub + s[j]
        if len(sub) > l:
            l = len(sub)
    return l


T = int(input())

while T > 0:
    S = input()
    n = len(S)
    print(long_dis_substring(S, n))
    T-=1


