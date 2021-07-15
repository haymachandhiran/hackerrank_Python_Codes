def organizingContainers(c, n):
    print(c)
    row_sum = []
    clm_sum = []
    for i in range(n):
        row_sum.append(sum(c[i]))
    print(row_sum)
    for i in range(n):
        temp = 0
        for j in range(n):
            temp += c[j][i]
        clm_sum.append(temp)
    print(clm_sum)
    row_sum.sort()
    clm_sum.sort()
    if row_sum == clm_sum:
        return 'Possible'
    else:
        return 'Impossible'


N = int(input())
container = []
for _ in range(N):
    container.append(list(map(int, input().rstrip().split())))
print(organizingContainers(container, N))
