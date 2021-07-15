#https://www.hackerrank.com/challenges/the-birthday-bar/problem

# from itertools import combinations

def birthday(s, d, m):
    # comb = list(combinations(s, m))
    # print(comb)
    res = 0
    for i in range(0, len(s)-m+1):
        tot = 0
        for j in range(i, i+m):
            tot += s[j]
        if tot == d:
            res += 1
    return res


n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
result = birthday(s, d, m)
print(result)


# 5
# 1 2 1 3 2
# 3 2