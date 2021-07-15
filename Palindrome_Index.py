#https://www.hackerrank.com/challenges/palindrome-index/problem
#
# def palindromeIndex(s):
#     s = list(s)
#     # temp1 = s
#     # print(temp1.pop(3))
#     print(s)
#     print(s[::-1])
#     if s == s[::-1]:
#         return -1
#     for i in range(len(s)):
#         temp = s.copy()
#         print(temp)
#         print(s)
#         x = temp.pop(i)
#         print(x)
#         print(i)
#         if temp == temp[::-1]:
#             return i
#         else:
#             continue
#     return -1
#
#
# s = 'aaab'
# print(palindromeIndex(s))


for _ in range(int(input())):
    s = input()
    sr=s[::-1]
    for i in range(len(s)//2):
        if s[i]!=sr[i]:
            if s[i+1:i+3]==sr[i:i+2]:
                print(i)
            else:
                print(len(s)-1-i)
            break
    else:
          print(-1)