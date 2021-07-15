# A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# You are an FBI agent. You have to determine the total number of ways that message can be decoded.
# Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.
#
# Example :
# Given encoded message "123",  it could be decoded as "ABC" (1 2 3) or "LC" (12 3) or "AW"(1 23).
# So total ways are 3.
#
# Input:
# First line contains the test cases T.  1<=T<=1000
# Each test case have two lines
# First is length of string N.  1<=N<=40
# Second line is string S of digits from '0' to '9' of N length.
#
# Example:
# Input:
# 2
# 3
# 123
# 4
# 2563
# Output:
# 3
# 2
import string
def tot_decoding_mesg(x, n):

    if x.find('00') != -1:
        return '0'
    if '0' in x:
        if x.find('10') == -1 and x.find('20') == -1:
            return '0'
    decode = ''
    x += ' '
    tot = 0
    res = 0
    for i in range(n-1):
        if x[i] == '0':
            continue
        decode = x[i] + x[i+1]
        if int(decode) <= 26:
            tot = tot + 1
    if '0' in x:
        return str(tot)

x = '123'
print(x)
n = len(x)
y = '2563'
print(tot_decoding_mesg(x, n))


