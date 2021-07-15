# Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
# Structure is like below:
# |  |
# |_|
# We can trap 2 units of water in the middle gap.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. Each test case contains an integer N denoting the size of the array, followed by N space separated numbers to be stored in array.
#
# Output:
# Output the total unit of water trapped in between the blocks.
#
# Constraints:
# 1 <= T <= 100
# 3 <= N <= 107
# 0 <= Ai <= 108
#
# Example:
# Input:
# 2
# 4
# 7 4 0 9
# 3
# 6 9 9
#
# Output:
# 10
# 0
#
# Explanation:
# Testcase 1: Water trapped by block of height 4 is 3 units, block of height 0 is 7 units. So, total unit of water trapped is 10 units.

def total_unit_of_water(a, n):
    tot = 0
    left = [0] * n
    right = [0] * n
    left[0] = a[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], a[i])
    right[n - 1] = a[-1]
    for j in range(n - 2, -1, -1):
        right[j] = max(right[j + 1], a[j])
    for i in range(1, n - 1):
        tot = tot + min(left[i], right[i]) - a[i]

    return tot


N = 5
# A = [8, 8, 2, 4, 5, 5, 1]
# B = [9, 8, 1, 3, 5]
C = [7, 4, 8, 2, 5]

print(total_unit_of_water(C, N))

# T = int(input())
#
# while T > 0:
#     N = int(input())
#     A = list(map(int, input().split()))
#     print(total_unit_of_water(A, N))
#     T -= 1






















