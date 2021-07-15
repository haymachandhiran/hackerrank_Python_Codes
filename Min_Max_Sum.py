#https://www.hackerrank.com/challenges/mini-max-sum/problem


from itertools import combinations


def miniMaxSum(arr):
    comb = list(combinations(arr,4))
    sum_comb = []
    for i in comb:
        print(i)
        x = sum(i)
        print(x)
        sum_comb.append(x)
    min_val = min(sum_comb)
    max_val = max(sum_comb)
    print(str(min_val)+' '+str(max_val))


arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)