#https://www.youtube.com/watch?v=EKyvjySMmGc&list=PL7f0FYY_3hQDS79OekQv5PO7jCDGUaEyk&index=11

#Tak 2 numbers as input
#Print the unique digits
#Input1: 10 15 : Op= 0 2 3 4 5
#IP2: 100 105   : OP= 2 3 4 5

n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)
arr = list(range(n1, n2 + 1))
res = []
for i in arr:
    res.extend(str(i))
print(res)
op = []
for j in set(res):
    if res.count(j) == 1:
        op.append(j)
op.sort()
print(*op)

# a = 'abc'
# rs1 = []
# rs2 = []
# rs1.append(a)
# rs2.extend(a)
# print(rs1)
# print(rs2)
