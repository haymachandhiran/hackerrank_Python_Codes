#https://www.hackerrank.com/challenges/grid-challenge/problem?h_r=next-challenge&h_v=zen


def gridChallenge(grid, n):
    res = []
    for i in range(n):
        res.append(''.join(sorted(grid[i])))
    temp = 0
    for i in range(1, n):
        for j in range(len(res[0])):
            if res[i][j] >= res[i-1][j]:
                continue
            else:
                temp = 1
                break
    if temp == 1:
        return 'NO'
    else:
        return 'YES'


t = int(input())
for t_itr in range(t):
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = gridChallenge(grid, n)
    print(result+'\n')
