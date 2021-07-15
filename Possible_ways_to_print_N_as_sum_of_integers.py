#https://www.youtube.com/watch?v=JHDqH0kBSDg

# from itertools import combinations_with_replacement as cr
# n = 4
# count = 1
# for i in range(2, n):
#   for j in cr(range(1, n), i):
#     if sum(j) == n:
#       count += 1
# print(count)
#
# from itertools import combinations_with_replacement as cr
# n = 10
# count = 1
# x = list(cr(range(1,n), 2))
# print(x)
# for i in range(2,n):
#   for j in cr(range(1,n), i):
#     if sum(j) == n:
#       print(*j)
# print('1 '*n)


from itertools import combinations_with_replacement as cr
n = 100
count = 0
x = list(cr(range(1,n), 2))
res = []
for i in x:
    if sum(i) == n:
        res.append(i)
for j in range(len(res)-1):
    print(res[j], end=', ')
print(res[-1])

map(print(res), res)

#for i in range(1, n):
