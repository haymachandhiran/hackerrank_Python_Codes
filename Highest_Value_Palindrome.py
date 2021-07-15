#https://www.hackerrank.com/challenges/richie-rich/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def high_val_pal(s, n, k):
    s = list(s)
    mark = [0] * n
    l, r = 0, n-1
    while l <= r:
        if s[l] != s[r]:
            if s[l] > s[r]:
                s[r] = s[l]
                mark[r] += 1
            else:
                s[l] = s[r]
                mark[l] += 1
            k -= 1
        l += 1
        r -= 1
    if k < 0:
        return "-1"
    l, r = 0, n - 1
    while l <= r:
        if l == r and k >= 1:
            s[l] = '9'
            break
        if s[l] < '9':
            if mark[l] == 0 and mark[r] == 0 and k >= 2:
                s[l] = s[r] = '9'
                k -= 2
            if (mark[l] == 1 or mark[r] == 1) and k >= 1:
                s[l] = s[r] = '9'
                k -= 1
        l += 1
        r -= 1
    return ''.join(s)

n, k = input().split()
n = int(n)
k = int(k)
s = input().rstrip()
print(high_val_pal(s, n, k))
