# Given a string str containing alphanumeric characters, calculate sum of all numbers present in the string.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string containing alphanumeric characters.
#
# Output:
# Print the sum of all numbers present in the string.
#
# Constraints:
# 1<=T<=105
# 1<=length of the string<=105
#
# Example:
# Input:
# 4
# 1abc23
# geeks4geeks
# 1abc2x30yz67
# 123abc
#
# Output:
# 24
# 4
# 100
# 123
#
# Explanation:
# Testcase 1: 1 and 23 are numbers in the string which is added to get the sum as 24.
# Testcase 4: 123 is a single number, so sum is 123.
# import re
#
# def sum_of_no(s):
#     '''
#     Info: This function adds the numbers present in the string
#     EG:1abc23 => 1 and 23 are numbers in the string which is added to get the sum as 24.
#
#     '''
#     return sum(map(int, re.findall('\d+', s)))
#
#
# T = int(input())
#
#
# while T > 0:
#   S = str(input())
#   print(sum_of_no(S))
#   T -= 1


#another method


# Python3 program to calculate sum of
# all numbers present in a str1ing
# containing alphanumeric characters

# Function to calculate sum of all
# numbers present in a str1ing
# containing alphanumeric characters


def findSum(str1):
    temp = "0"
    Sum = 0
    for ch in str1:
        if (ch.isdigit()):
            temp += ch
            print(temp)
        else:
            Sum += int(temp)
            print(Sum)
            temp = "0"


    return Sum + int(temp)


str1 = "12abc20yz68"

print(findSum(str1))



