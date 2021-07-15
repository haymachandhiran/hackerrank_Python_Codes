# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.
#
# Output:
# For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= Ai <= 1010
#
# Example:
# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10
# Output:
# 2 4
# 1 5
#
# Explanation :
# Testcase1: sum of elements from 2nd position to 4th position is 12
# Testcase2: sum of elements from 1st position to 5th position is 15

T = int(input())


def pos_of_sub_array(arr, n, s):
    start = 0
    end = 0
    for i in range(n):
        tot = 0
        start = i + 1
        for j in range(i, n):
            tot += arr[j]
            if tot < s:
                pass
            elif tot == s:
                end = j + 1
                return str(start), str(end)
            else:
                break
        # if end:
        #     break
    # if end:
    #     return str(start), str(end)
    # else:
    return None


while T > 0:
    N, S = input().split()
    N = int(N)
    S = int(S)
    arr = list(map(int, input().split()))
    op = pos_of_sub_array(arr, N, S)
    if op:
        print(' '.join(op))
    else:
        print(-1)
    T -= 1





