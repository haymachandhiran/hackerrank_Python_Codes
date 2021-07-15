# You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.
# Note: Expected solution in O(n) time using constant extra space.
#
# Input:
# First line consists of T test cases. First line of every test case consists of N, denoting the number of elements in array. Second line of every test case consists of elements in array.
#
# Output:
# Single line output, print the smallest positive number missing.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 106
# -106 <= arr[i] <= 106
#
# Example:
# Input:
# 2
# 5
# 1 2 3 4 5
# 5
# 0 -10 1 3 -20
# Output:
# 6
# 2
#
# Explanation:
# Testcase 1: Smallest positive missing number is 6.
# Testcase 2: Smallest positive missing number is 2.

def small_pos_no(arr):
    res = 0
    temp = 0
    arr.sort()
    print(arr)
    arr = list(filter(lambda x: x > 0, arr))
    print(arr)
    min_pos = arr[0]
    print(min_pos)
    n = len(arr)
    if arr[0] > 1:
        return 1
    else:
        for i in range(n-1):
            if arr[i] == arr[i + 1] or arr[i + 1] - arr[i] == 1:
                continue
            else:
                return arr[i] + 1
    return arr[-1] + 1


ARR = list(map(int, input().split()))
N = len(ARR)
print(small_pos_no(ARR))
