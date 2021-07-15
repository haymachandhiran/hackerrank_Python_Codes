#https://www.hackerrank.com/challenges/gem-stones/problem

def gemstones(arr):
    temp = str(min(arr, key=len))
    min_str = (set(temp))
    l = len(min_str)
    # print(min_str)
    # print(l)
    arr.remove(temp)
    gems = 0
    for i in min_str:
        t = 0
        for j in range(len(arr)):
            if i in arr[j]:
                continue
            else:
                t = 1
                break
        if t == 0:
            gems += 1
    return gems


n = int(input())
arr = []
for i in range(n):
    x = input().rstrip()
    arr.append(x.lower())
print(gemstones(arr))

