# In
# the
# Byteland
# country, a
# string
# S is said
# to
# super
# ASCII
# string if and only if the
# count
# of
# each
# character in the
# string is equal
# to
# its
# ASCII
# value.In
# the
# Byteland
# country
# ASCII
# code
# of ‘a’ is 1, ‘b’ is 2, …, ‘z’ is 26.
# The
# task is to
# find
# out
# whether
# the
# given
# string is a
# super
# ASCII
# string or not.If
# true, then
# print “Yes” otherwise
# print “No”.
#
# Examples:
#
# Input: S = “bba”
# Output: Yes
# Explanation:
# The
# count
# of
# character ‘b’ is 2 and the
# ASCII
# value
# of ‘b’ is also
# 2.
# The
# count
# of
# character ‘a’ is 1. and the
# ASCII
# value
# of ‘a’ is also
# 1.
# Hence, string “bba” is super
# ASCII
# String.
#
# Input: S = “ssba”
# Output: No
# Explanation:
# The
# count
# of
# character ‘s’ is 2 and the
# ASCII
# value
# of ‘s’ is 19.
# The
# count
# of
# character ‘b’ is 1. and the
# ASCII
# value
# of ‘b’ is 2.
# Hence, string “ssba” is not a
# super
# ASCII
# String.



def checkSuperASCII(s):
    b = [0 for _ in range(1, 27)]
    for i in range(len(s)):
        index = ord(s[i]) - 97 + 1
        b[index - 1] += 1
    for i in range(len(s)):
        index = ord(s[i]) - 97 + 1
        if index != b[index - 1]: return 'No'
    return 'Yes'


s = str(input())
print(checkSuperASCII(s))
