# Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.

# Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated array elements.

# Output:
# For each test case, in a new line print the required element. If no such element present in array then print -1.

# Constraints:
# 1 <= T <= 100
# 3 <= N <= 106
# 1 <= A[i] <= 106

# Example:
# Input:
# 3
# 4
# 4 2 5 7
# 3
# 11 9 12
# 6
# 4 3 2 7 8 9

# Output:
# 5
# -1
# 7
# Explanation:
# Testcase 1 : Elements on left of 5 are smaller than 5 and on right of it are greater than 5.

# Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.

# Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated array elements.

# Output:
# For each test case, in a new line print the required element. If no such element present in array then print -1.

# Constraints:
# 1 <= T <= 100
# 3 <= N <= 106
# 1 <= A[i] <= 106

# Example:
# Input:
# 3
# 4
# 4 2 5 7
# 3
# 11 9 12
# 6
# 4 3 2 7 8 9

# Output:
# 5
# -1
# 7
# Explanation:
# Testcase 1 : Elements on left of 5 are smaller than 5 and on right of it are greater than 5.

T = int(input())


def find_grt_sml(brr, n):
    left_max = [None] * n
    left_max[0] = float('-inf')
    right_min = float('inf')
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], brr[i - 1])
    for j in range(n - 1, -1, -1):
        if left_max[j] < brr[j] and brr[j] < right_min:
            return left_max[j]
        right_min = min(right_min, brr[j])
    return -1


while (T > 0):
    N = int(input())
    arr = (list(map(int, input().split())))
    print(find_grt_sml(arr, N))
    T -= 1
