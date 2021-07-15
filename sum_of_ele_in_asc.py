#Take size and Take array of integers
#Add up the elements in the asc order of their presence  and print final op
# 7 , [2,201,2,3,205,4,5] => 2+201 = 203; 2+3+205= 210; 4+5=9;
#Op: [203,210,9]
#Another qn - Print max val : Output = 210


n = int(input())
arr = list(map(int, input().split()))
res = []
arr.append(0)
tot = 0
for i in range(len(arr)-1):
    tot += arr[i]
    if arr[i] < arr[i+1]:
        pass
    else:
        res.append(tot)
        tot = 0
print(*res)
print(max(res))
