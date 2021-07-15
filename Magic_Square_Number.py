from itertools import islice
n = int(input())
s = list(map(int, input().split()))
sr = iter(s)
s = [list(islice(sr, n)) for _ in range(n)]
res = 0
magic_number = int(n * (n ** 2 + 1) / 2)
print(f'Magic Number is {magic_number}')
#d1
d1_sum = 0
for i in range(n):
    d1_sum = d1_sum + s[i][i]
print(f'Diagonal one sum = {d1_sum}')
res = res + abs(magic_number - d1_sum)
#d2
d2_sum = 0
l = 0
for j in range(n-1, -1, -1):
    d2_sum = d2_sum + s[j][l]
    l += 1
print(f'Diagonal two sum = {d2_sum}')
res = res + abs(magic_number - d2_sum)
#row_check
for row in range(1, n-1):
    row_count = 0
    for col in range(n):
        row_count += s[row][col]
    res = res + abs(magic_number - row_count)
#column_check
for col in range(1, n-1):
    col_count = 0
    for row in range(n):
        col_count += s[row][col]
    res = res + abs(magic_number - col_count)

print(f'Total replacement cost: {res}')
