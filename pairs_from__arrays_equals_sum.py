# Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains 3 lines . The first line contains 3 space separated integers N, M, X. Then in the next two lines are space separated values of the array A and B respectively.
#
# Output:
# For each test case in a new line print the sorted space separated values of all the pairs u,v where u belongs to array A and v belongs to array B, such that each pair is separated from the other by a ',' without quotes also add a space after the ',' . If no such pair exist print -1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N, M, X <= 106
# -106 <= A, B <= 106
#
# Example:
# Input:
# 2
# 5 5 9
# 1 2 4 5 7
# 5 6 3 4 8
# 2 2 3
# 0 2
# 1 3
# Output:
# 1 8, 4 5, 5 4
# 0 3, 2 1
#
# Explanation:
# Testcase 1: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.


def pair_of_sum(arr, brr, N, M, X):
    comp = []
    pair = {}
    ret = []
    arr.sort()
    print(arr)
    for i in range(N):
        comp.append(X - arr[i])
        if comp[i] in brr:
            ret.append(str(arr[i])+" "+str(comp[i]))# '-44 96', '-16 68'
    return pair


T = int(input())
while (T > 0):
    N, M, X = input().split()
    N = int(N)
    M = int(M)
    X = int(X)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    op = pair_of_sum(A, B, N, M, X)

    op = sorted(op.items())
    for i in op:
        if i == op[-1]:
            print(i[0], i[1], end  = '')
        else:
            print(i[0], i[1], end = ', ')
    # print(op)
    # res_dct = {op[i]: op[i + 1] for i in range(0, len(op), 2)}
    # print(res_dct)
    res = []
    # for key, value in op.items():
    #     res.append(str(key) + " " + str(value))
    # print(res)
    # if res:
    #     print(', '.join(res))
    # else:
    #     print(-1)
    T -= 1

#
# N = 2
# X = 3
# arr = [0,2]#[1, 2, 4, 5, 7]
# brr = [1,3]#[5, 6, 3, 4, 8]


    # for i in op:
    #     if i == op[-1]:
    #         print(i[0], i[1], end  = '')
    #     else:
    #         print(i[0], i[1], end = ', ')
    # print(op)
    # res_dct = {op[i]: op[i + 1] for i in range(0, len(op), 2)}
    # print(res_dct)
    # res = []
    # for key, value in op.items():
    #     res.append(str(key) + " " + str(value))
    # print(res)
	
	
	#
# N = 2
# X = 3
# arr = [0,2]#[1, 2, 4, 5, 7]
# brr = [1,3]#[5, 6, 3, 4, 8]

