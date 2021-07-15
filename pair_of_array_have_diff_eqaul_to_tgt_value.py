def pairs(arr, k, n):
    count = 0
    for i,j in enumerate(arr):
        if i < n-1:
            if abs(j-arr[i+1]) == k:
                count += 1

    return count


n, k = input().split()
arr = (list(map(int, input().split())))
n = int(n)
k = int(k)
print(pairs(arr, k, n))
