# Jarvis is weak in computing palindromes for Alphanumeric characters.
# While Ironman is busy fighting Thanos, he needs to activate sonic punch but Jarvis is stuck in computing palindromes.
# You are given a string S containing alphanumeric characters. Find out whether the string is a palindrome or not.
# If you are unable to solve it then it may result in the death of Iron Man.
#
# Input:
# The first line of the input contains T, the number of test cases. T testcases follow.  Each line of the test case contains string 'S'.
#
# Output:
# Each new line of the output contains "YES" if the string is palindrome and "NO" if the string is not a palindrome.
#
# Constraints:
# 1<=T<=100
# 1<=|S|<=100000
# Note: Consider alphabets and numbers only for palindrome check. Ignore symbols and whitespaces.
#
# Example:
# Input:
# 2
# I am :IronnorI Ma, i
# Ab?/Ba
#
# Output:
# YES
# YES
#
# def Save_Ironman(s):
#     s = s.replace(" " , "")
#     s += ''
#     print(s)
#     res = []
#     for i in range(len(s)):
#         if s[i].isalnum():
#             res.append(s[i])
#     s = ''.join(res)
#     print(s)
#     print(s[::-1])
#     if s == s[::-1]:
#         return 'YES'
#     else:
#         return "NO"
#
#
# s = 'I am :IronnorI Ma, i'
# print(Save_Ironman(s))


def Save_Ironman(s):
    s += ''
    res = []
    s = s.lower()
    for i in range(len(s)):
        if s[i].isalnum():
            res.append(s[i])
    s = ''.join(res)
    reverse_of_s = s[::-1]
    print(s)
    print(reverse_of_s)
    if s == reverse_of_s:
        return 'YES'
    else:
        return "NO"


T = int(input())
while T > 0:
    S = input()
    print(Save_Ironman(S))
    T -= 1
