a = [2, 5, 200, 10, 15, 150, 25]
a.append(0)
n = len(a)
temp = []
profit = 0
for i in range(n-1):
    temp.append(a[i])
    if a[i] <= a[i+1]:
        pass
    else:
        if profit <= (temp[-1] - temp[0]):
            profit = temp[-1] - temp[0]
        temp.clear()
print(profit)
