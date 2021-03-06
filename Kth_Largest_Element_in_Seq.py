# Given an input stream of n integers, find the kth largest element for each element in the stream.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two lines. The first line of each test case contains two space separated integers k and n . Then in the next line are n space separated values of the array.
#
# Output:
# For each test case, in a new line, print the space separated values denoting the kth largest element at each insertion, if the kth largest element at a particular insertion in the stream doesn't exist print -1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= K <= n
# 1 <= n <= 106
# 1 <= stream[] <= 105
#
# Example:
# Input:
# 2
# 4 6
# 1 2 3 4 5 6
# 1 2
# 3 4
#
# Output:
# -1 -1 -1 1 2 3
# 3 4
#
# Explanation:
# Testcase1:
# k = 4
# For 1, the 4th largest element doesn't exist so we print -1.
# For 2, the 4th largest element doesn't exist so we print -1.
# For 3, the 4th largest element doesn't exist so we print -1.
# For 4, the 4th largest element is 1 {1, 2, 3, 4}
# For 5, the 4th largest element is 2 {2, 3, 4 ,5}
# for 6, the 4th largest element is 3 {3, 4, 5}

# def k_largest_element(arr, k):
#     res = []
#     checking = []
#     n = len(arr)
#     for i in range(n):
#         if i < k-1:
#             res.append(-1)
#             checking.append(arr[i])
#             continue
#         else:
#             checking.append(arr[i])
#             print(sorted(checking))
#             res.append(sorted(checking)[-k])
#     res = list(map(str, res))
#     return res


def k_largest_element(arr, k):
    res = []
    n = len(arr)
    for i in range(n):
        checking = []
        if i < k-1:
            res.append(-1)
            continue
        else:
            checking.extend(arr[i-k+1:i+1])
            res.append(sorted(checking)[0])
    res = list(map(str, res))
    return res


ARR = list(map(int, input().split()))
K = int(input())
N = len(ARR)
print(' '.join(k_largest_element(ARR, K)))
