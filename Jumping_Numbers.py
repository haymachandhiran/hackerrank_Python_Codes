# Given a positive number X. Find all Jumping Numbers smaller than or equal to X.
# Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.
#
# Input:
# The first line of the input contains T denoting the number of testcases. Each testcase contain a positive number X.
#
# Output:
# Output all the jumping numbers less than X in sorted order. Jump to example for better understanding.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 109
#
# Example:
# Input:
# 2
# 10
# 50
# Output:
# 0 1 2 3 4 5 6 7 8 9 10
# 0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45
#
# Explanation:
# Testcase 2: Here, the most significant digits of each jumping number is following increasing order, i.e., jumping numbers starting from 0, followed by 1, then 2 and so on, themselves being in increasing order 2, 21, 23.


# def  adj_dif_equals_one(a):
#     a= str(a)
#     a+= ''
#     l = len(a)
#     if abs(int(a[1]) - int(a[0])) != 1:
#         return 0
#     for i in range(1, l-1):
#         if abs(int(a[i]) - int(a[i+1])) == 1:
#             continue
#         else:
#             return 0
#     return 1
#
#
# def jumping_numbers(n):
#     res = []
#     if n < 10:
#         for i in range(n+1):
#             res.append(str(i))
#     else:
#         res = [i for i in range(10)]
#         res = list(map(str, res))
#         for i in range(10, n+1):
#             if adj_dif_equals_one(i):
#                 res.append(str(i))
#     return res


#Another method only one function

def jumping_numbers(n):
    res = []
    if n < 10:
        for i in range(n+1):
            res.append(str(i))
    else:
        res = [i for i in range(10)]
        res = list(map(str, res))
        for i in range(10, n+1):
            i = str(i)
            i += ''
            temp = 0
            for j in range(len(i)-1):
                if abs(int(i[j]) - int(i[j+1])) != 1:
                    temp = 1
            if temp == 0:
                res.append(str(i))
            # if adj_dif_equals_one(i):
            #     res.append(str(i))
    return res


# T = int(input())
# while T > 0:
#     X = int(input())
#     print(' '.join(jumping_numbers(X)))
#     T -= 1

N = 100
print(' '.join(jumping_numbers(N)))



# def  adj_dif_equals_one(a):
#     a= str(a)
#     a+= ''
#     l = len(a)
#     if abs(int(a[1]) - int(a[0])) != 1:
#         return 0
#     for i in range(1, l-1):
#         if abs(int(a[i]) - int(a[i+1])) == 1:
#             continue
#         else:
#             return 0
#     return 1


#Another method

def n_is_jumping_numbers(n):
  n = str(n)
  n += ''
  temp = 0
  for j in range(len(n)-1):
    if abs(int(n[j]) - int(n[j+1])) != 1:
      temp = 1
  if temp == 0:
    return n

T = int(input())
while T > 0:
    X = int(input())
    if X > 9:
        x_great_10 = [str(i) for i in range(10)]
        a = list(map(n_is_jumping_numbers,range(10,X+1)))
        res = list(filter(None, a))
        x_great_10.extend(res)
        print(' '.join(x_great_10))
    else:
        x_less_10 = [str(i) for i in range(X+1)]
        print(x_less_10)
        print(' '.join(x_less_10))
    T -= 1
	
#Aonther Method
x=9
def jump(a):
  i=[a]
  while (i != []):
    j=i.pop()
    if j<=x:
      res.append(j)
      dig=j%10
      if dig == 0:
        i.append(j*10+(dig+1))
      elif dig == 9:
        i.append(j*10+(dig-1))
      else:
        i.append(j*10+(dig+1))
        i.append(j*10+(dig-1))

res=[0]
for k in range(1,10):
  jump(k)
print(*sorted(res))	