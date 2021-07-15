# Given
# two
# arrays
# A and B
# of
# positive
# integers.Your
# task is to
# find
# numbers
# which
# are
# present in the
# first
# array, but
# not present in the
# second
# array.
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
# T
# denoting
# the
# number
# of
# test
# cases.Each
# test
# case
# contains
# space
# separated
# integers
# N and M
# which
# denotes
# the
# number
# of
# elements in the
# array
# A and B.Next
# two
# line
# contains
# space
# separated
# array
# elements.
#
# Output:
# Print
# space
# separated
# numbers
# present in the
# first
# array
# but not in the
# second.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N, M <= 107
# 1 <= Ai, Bi <= 1018
#
# Example:
# Input:
# 2
# 6
# 5
# 1
# 2
# 3
# 4
# 5
# 10
# 2
# 3
# 1
# 0
# 5
# 5
# 5
# 4
# 3
# 5
# 9
# 11
# 4
# 9
# 3
# 11
# 10
#
# Output:
# 4
# 10
# 5
#
# Explanation:
# Testcase
# 1: 4 and 10
# are
# present in first
# array
# while not in second array.


def val_in_first_not_second(a, b, n, m):
    for i in range(n):
        if a[i] not in b:
            print(a[i], end=' ')
    print()


T = int(input())
while T > 0:
    N, M = input().split()
    N = int(N)
    M = int(M)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    val_in_first_not_second(A, B, N, M)
    T -= 1
