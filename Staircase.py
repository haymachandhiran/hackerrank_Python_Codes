#https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_v=zen

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        res = ['#'] * n
        for j in range(0, n - i - 1, 1):
            res[j] = ' '
        print(*res, sep='')


n = int(input())
staircase(n)
