#https://www.hackerrank.com/challenges/luck-balance/problem

def luckBalance(k, contests):
    min_win = 0
    res_imp = []
    res_not_imp = []
    for i in range(len(contests)):
        if contests[i][1] == 1:
            res_imp.append(contests[i][0])
        else:
            res_not_imp.append(contests[i][0])
    print(res_imp)
    print(res_not_imp)
    for i in range(len(res_imp) - k):
        x = min(res_imp)
        min_win += x
        res_imp.remove(x)
    return sum(res_imp) + sum(res_not_imp) - min_win


n, k = input().split()
n = int(n)
k = int(k)
contests = []
for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))
result = luckBalance(k, contests)
print(result)
