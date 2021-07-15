def maxMin(n, k, arr):
    arr.sort()
    print(arr)
    low = float('inf')
    for i in range(0, n-k+1):
        x = arr[i:i+k]
        print(f"x = {x}")
        print(f"max = {max(x)}")
        print(f"min = {min(x)}")
        if len(x) == k:
            if (max(x) - min(x)) < low:
                low = max(x) - min(x)
    return low


n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr_item = int(input())
    arr.append(arr_item)
print(maxMin(n, k, arr))


