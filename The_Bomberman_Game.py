def print_grid(x):
  for i in x:
    print(''.join(i))

r,c,n=map(int,input().split())
G=[]
for i in range(r):
  G.append(list(input()))
D=[['O' for j in range(c)] for i in range(r)]
A=[['.' for j in range(c)] for i in range(r)]
for i in range(r):
  for j in range(c):
    if not ((i+1<r and G[i+1][j]=='O') or (i-1>=0 and G[i-1][j]=='O') or (j+1<c and G[i][j+1]=='O') or (j-1>=0 and G[i][j-1]=='O')):
      if G[i][j]!='O':
        A[i][j]='O'
B=[['.' for j in range(c)] for i in range(r)]
for i in range(r):
  for j in range(c):
    if not ((i+1<r and A[i+1][j]=='O') or (i-1>=0 and A[i-1][j]=='O') or (j+1<c and A[i][j+1]=='O') or (j-1>=0 and A[i][j-1]=='O')):
      if A[i][j]!='O':
        B[i][j]='O'
if n==1:
  print_grid(G)
elif n%2==0:
  print_grid(D)
elif (n+1)%4==0:
  print_grid(A)
else:
  print_grid(B)



#
# def bomberMan(n, Grid):
#     g = []
#     # print(Grid)
#     for i in Grid:
#         z = list(i)
#         g.append(z)
#     # print(g)
#     full_bomb = []
#     r = len(g)
#     c = len(g[0])
#     # print(r,c)
#     for i in range(r):
#         x = 'O' * c
#         y = list(x)
#         full_bomb.append(y)
#     # print(full_bomb)
#     if n == 1:
#         same_g = []
#         for i in g:
#             same_g.append(''.join(i))
#         return same_g
#     if n == 2 or n % 2 == 0:
#         Res = []
#         for i in full_bomb:
#             Res.append(''.join(i))
#         return Res
#     if n >= 3:
#         for i in range(r):
#             for j in range(c):
#                 if g[i][j] == 'O':
#                     full_bomb[i][j] = '.'
#                     if i - 1 >= 0 and j - 1 >= 0 and i + 1 < r and j + 1 < c:
#                         full_bomb[i-1][j] = '.'
#                         full_bomb[i+1][j] = '.'
#                         full_bomb[i][j-1] = '.'
#                         full_bomb[i][j+1] = '.'
#                         continue
#                     else:
#                         if i == 0:
#                             if j == 0:
#                                 full_bomb[i + 1][j] = '.'
#                                 full_bomb[i][j + 1] = '.'
#                                 continue
#                             elif j == c-1:
#                                 full_bomb[i][j - 1] = '.'
#                                 continue
#                             else:
#                                 full_bomb[i][j + 1] = '.'
#                                 full_bomb[i + 1][j] = '.'
#                                 full_bomb[i][j - 1] = '.'
#                                 continue
#                         if i == r-1:
#                             if j == 0:
#                                 full_bomb[i - 1][j] = '.'
#                                 full_bomb[i][j + 1] = '.'
#                                 continue
#                             elif j == c-1:
#                                 full_bomb[i - 1][j] = '.'
#                                 full_bomb[i][j - 1] = '.'
#                                 continue
#                             else:
#                                 full_bomb[i - 1][j] = '.'
#                                 full_bomb[i][j + 1] = '.'
#                                 full_bomb[i][j - 1] = '.'
#                                 continue
#                         if j == 0:
#                             full_bomb[i - 1][j] = '.'
#                             full_bomb[i + 1][j] = '.'
#                             full_bomb[i][j + 1] = '.'
#                             continue
#                         if j == c-1:
#                             full_bomb[i - 1][j] = '.'
#                             full_bomb[i + 1][j] = '.'
#                             full_bomb[i][j - 1] = '.'
#                             continue
#         Res = []
#         for i in full_bomb:
#             Res.append(''.join(i))
#         return bomberMan(n-2, Res)
#
#
#
# rcn = input().split()
#
# r = int(rcn[0])
#
# c = int(rcn[1])
#
# n = int(rcn[2])
#
# grid = []
#
# for _ in range(r):
#     grid_item = input()
#     grid.append(grid_item)
# result = bomberMan(n, grid)
# print('\n'.join(result))

# 6 7 3
# .......
# ...O...
# ....O..
# .......
# OO.....
# OO.....
#
# 6 7 5
# .......
# ...O.O.
# ....O..
# ..O....
# OO...OO
# OO.O...


# .......
# ...O.O.
# ...OO..
# ..OOOO.
# OOOOOOO
# OOOOOOO

# OOO.O.O
# OO.....
# OO....O
# .......
# .......
# .......