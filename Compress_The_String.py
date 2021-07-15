# You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
#
# For a better understanding of the problem, check the explanation.
#
# Input Format
#
# A single line of input consisting of the string .
#
# Output Format
#
# A single line of output consisting of the modified string.
#
# Constraints
#
# All the characters of  denote integers between  and .
#
#
# Sample Input
#
# 1222311
# Sample Output
#
# (1, 1) (3, 2) (1, 3) (2, 1)
# Explanation
#
# First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.
#
# Also, note the single space within each compression and between the compressions.
#
# Python 2


from itertools import groupby
def find_repeat_times(num, n):
    res = []
    num = list(num)
    for key, group in (groupby(num)):
        res.append((len(list(group)),int(key)))
    for i in res:
        print(i, end = ' ')


S= input()
n = len(S)
find_repeat_times(S, n)



# num = str(1222311)
#
# n = len(num)
# print(find_repeat_times(num, n))