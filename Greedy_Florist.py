#https://www.hackerrank.com/challenges/greedy-florist/problem?h_r=next-challenge&h_v=zen

def florist(n, k, c):
    c.sort(reverse=True)
    print(c)
    res_sep = [c[i:i + k] for i in range(0, n, k)]
    # res_sep = []
    # for i in range(0, n, k):
    #     res_sep.append(c[i:i + k])
    print(res_sep)
    tot = 0
    j = 0
    for i in res_sep:
        # res_sep[i] = list(map(lambda x: x * (i+1), res_sep[i]))
        # print(res_sep[i])
        tot += (j + 1) * sum(i)
        j += 1
    return tot

n, k = input().split()
n = int(n)
k = int(k)
c = list(map(int, input().split()))
print(florist(n, k, c))