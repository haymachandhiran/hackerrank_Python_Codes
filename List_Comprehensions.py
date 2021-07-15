from itertools import permutations

x = int(input())
y = int(input())
z = int(input())
n = int(input())
perm = permutations([x, y, z])
res = []
for i in perm:
    print(i)
    if sum(i) == n:
        res.append(list(i))

print(res)