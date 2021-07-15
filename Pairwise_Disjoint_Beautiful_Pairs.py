#https://www.hackerrank.com/challenges/beautiful-pairs/problem


def pairwise_disjoint(n, A, B):
    if n == 1:
        return 0
    max = 0
    temp_A = sorted(A[:])
    temp_B = sorted(B[:])
    if temp_A == temp_B:
        return n - 1
    for i in range(n):
        if A[i] in temp_B:
            max += 1
            temp_B.remove(A[i])
            temp_A.remove(A[i])
            # print(A)
            # print(B)
    if temp_A:
        return max + 1
    else:
        return max


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(pairwise_disjoint(n, A, B))

