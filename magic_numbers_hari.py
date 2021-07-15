import functools
s = [[4, 9, 2], 
     [3, 5, 7], 
     [8, 1, 5]]
magic_val=15
#is_magic_square
def is_magic_square(s,m):
  dr_count,dl_count=0,0
  for i in range(3):
    r_count,c_count=0,0
    k=i
    l=abs(i-2)
    dr_count+=s[i][k]
    dl_count+=s[i][l]
    for j in range(3):
      r_count+=s[j][i]
      c_count+=s[i][j]
    if r_count!=m or c_count!=m:
      return False
  if dr_count!=m or dl_count!=m:
    return False
  else:
    return True
# Replacement_cost
def replacement_cost(s,m):
  r,c,dr,dl=0,0,0,0
  for i in range(3):
    if i==1:
      j=i
    else:
      j=abs(i-1)
    k=i
    l=abs(i-2)
    r+=s[j][i]
    c+=s[i][j]
    dr+=s[i][k]
    dl+=s[i][l]
  return [m-r,m-c,m-dr,m-dl]
R=replacement_cost(s,magic_val)
#order:row->column->diagonal_right->diagonal_left
#row_check
def magic_check(s):
  s[1][0]+=R[0]
  if column_check(s):
    return s
  s[1][0]-=R[0]
  s[1][2]+=R[0]
  if column_check(s):
    return s
#column_check
def column_check(s):
  s[0][1]+=R[1]
  if dia_right(s):
    return s
  s[0][1]-=R[1]
  s[2][1]+=R[1]
  if dia_right(s):
    return s
  s[2][1]-=R[1]
  return False
#dia_right
def dia_right(s):
  s[0][0]+=R[2]
  if dia_left(s):
    return s
  s[0][0]-=R[2]
  s[2][2]+=R[2]
  if dia_left(s):
    return s
  s[2][2]-=R[2]
  return False
#dia_left
def dia_left(s):
  s[2][0]+=R[3]
  if is_magic_square(s,magic_val):
    return s
  s[2][0]-=R[3]
  s[0][2]+=R[3]
  if is_magic_square(s,magic_val):
    return s
  s[0][2]-=R[3]
  return False
rc=functools.reduce(lambda x,y: abs(x)+abs(y),R)
print(rc,magic_check(s))